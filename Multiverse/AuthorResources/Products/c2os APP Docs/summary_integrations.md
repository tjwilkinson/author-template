# Summary: External Integrations (GHL & Google Calendar)

## GoHighLevel (GHL)
*   **Purpose:** Manage Tenant activation/deactivation based on GHL subscription status (via Webhooks). Avoids building separate tenant billing initially.
*   **Mechanism:**
    *   Webhook from GHL (e.g., on tag add/remove) to a dedicated C²OS endpoint.
    *   Requires `tenants.ghl_identifier` to link payload to C²OS tenant record.
    *   C²OS action: Update tenant status (`active`/`inactive`) based on webhook event type.
*   **Security:** Secure endpoint (shared secret verification if possible). Validate payload.
*   **Reliability:** Log webhooks, consider reconciliation mechanism for missed events.

## Google Calendar
*   **Purpose:** Allow users to view scheduled C²OS items on Google Calendar, block time for tasks.
*   **Mechanism:** Google OAuth 2.0, Google Calendar API.
*   **Scope:** Requires `calendar.events` (read/write).
*   **Initial Sync Direction (MVP):** One-way push from C²OS Task -> Google Calendar Event.
    *   Tasks with Do/Due Date/Time can be pushed.
    *   Representation: Title, link back, time based on task date. User might select target calendar.
*   **Time Blocking:** Allow users to create GCal events for specific time blocks for tasks directly from C²OS.
*   **Authorization:** Securely store user OAuth tokens (access/refresh). Handle refresh flow. Allow connect/disconnect.
*   **Future:** Two-way sync is complex (updates/deletes, conflicts). Meeting Notes integration has separate detailed requirements. 