# User Personas and Key Flows

This document outlines the primary user types interacting with the [App Name] platform and describes key interaction flows, particularly those involving multiple user types or unique features.

## 1. User Personas

*   **Individual User (Free):**
    *   **Goal:** Manage personal tasks, projects, and potentially basic goals using the core TRO workflow.
    *   **Key Features:** Task Management (Inbox, Processing, Contexts, Lists), Basic Project Management, Notes/Resources (Personal Scope).
    *   **Limitations:** May have limits on active projects, advanced features (e.g., complex recurring tasks, advanced goal setting, trackers), delegation capabilities, or connecting with coaches.
*   **Individual User (Pro - Paid):**
    *   **Goal:** Maximize personal productivity using the full suite of integrated methodologies (TRO, RPM, 12WY, Compound Effect).
    *   **Key Features:** All Free features plus Advanced Goal Setting (Visions, 12WY Cycles/Goals/Tactics), Custom Trackers, Weekly Planning & Review, Execution Score, User-to-User Task Delegation, Ability to connect with a Coach.
*   **Tenant Member:**
    *   **Goal:** Collaborate on team/company projects and tasks within a specific organization or coaching practice context, while potentially also managing personal productivity.
    *   **Key Features:** Access to Tenant-scoped Projects, Tasks, Goals, Notes/Resources based on assigned Role/Permissions (RBAC). Participate in RACI assignments. May use personal features depending on their individual plan type (Free/Pro).
    *   **Context:** Operates within the tenant's defined structure and branding (white-label).
*   **Tenant Admin:**
    *   **Goal:** Manage the organization's or coaching practice's tenant within the app, including users, roles, permissions, and settings.
    *   **Key Features:** All Tenant Member features plus User Management (Invites, Role Assignment), Custom Role Creation/Permission Management, White-Label Settings configuration, potentially Billing/Subscription Management (if not solely via GHL), viewing Tenant-level analytics (future).
*   **Coach (User within a 'Coaching' Tenant Type):**
    *   **Goal:** Manage their coaching practice, onboard clients, view client progress, provide feedback, and potentially share templates.
    *   **Key Features:** Tenant Admin features (likely), plus Coach Dashboard (client overview), ability to accept connection requests from Clients, permission-based visibility into connected Client's data (Goals, Tasks, Trackers, Reviews), In-app commenting/feedback with Clients, Templating Engine (create/share templates).
*   **Client (Individual User Pro connected to a Coach):**
    *   **Goal:** Leverage the platform for personal productivity while receiving guidance and accountability from their Coach.
    *   **Key Features:** All Individual User Pro features plus the ability to initiate a connection request to a Coach, share specific data (based on permissions granted) with their Coach, receive feedback/comments from the Coach, potentially use templates provided by the Coach.

## 2. Key Interaction Flows

*   **User Onboarding (Individual):**
    1.  Sign up via Google Sign-In.
    2.  Guided tour explaining the core TRO concepts (Capture, Clarify, Organize, Reflect, Engage) and basic app navigation (Inbox, Task Lists).
    3.  Prompt to create first few tasks or capture initial thoughts into the Inbox.
    4.  (Pro users) Introduction to Goal Setting (RPM/12WY) and Trackers.
*   **Tenant Onboarding (Admin Initiated):**
    1.  Tenant Admin creates the Tenant (potentially triggered via GHL).
    2.  Admin configures initial White-Label settings.
    3.  Admin invites Tenant Members via email.
    4.  Invited user clicks link, signs in (or up) with Google.
    5.  User accepts invitation and is added to the Tenant, assigned a default role.
    6.  User now sees the Tenant context available in their account.
*   **User-to-User Task Delegation (Pro User Initiates):**
    1.  User A (Pro) creates a Task.
    2.  User A chooses to delegate the task, searches for User B (can be Free or Pro).
    3.  User A assigns the task to User B, potentially adding notes.
    4.  User B receives a notification about the delegated task.
    5.  User B can view the task details (potentially limited view based on permissions) and update its status.
    6.  User A can track the status of the delegated task.
*   **Coach-Client Connection:**
    1.  Client (Pro User) searches for their Coach (User within a Coaching Tenant) within the app.
    2.  Client sends a connection request to the Coach.
    3.  Coach receives the request notification.
    4.  Coach reviews and accepts the connection request.
    5.  The connection is established, granting the Coach permission-based visibility into the Client's specified data (e.g., Goals, Tasks, Trackers, Weekly Reviews).
    6.  Coach can view Client progress on their dashboard and provide feedback via comments on relevant items.
    7.  Client can see Coach comments.
    8.  Either party can terminate the connection.
*   **Tenant Task Collaboration (RACI Example):**
    1.  Tenant Member A creates a Project within the Tenant context.
    2.  Member A creates Task 1 within the Project.
    3.  Member A assigns RACI roles for Task 1: Member B (Responsible), Member A (Accountable), Member C (Consulted), Team Lead D (Informed).
    4.  Member B works on the task and updates status.
    5.  Member C is notified or can easily filter to see tasks where they are consulted.
    6.  When Member B marks the task complete, Member A (Accountable) might be notified for review, and Team Lead D (Informed) is notified of completion. 