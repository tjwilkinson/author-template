# Research: Meeting Notes & Google Calendar Integration

This document summarizes research on integrating meeting notes features with Google Calendar, inspired by apps like `fellow.app`.

## Core Concepts & Features

Common features across `fellow.app` and similar tools (Hugo, Range, Hypercontext, Notion Calendar):

1.  **Calendar Integration (Google Calendar/Outlook):**
    *   Syncs with user calendars.
    *   Surfaces upcoming meetings.
    *   Attaches notes/agendas directly to calendar events (key linking mechanism).
    *   Often automatically creates note structures based on calendar events (attendees, date, time, templates).

2.  **Collaborative Agendas:**
    *   Pre-meeting agenda building.
    *   Structured sections (Talking Points, Action Items, Notes).
    *   Often shared via calendar event description or link.

3.  **Real-time Note Taking:**
    *   Dedicated space during meetings.
    *   Rich text/Markdown support.
    *   Multi-user collaboration.

4.  **Action Item Tracking:**
    *   Identify/assign action items within notes (checkboxes, @mentions, due dates).
    *   Syncs to internal task lists or external task managers (Jira, Asana, etc.).

5.  **Meeting Templates:**
    *   Reusable templates for different meeting types (1-on-1s, team syncs).

6.  **AI Features (Increasingly Common):**
    *   AI Copilot: Record, transcribe, summarize virtual meetings.
    *   AI Action Item Detection.
    *   AI Insights: Query past meetings.

7.  **Centralization & Search:**
    *   Central repository for meeting artifacts.
    *   Search across past meetings.

8.  **Integrations:**
    *   Beyond calendars/tasks: Slack, CRM, video conferencing.

## How Linking Typically Works

*   Uses Google Calendar API (OAuth) to read events.
*   Stores `google_calendar_event_id` alongside internal note/agenda records.
*   App's internal calendar view queries notes based on `event_id`.
*   Browser extensions may inject links into Google Calendar UI.
*   Calendar event updates (time/attendees) sync back to the app's note.

## Implementation Ideas for Cadence Cornerstone OS (Phase 7 Target)

Leveraging existing `Notes`, `Tasks`, `Tags`, and user roles:

1.  **Meeting Identification:** Use the existing `tags` system. Notes related to meetings should be assigned a specific "Meeting" tag (or potentially more granular tags like "Coaching Meeting").
    *   *Implication:* UI needs to support tagging notes; backend queries for meeting views need to filter by tag.

2.  **Enhance `Notes` Schema:** Add fields relevant to meetings:
    *   `google_calendar_event_id` (TEXT, nullable, unique index if possible): Stores the ID from the Google Calendar event.
    *   `meeting_start_time` (TIMESTAMPTZ, nullable): Fetched from the calendar event.
    *   `meeting_end_time` (TIMESTAMPTZ, nullable): Fetched from the calendar event.
    *   `attendee_emails` (TEXT[], nullable): Raw list of attendee emails fetched from the calendar event.

3.  **Attendee Relationships (`note_attendees` Table):** Create a linking table:
    *   `note_id` (UUID, FK to `notes.id`)
    *   `user_id` (UUID, FK to `auth.users(id)`)
    *   Primary Key (`note_id`, `user_id`)
    *   *Implication:* When linking a note to a calendar event, fetch attendees, iterate through emails, find matching internal users via `auth.users` based on email, and populate this table.

4.  **Calendar UI View:** Create a new section/page displaying events fetched from the user's Google Calendar API.

5.  **Linking Logic (Read-Only Sync initially):**
    *   In calendar view, check for existing `Note` with matching `google_calendar_event_id` **AND** the "Meeting" tag. Provide link if found.
    *   If not found, provide "Create Meeting Notes" button.
    *   Button click -> Create new `Note`, assign "Meeting" tag, fetch event details (title, time, attendees), populate `notes` fields (`google_calendar_event_id`, times, `attendee_emails`), resolve and populate `note_attendees` table, save note (potentially using a template).

6.  **Action Item Integration:**
    *   Enhance note editor to easily create `Tasks` from note content.
    *   Add `source_note_id` (UUID, nullable, FK to `notes.id`) to the `tasks` table.
    *   When a task is created from a note, populate `source_note_id`.
    *   RACI (implemented in Phase 5) will apply to these tasks just like any other task.

7.  **Templates:** Implement a template system for `Notes`, selectable when creating meeting notes.

8.  **Coach View:** Coaches need a view/filter to see meeting notes for their linked clients:
    *   Requires `coach_client_links` table (Phase 6).
    *   Query `notes` joined with `note_tags` (where tag = "Meeting" or "Coaching Meeting") and `note_attendees` (where `user_id` = `client_id`).
    *   Alternatively, filter notes where `tag` = "Meeting" AND `created_by_user_id` = `client_id` (simpler if coaches don't attend all client meetings but notes are client-owned).
    *   Sort results chronologically.

9.  **Bidirectional Sync (Future Enhancement - High Complexity):**
    *   **Write App -> Calendar:**
        *   Requires Google Calendar API **write scope** during OAuth.
        *   UI buttons ("Schedule Meeting" on notes/tasks).
        *   Backend API endpoint to call Google Calendar `events.insert`.
        *   Update the local `Note`/`Task` with the returned `eventId`.
    *   **Update/Delete Sync:** Requires handling updates/deletes initiated in *either* system and propagating them, which is complex.

10. **Permissions:** Note visibility should respect calendar attendees (checking `note_attendees`) and tenant RBAC for shared meetings. 