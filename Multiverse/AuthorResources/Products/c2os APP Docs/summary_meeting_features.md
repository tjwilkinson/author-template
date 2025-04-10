# Summary: Meeting Notes & Calendar Integration Features (Phase 7 Target)

## Core Concepts (Inspired by tools like Fellow.app)
*   Link notes/agendas to calendar events.
*   Collaborative agenda building, real-time notes, action item tracking.

## Implementation Ideas for C²OS
*   **Identify Meetings:** Use a specific `Tag` (e.g., "Meeting") on Notes.
*   **Enhance `Notes` Schema:** Add `google_calendar_event_id` (TEXT), `meeting_start_time` (TIMESTAMPTZ), `meeting_end_time` (TIMESTAMPTZ), `attendee_emails` (TEXT[]).
*   **`note_attendees` Table:** Link `notes` to internal `users` based on attendee emails (`note_id`, `user_id`).
*   **Calendar UI View:** Display user's GCal events.
*   **Linking Logic (Read-Only Sync Initially):**
    *   Check for existing Note with matching `google_calendar_event_id` + "Meeting" tag. Show link.
    *   "Create Meeting Notes" button -> Creates Note, adds tag, populates fields from GCal event, populates `note_attendees`.
*   **Action Item Integration:**
    *   Enhance note editor to easily create Tasks.
    *   Add `source_note_id` (UUID, FK to `notes`) to `tasks` table.
*   **Templates:** Implement Note templates for meetings.
*   **Coach View:** Filter/view client meeting notes (requires `coach_client_links`).
*   **Bidirectional Sync (Future - High Complexity):** Requires write scope, careful handling of updates/deletes initiated in either system.
*   **Permissions:** Respect calendar attendees (`note_attendees`) and tenant RBAC. 