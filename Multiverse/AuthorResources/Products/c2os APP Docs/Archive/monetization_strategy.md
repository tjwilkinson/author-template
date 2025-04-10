# Monetization Strategy Notes

This document outlines the initial concepts for the monetization strategy of [App Name], covering both individual users and tenants.

## 1. Individual User Plans

A freemium model is proposed for individual users:

*   **Free Plan:**
    *   **Goal:** Allow users to experience the core TRO task management workflow and basic features.
    *   **Features:** Core Task Management (Inbox, Processing, Contexts, Lists), Basic Project Management (potentially limited number), Personal Notes/Resources.
    *   **Purpose:** Attract a wide user base, allow basic personal organization, serve as an entry point to paid features.
    *   **Potential Limitations:** Number of active projects, advanced recurring tasks, no access to Goal Setting (RPM/12WY), Trackers, Weekly Reviews, Delegation, Coach Connection.
*   **Pro Plan (Paid Subscription - e.g., Monthly/Annual):**
    *   **Goal:** Provide the full suite of integrated personal productivity methodologies and advanced features.
    *   **Features:** All Free features + Unlimited Projects, Advanced Goal Setting (Visions, 12WY Cycles/Goals/Tactics), Custom Trackers & Visualization, Weekly Planning & Review + Execution Score, User-to-User Task Delegation, Ability to Connect with a Coach.
    *   **Target Audience:** Individuals serious about improving productivity, goal achievement, and potentially seeking coaching.

## 2. Tenant Plans (Businesses / Coaching Practices)

*   **Model:** Primarily driven by integration with GoHighLevel (GHL). Access to tenant features is tied to an active GHL subscription associated with the tenant.
*   **Activation/Deactivation:**
    *   When a GHL subscription (for a specific plan/tag indicating access to [App Name]) becomes active, a webhook triggers the activation of the corresponding Tenant in [App Name].
    *   If the GHL subscription becomes inactive (cancelled, paused), a webhook triggers the deactivation or restriction of the Tenant features in [App Name].
*   **Features Unlocked by Tenant Activation:**
    *   Ability to invite Tenant Members.
    *   Access to Tenant-scoped items (Projects, Goals, Tasks, Notes).
    *   Team Collaboration features (Teams, RACI assignments).
    *   Tenant Administration (User Management, Role Management, White-Labeling).
    *   (For Coaching Tenants) Coaching Dashboard, Templating Engine.
*   **User Seats/Pricing within GHL:** The pricing structure (e.g., per seat, flat fee) would likely be managed within the GHL subscription plan itself. [App Name] simply enables/disables the tenant based on the GHL status signal.
*   **White-Labeling:** Might be a standard feature for all active tenants or potentially tied to a specific GHL plan tier.

## 3. Overlap and Considerations

*   **Tenant Member's Individual Plan:** A user invited into a Tenant can still have their own Individual Plan (Free or Pro). Their access to *personal* features (like personal goal setting, trackers, delegation *originating* from them) depends on their individual plan status. Their access to *tenant* features depends on their role within the active tenant.
*   **Billing:** Billing for Individual Pro plans is handled directly (e.g., via Stripe). Billing for Tenant access is handled indirectly via the GHL subscription.
*   **Future Possibility:** Direct Tenant subscriptions outside of GHL could be considered later but complicates the initial model. 