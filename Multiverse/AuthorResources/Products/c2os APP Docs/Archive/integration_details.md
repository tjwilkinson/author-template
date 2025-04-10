# Integration Details

This document captures specific technical considerations and expected flows for key external integrations: GoHighLevel (GHL) and Google Calendar.

## 1. GoHighLevel (GHL) Integration

*   **Purpose:** Manage Tenant activation/deactivation based on subscription status within GHL. Avoids building a separate subscription management system for Tenants initially.
*   **Mechanism:** Webhooks from GHL to a dedicated endpoint in [App Name].
*   **Tenant Linking:** The `tenants` table in [App Name] needs a `ghl_identifier` field (e.g., GHL Location ID or a custom identifier managed in GHL) to link the webhook payload to the correct tenant record.
*   **Webhook Events:**
    *   **Subscription Activated/Resumed:**
        *   *Trigger:* A specific tag is added, a custom field is updated, or a user is added to a specific GHL workflow/membership level indicating access to [App Name]. (Exact trigger needs GHL setup definition).
        *   *Payload Expectation:* Should ideally contain the `ghl_identifier` and an event type indicating activation.
        *   *[App Name] Action:* Find tenant by `ghl_identifier`. Set tenant status to `active`. Enable relevant features (e.g., allow invites, unlock tenant-scoped creation).
    *   **Subscription Deactivated/Cancelled/Paused:**
        *   *Trigger:* The tag/field/membership indicating access is removed or changed in GHL.
        *   *Payload Expectation:* Should ideally contain the `ghl_identifier` and an event type indicating deactivation.
        *   *[App Name] Action:* Find tenant by `ghl_identifier`. Set tenant status to `inactive` or `restricted`. Prevent new member invites. Potentially restrict access to existing tenant data (read-only?) or specific features. (Exact behavior on deactivation needs definition - graceful degradation vs. hard cutoff).
*   **Security:**
    *   The webhook endpoint must be secured (e.g., using a shared secret signature verification provided by GHL if possible, or IP whitelisting).
    *   Validate incoming payload structure and `ghl_identifier` format.
*   **Error Handling & Resilience:**
    *   What happens if a webhook is missed? Need a way to potentially reconcile tenant status periodically (e.g., an admin function to query GHL status or re-sync).
    *   Log all incoming webhooks and actions taken.
    *   Implement retry logic for transient processing errors.
*   **Setup:** Requires configuring the webhook URL and triggers within the relevant GHL account(s).

## 2. Google Calendar Integration

*   **Purpose:** Allow users to view scheduled tasks from [App Name] on their Google Calendar and potentially block time.
*   **Mechanism:** Google OAuth 2.0 for authorization. Google Calendar API.
*   **Scope:** Requires `calendar.events` scope (read/write).
*   **Data Flow (Two-Way Sync):**
    *   **[App Name] Task -> Google Calendar Event:**
        *   Tasks with a specific Do Date/Time or Due Date/Time can be pushed to a selected Google Calendar.
        *   Representation: How should tasks appear? (e.g., Event Title: "[Task Name]", Description: Link back to task in [App Name], Time: Based on Do/Due Date). Should users choose the target calendar?
        *   Sync Trigger: On task creation/update with relevant date/time.
    *   **Google Calendar Event -> [App Name] (Potential/Future):**
        *   More complex. Should creating an event in a specific Google Calendar create a task in [App Name]? How to handle updates/deletions?
        *   *Initial MVP likely focuses on one-way push from [App Name] to Google Calendar for simplicity.*
*   **Time Blocking:**
    *   Users might want to explicitly block time for tasks on their calendar directly from [App Name].
    *   This would involve creating a Google Calendar event with the task details and a specific time block selected by the user.
*   **Authorization Management:**
    *   Need secure storage for user Google OAuth tokens (access and refresh tokens).
    *   Handle token expiry and refresh flows.
    *   Allow users to connect/disconnect their Google Calendar.
*   **Conflict Resolution (if two-way):** How to handle updates made in both systems simultaneously? (Last update wins? Prompt user?). *Avoids complexity if initially one-way.*
*   **Rate Limiting:** Be mindful of Google API rate limits. 