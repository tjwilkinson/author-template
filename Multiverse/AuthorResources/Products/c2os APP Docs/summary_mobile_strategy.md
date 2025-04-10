# Summary: Mobile App Strategy

## Philosophy & Goals
*   **Primary Goal:** Fast, convenient, focused experience for core workflows (Capture, Triage/Process, View Lists).
*   **Not Initial Feature Parity:** MVP focuses on most frequent/mobile-relevant actions.
*   **Performance:** Must be fast and responsive.

## Key Feature Priorities
*   **MVP (Aligns Phase 2/3):** Quick Capture, Inbox Triage, View Task Lists (Context, Date, Project), View Task Details, Mark Complete, Basic Project/Note View, View Goals/Tactics, View/Enter Trackers, Simplified Weekly Review prompt, **Offline Access (Critical)**.
*   **Later Phases:** View Tenant items, Notifications, Delegation, Coach/Client features.

## Technical Considerations
*   **Technology:** React Native with Expo.
*   **Offline Strategy:**
    *   Requires local database (e.g., SQLite, WatermelonDB, Realm).
    *   Define offline data scope (active tasks, inbox, etc.).
    *   Robust sync mechanism needed.
*   **API Design:** Mobile-friendly endpoints.
*   **UI/UX:** Design specifically for mobile patterns.

## Non-Goals (Initially)
*   Full Tenant Administration.
*   Complex reporting/visualization.
*   Editing roles/permissions. 