# Database Design Notes

This document provides rationale and commentary on key database design decisions outlined in `plan.md`, particularly focusing on the hybrid user/tenant model.

## 1. Hybrid Implementation Approach (Design Globally, Implement Locally)

*   **Rationale:** The core challenge is supporting both purely personal use and tenant-based collaboration seamlessly. Designing the full schema upfront, including tenant relationships, prevents major, costly refactoring later when adding multi-tenancy. However, implementing only the necessary tables/fields for the current phase (MVP first) keeps development focused and reduces initial complexity.
*   **Key Fields for Hybrid Support:**
    *   `context_tenant_id` (Nullable, Foreign Key to `tenants`): Added to core data tables like `projects`, `tasks`, `goals`, `notes_resources`. If NULL, the item is personal. If NOT NULL, it belongs to the specified tenant.
    *   `scope` (e.g., ENUM('personal', 'company')): Used on items within a tenant context (`context_tenant_id` is NOT NULL) to differentiate between items intended only for the user within that tenant vs. items shared with the company/team.
    *   `created_by_user_id` (Foreign Key to `users`): Tracks the original creator, essential for ownership and potentially permissions.
*   **Implementation:** In early phases (MVP), `context_tenant_id` will always be NULL, and `scope` might default to 'personal' or be ignored. Queries will primarily filter `WHERE context_tenant_id IS NULL`. Later phases activate logic using these fields.

## 2. Core Tables Rationale

*   **`users`:** Global user store. Contains authentication info (`google_id`) and the user's *individual* plan type (`plan_type` - 'Free', 'IndividualPro'). This determines their access to personal features like delegation and advanced goal setting, *independent* of tenant membership.
*   **`tenants`:** Stores organizational details, including `ghl_identifier` for subscription linking and `tenant_type` ('Business', 'Coaching') which might gate specific features (like the Coach Dashboard).
*   **`tenant_memberships`:** The crucial link table. Connects `users` to `tenants`. Critically, this table also stores the user's `role_id` *within that specific tenant*. This replaces a separate `user_roles` table, simplifying the structure as roles are always tenant-specific.
*   **`roles` & `permissions` & `role_permissions`:** Standard RBAC implementation. `roles` are defined *per tenant* (allowing tenant admins to create custom roles). `permissions` are system-defined actions. `role_permissions` links them.

## 3. Feature-Specific Table Notes

*   **`task_delegations`:** Manages user-to-user delegation. Needs `task_id`, `delegator_user_id`, `assignee_user_id`, `status`, potentially `permissions_granted` (e.g., 'view_only', 'can_complete'). Independent of tenants initially, allowing Pro users to delegate to any other user.
*   **`coach_client_links`:** Manages the specific connection between a Coach (User in a Coaching Tenant) and a Client (Individual Pro User). Needs `coach_user_id`, `client_user_id`, `status` ('pending', 'active', 'inactive'), and importantly, `permissions_granted` (detailing what data the coach can see - e.g., 'view_goals', 'view_tasks', 'view_trackers').
*   **RACI Tables (`project_raci_assignments`, `task_raci_assignments`):** Link `users` (or potentially `teams`) to tenant-scoped `projects`/`tasks` with a specific `raci_role` ('Responsible', 'Accountable', etc.). Only relevant when `context_tenant_id` is not NULL.

## 4. Indexing Strategy (Initial)

*   Index `context_tenant_id` on all relevant tables for efficient filtering between personal and tenant data.
*   Index `created_by_user_id` for queries related to user-specific data.
*   Index foreign keys (`project_id` on `tasks`, `goal_id` on `tactics`, etc.).
*   Index fields commonly used in filters (e.g., `status` on `tasks`, `due_date` on `tasks`).
*   Re-evaluate indexing strategy as query patterns evolve and tenant features are implemented. 