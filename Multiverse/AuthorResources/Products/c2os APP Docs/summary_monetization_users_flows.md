# Summary: Monetization, User Personas, and Key Flows

## Monetization Model
*   **Individual Users:** Freemium
    *   **Free:** Core TRO task management, basic projects/notes. Limited features.
    *   **Pro (Paid Subscription):** Full personal productivity suite (Advanced Goals/12WY, Trackers, Delegation, Coach Connection).
*   **Tenants (Businesses/Coaching):** Access tied to associated GoHighLevel (GHL) subscription status (managed via webhooks). Unlocks tenant features. Pricing/seats managed within GHL plan.

## User Personas
*   **Individual User (Free):** Basic personal task management.
*   **Individual User (Pro):** Full personal productivity features, can delegate, can connect to coach.
*   **Tenant Member:** Collaborates within a tenant context; personal features depend on individual plan (Free/Pro). Access based on Tenant Role.
*   **Tenant Admin:** Manages tenant users, roles, settings.
*   **Coach (User in Coaching Tenant):** Manages practice, connects with clients, views client data (permission-based), uses Coach Dashboard, potentially templates.
*   **Client (Pro User connected to Coach):** Shares data with coach, receives feedback.

## Key Interaction Flows
*   **Individual Onboarding:** Google Sign-In, TRO intro, prompt capture. Pro users see Goals/Trackers intro.
*   **Tenant Onboarding:** Admin creates Tenant (maybe via GHL), invites members, member accepts & joins with role.
*   **User-to-User Delegation:** Pro user delegates task to another user (Free/Pro), assignee notified, originator tracks status.
*   **Coach-Client Connection:** Client (Pro) requests connection, Coach accepts, permissions granted, Coach views client data & comments.
*   **Tenant Task Collaboration (RACI):** Member creates Project/Task in Tenant context, assigns RACI roles, users notified/perform actions based on role. 