# Mobile App Strategy

This document outlines the strategic goals, key focus areas, and technical considerations for the [App Name] mobile application.

## 1. Philosophy & Goals

*   **Primary Goal:** Provide a fast, convenient, and focused experience for core productivity workflows, particularly on the go.
*   **Key Principles:**
    *   **Capture Emphasis:** Mobile is ideal for quick capture of thoughts, tasks, and notes into the Inbox.
    *   **Core Workflow Focus:** Prioritize seamless execution of the TRO daily workflow (Capture, Triage/Process essentials, View Lists by Context/Date).
    *   **Review & Planning Support:** Facilitate on-the-go review of task lists, upcoming items, and potentially simplified weekly planning/review elements.
    *   **Not Feature Parity (Initially):** The initial mobile MVP will likely *not* replicate every single feature available on the web application (e.g., complex tenant admin, deep goal hierarchy editing). Focus on the most frequent and mobile-relevant actions.
    *   **Performance:** The app must feel fast and responsive.

## 2. Key Feature Priorities (Mobile MVP - Aligning with Plan Phases)

*   **Phase 2 Focus:**
    *   **Quick Capture:** Easily add items to the Inbox.
    *   **Inbox Triage:** Basic processing of inbox items (assigning context, simple dates, moving to Someday/Maybe).
    *   **Task Lists:** View tasks by context, date (Today, Upcoming), project.
    *   **Task Detail View:** View task details, mark tasks complete.
    *   **Basic Project View:** View projects and associated tasks.
    *   **Basic Notes View:** View and capture simple notes.
    *   **Offline Access:** Critical data (e.g., Today's tasks, Inbox) should be accessible offline, with changes syncing upon reconnection.
*   **Phase 3 Additions:**
    *   View Goals and associated Tactics.
    *   View Trackers and enter tracker data.
    *   Simplified Weekly Review prompt/checklist.
*   **Later Phases:**
    *   View Tenant-scoped items (tasks, projects).
    *   Notifications (delegations, mentions, etc.).
    *   Delegate tasks / manage delegations.
    *   Coach/Client communication features.

## 3. Technical Considerations

*   **Technology:** (As per `plan.md` - *Suggest Technology*) React Native or Flutter are strong candidates for cross-platform development, leveraging existing web frontend skills if applicable (React Native).
*   **Offline Strategy:**
    *   Need a local database (e.g., SQLite, WatermelonDB, Realm) to store cached data.
    *   Define which data needs to be available offline (e.g., user's active tasks, inbox, recent notes, current cycle goals/tactics).
    *   Implement a robust synchronization mechanism to handle data changes made offline and sync conflicts.
*   **API Design:** Ensure APIs are mobile-friendly (e.g., appropriate payload sizes, efficient endpoints for common mobile views).
*   **UI/UX:** Design specifically for mobile interaction patterns (touch targets, navigation, screen size constraints). Avoid simply shrinking the web UI.
*   **Push Notifications:** Requires integration with platform notification services (APNS for iOS, FCM for Android).

## 4. Non-Goals (Initially)

*   Full Tenant Administration features.
*   Complex reporting or data visualization (beyond basic tracker charts).
*   Editing complex role/permission structures.
*   White-label configuration. 