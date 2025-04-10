# Summary: Database Design Principles

## Approach
*   **Design Globally, Implement Locally:** Full schema considers multi-tenancy from start; implement tables/fields needed per phase (MVP first).
*   **Hybrid Support Fields (Core Tables like `projects`, `tasks`, `notes`):**
    *   `context_tenant_id` (UUID, Nullable FK to `tenants`): NULL for personal, NOT NULL for tenant scope.
    *   `scope` (ENUM/TEXT, e.g., 'personal', 'company'): Differentiates items within a tenant context.
    *   `created_by_user_id` (UUID, FK to `auth.users`): Tracks creator.

## Core Tables
*   **`users` (maps to `auth.users`):** Global user store, `plan_type` ('Free'/'IndividualPro') for personal feature access.
*   **`tenants`:** Organizations/Practices, `ghl_identifier`, `tenant_type` ('Business'/'Coaching').
*   **`tenant_memberships`:** Links `users` to `tenants`, stores user's `role_id` *within that tenant*.
*   **`roles`:** Tenant-specific roles.
*   **`permissions`:** System-defined actions.
*   **`role_permissions`:** Links roles to permissions.

## Key Feature Table Notes (Future Phases)
*   **`task_delegations`:** User-to-user delegation (`delegator_user_id`, `assignee_user_id`, `status`). Independent of tenants initially for Pro users.
*   **`coach_client_links`:** Connects Coach (in Coaching Tenant) to Client (Pro User), `permissions_granted`.
*   **RACI Tables (`project_raci_assignments`, `task_raci_assignments`):** Link users/teams to tenant-scoped items with `raci_role`.

## Initial Indexing Strategy
*   Index `context_tenant_id`, `created_by_user_id`, foreign keys, common filter fields (`status`, `due_date`). Re-evaluate later. 