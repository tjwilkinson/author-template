# Project Plan: `Cadence Cornerstone OS` Cloud & Mobile App

*Version: Reflecting Hybrid User/Tenant Model & Feature Expansion*

## 1. Project Vision & Methodology

**Vision:** To create a comprehensive cloud and mobile application for personal and business productivity, integrating goal achievement, task management, habit formation, and knowledge management. **`Cadence Cornerstone OS`** (the Application) will empower individual users, facilitate team collaboration within organizations, and serve as a powerful platform for coaches to manage and guide their clients, with full white-labeling capabilities.

**Methodology (Integrated):** This application implements the **`ASCEND Method`**, a unique operational system synthesizing principles from:

*   **Total Relaxed Organization (TRO):** Provides the core daily workflow for capture, triage, processing, review, and execution (part of Structure, Commit, Evaluate).
*   **Tony Robbins (RPM):** Structures goal setting around Results, Purpose, and MAP (part of Align, Structure).
*   **Darren Hardy (Compound Effect):** Emphasizes consistent small actions and tracking (part of Commit, Nurture, Evaluate).
*   **The 12 Week Year (12WY):** Implements a high-urgency execution framework with cycles, tactics, and scoring (part of Align, Structure, Commit, Evaluate).
*   **RACI:** Incorporates principles for defining team roles (relevant for collaboration features within Structure/Commit).
*   **(Underlying Philosophy):** Supports the journey towards the **AI³ Framework's** "Autonomous Identity" by facilitating "Automate Action" and reinforcing "Inspired Integrity" through the Align stage.

## 2. Core Features

*   **Hybrid User Model:** Supports Individual Users (Free/Pro plans) and Tenant Members (invited into Organizations/Coaching practices). Users can exist independently and/or belong to tenants.
*   **Multi-Tenant Architecture:** Securely isolates data *within* specific tenant contexts, while allowing user-level data and controlled sharing/delegation/connections between users/tenants.
*   **White-Labeling:** Allows tenants (e.g., coaching clients, businesses) to customize branding (logo, colors, app name) for their members.
*   **Google Sign-In:** Primary authentication method for all users.
*   **Role-Based Access Control (RBAC):**
    *   Standard Tenant Admin/User roles.
    *   Tenant Admins can create custom roles with granular permissions within their tenant.
    *   Permissions control access to features and data within personal and tenant contexts.
*   **Goal Management (RPM & 12WY):**
    *   Define long-term Visions/Purpose (Personal or Company scope).
    *   Structure work in 12-Week Cycles.
    *   Define measurable 12-Week Goals (Results - Personal or Company scope).
    *   Plan specific Weekly Tactics required for goals.
*   **Task Management (TRO):**
    *   Full task lifecycle (Inbox, Triage, Processed, WaitingFor, Done, SomedayMaybe).
    *   Quick Capture (Mobile, Web, Email Forwarding - future).
    *   Processing includes Next Actions, Contexts, Do Dates, Due Dates.
    *   Project linking.
    *   Flexible Recurring Task options.
*   **Project Management:** Define multi-step projects (Personal or Company scope) linked to goals.
*   **Team Collaboration:**
    *   Define Teams within a tenant.
    *   Assign RACI roles to Users or Teams for Projects/Tasks within a tenant context.
    *   Visibility of linked Notes/Resources controlled by RACI assignments.
    *   Company-scoped Goals/Projects visible within the tenant.
    *   (Optional) Shared Contexts/Tags at tenant level.
    *   (Optional) @Mentions in comments.
*   **User-to-User Delegation:** Individual users (paid plan) can delegate specific tasks to *any* other user (including free users), managing status and access level.
*   **Coach-Client Connection:**
    *   Individual users (paid plan) can securely connect with a Coach (user within a 'Coaching' type tenant).
    *   Grants the Coach permission-based visibility into the client's personal goals, tasks, trackers, and reviews.
    *   In-app commenting/feedback mechanisms between coach and client (on goals, reviews, etc.).
*   **Coaching Platform Features:**
    *   Coach Dashboard: Overview of connected clients' progress and engagement metrics.
    *   Templating Engine: Coaches create reusable templates for Goals, Projects, Trackers.
*   **Knowledge Management:**
    *   Capture Notes/Resources (Personal or Tenant scope).
    *   Link Notes/Resources to Tasks/Projects/Goals.
    *   (Advanced) Bi-Directional Linking (`[[links]]`) between items.
*   **Custom Trackers (Compound Effect):** Define and track custom metrics (numeric, yes/no, scale) with visualization (charts, streaks). Link trackers to goals.
*   **Weekly Planning & Review (12WY):** Guided routines to plan the week based on Tactics, review progress, and calculate a Weekly Execution Score. Option to submit reviews to a connected coach.
*   **Google Calendar Integration:** Two-way sync for time blocking and viewing scheduled tasks/events.
*   **GoHighLevel Integration:** Tenant subscription status managed in GHL, automatically activating/deactivating tenant features/access in the app via webhooks.
*   **Dashboard:** Personalized overview (Cycle progress, execution score, upcoming items, tracker summary).
*   **Guided Onboarding:** Help users understand the methodology and app features.
*   **Mobile App:** Optimized for quick capture and core workflows.

## 3. Architecture Overview

*   **Backend:** (Suggest Technology - e.g., Node.js/Python/Go, PostgreSQL/MySQL database)
*   **Frontend:** (Suggest Technology - e.g., React/Vue/Angular for Web, React Native/Flutter for Mobile)
*   **Cloud Platform:** (e.g., AWS, GCP, Azure)
*   **Key Patterns:** Multi-tenancy support with user-centric data model, RBAC, Secure OAuth handling (Google Sign-In, Google Calendar), Webhook processing (GHL), API-driven design.

## 4. Database Schema Concept

The database structure evolves to support the hybrid model:

*   `tenants`: Stores organization details, white-label settings, `ghl_identifier`, `tenant_type` ('Business', 'Coaching'), `owner_user_id`.
*   `users`: Stores global user details, `google_id`, `plan_type` ('Free', 'IndividualPro', etc.).
*   `tenant_memberships`: Links users to tenants, defines user's role *within that tenant*.
*   `permissions`: System-defined actions.
*   `roles`: Tenant-specific roles (standard and custom).
*   `role_permissions`: Links permissions to roles per tenant.
*   `user_roles` (Replaced by `tenant_memberships` which includes role).
*   `visions`, `twelve_week_cycles`, `twelve_week_goals`, `weekly_tactics`, `projects`, `tasks`, `notes_resources`: Include `created_by_user_id` and `context_tenant_id` (nullable, indicates if item belongs to a tenant or is personal), `scope` ('personal', 'company').
*   `contexts`: User-defined contexts.
*   `task_contexts`: Links tasks to contexts.
*   `project_raci_assignments`, `task_raci_assignments`: Link users/teams to tenant-context items with RACI roles.
*   `teams`, `team_memberships`: (If implementing team assignments).
*   `task_delegations`: Manages user-to-user task assignment.
*   `coach_client_links`: Manages connections between coaches and clients, defining permissions.
*   `trackers`, `tracker_entries`: User-scoped custom tracking.
*   `weekly_reviews`: User-scoped, potentially visible to connected coach.
*   `(Potentially others: invitations, templates, comments, etc.)`

## 5. Implementation Checklist (MVP-First Approach)

### PHASE 1: FOUNDATION & INFRASTRUCTURE (Estimated Duration: 1-2 Weeks)
*Core system setup, Git, environments, basic cloud config, and initial schema design - required for all subsequent phases*

**Technical Foundation:**
*   [x] Select and finalize technology stack (Confirming: Next.js for Web/API, React Native/Expo for Mobile, Supabase for DB/Auth, Vercel for hosting)
*   [x] **Project Structure:** Create monorepo directory structure (`apps/web`, `apps/mobile`, `packages/shared-types`, `docs/`, `.github/workflows`, etc.) as per `project_rules.mdc`. (`apps/`, `packages/`, `.github/`, `docs/`, `tsconfig.base.json`)
*   [x] **Version Control:** Initialize Git repository locally and push initial structure to GitHub. (`.git/`, https://github.com/tjwilkinson/c2os)
*   [x] **Version Control:** Create `main`, `staging`, and `develop` branches. (branches pushed to GitHub)
*   [ ] **Version Control:** Set up branch protection rules for `main` and `staging` on GitHub. *(Note: Branch protection requires GitHub Pro for private repos. Consider repository workflows without technical branch protection for now.)*
*   [x] **Version Control:** Create `.gitignore` (include `.env*`, `node_modules/`, build outputs, OS files). (`.gitignore`)
*   [x] **Dependencies:** Initialize root `package.json` for workspace management (e.g., pnpm/yarn/npm). (`package.json`, `pnpm-workspace.yaml`)
*   [x] **Dependencies:** Initialize `package.json` for `apps/web` (Next.js). (`apps/web/package.json`, `apps/web/tsconfig.json`)
*   [x] **Dependencies:** Initialize `package.json` for `apps/mobile` (Expo/React Native). (`apps/mobile/package.json`)
*   [x] **Dependencies:** Initialize `package.json` for `packages/shared-types`. (`packages/shared-types/package.json`, `packages/shared-types/tsconfig.json`)
*   [x] **Cloud:** Set up Supabase project. (Project ID: `jqoqpnkndjisihlkqjrx`)
*   [x] **Cloud:** Set up Vercel project. (Linked to `claarityconsultants/c2os`)
*   [x] **Cloud:** Establish basic Vercel deployment configuration linking branches (main->prod, staging->staging, develop->dev previews).
*   [x] **CI/CD:** Create basic GitHub Actions workflow placeholders in `.github/workflows/` (e.g., lint, build, test placeholders).
*   [x] **Environment:** Create `.env.example` with placeholders for all required variables (Supabase, GHL, Google, Local DB) as per `project_rules.mdc`. (`.env.example`)
*   [x] **Environment:** Create local `.env` file (ensure it's gitignored). (`.env` created with initial Supabase keys)
*   [x] **Environment:** Implement secrets management strategy (e.g., Vercel env variables, Supabase Vault if applicable). (Added Supabase keys to Vercel envs: Prod, Preview, Dev)
*   [ ] Set up basic monitoring, logging, and error tracking (e.g., Vercel Analytics, Sentry/equivalent placeholder).

**Database Architecture (Design with End in Mind):**
*   [x] **Local DB:** Set up local PostgreSQL instance. (via Homebrew `postgresql@14` service)
*   [x] **Migration Tool:** Choose and initialize a migration tool (e.g., Prisma Migrate, Supabase migrations). (Supabase Migrations initialized, configured for local Homebrew PG in `supabase/config.toml`)
*   [x] **Schema Design (Core):** Design initial ERD focusing on core entities: Users, Tenants, TenantMemberships, Roles, Permissions (considering hybrid user/tenant model from the start). (Defined in initial migration)
*   [x] **Schema Design (Core):** Define these core tables with necessary relationships, ensuring multi-tenant capabilities (`context_tenant_id`, `scope`, etc. where appropriate). (Defined in initial migration)
*   [x] **Schema Design (Docs):** Document schema decisions and initial ERD. (In `docs/api-structure.md`)
*   [x] **Initial Schema (Core):** Create initial migration files for these core tables using the chosen migration tool. (`supabase/migrations/20250405033910_initial_schema.sql`)
*   [ ] **Schema Design (Inbox - Phase 2):** Design schema for `inbox` table (capture source, content, processed status).
*   [ ] **Schema Design (Notes - Phase 2):** Design schema for `notes` table (content, links, source).
*   [ ] **Schema Design (Projects - Phase 2):** Design schema for `projects` table (goal link, status, etc.).
*   [ ] **Schema Design (Contexts - Phase 2):** Design schema for `contexts` table (`id`, `name`, `user_id` nullable FK, `context_tenant_id` nullable FK) and `task_contexts` linking table.
*   [ ] **Schema Design (Future):** Consider placeholders/ideas for `tags`, `areas` (e.g., for PARA) tables and their linking tables.

**Core System Architecture:**
*   [x] **Database Implementation:** Apply initial schema migration to local DB. (Applied via `supabase start` to local Docker DB)
*   [x] **Authentication:** Configure Supabase Auth (Google Sign-In primary, possibly email/password fallback). (Google Provider enabled in Supabase dashboard, credentials added to Vercel envs & local `.env` needed)
*   [x] **Authentication:** Implement basic Google Sign-In flow in the Next.js app shell. (`AuthButton.tsx`, `/api/auth/callback`, `page.tsx`)
*   [x] **Authentication:** Set up basic user session management (e.g., using Supabase Auth helpers in Next.js). (`@supabase/ssr` clients, `middleware.ts`)
*   [x] **API:** Set up basic Next.js API route structure in `apps/web` (e.g., `/api/auth`, `/api/webhooks`). Define initial API versioning strategy (e.g., `/api/v1/...`).
*   [x] **Frontend Shell:** Create basic Next.js app structure (`/app` router recommended). (Done via `create-next-app`)
*   [x] **Frontend Shell:** Set up basic routing and minimal state management (e.g., Context API or Zustand).
*   [ ] **Mobile Shell:** Create basic Expo app structure.
*   [ ] **White-Labeling:** Implement placeholder/basic mechanism concept (e.g., reading config based on hostname/tenant).
*   [x] **GHL:** Define structure/placeholders for GHL webhook handling API endpoint (e.g., `/api/webhooks/ghl`).

**Milestone:** Foundational code structure exists in Git, local dev environment runnable, basic auth connects to Supabase, initial DB schema designed and migration created.

**Running the Local Environment:**
1. Start Supabase services: `npx supabase start`
2. Apply migrations (if needed): `npx supabase db push` (for local changes) or `npx supabase migration up` (for new migrations)
3. Start the web server (from `apps/web` directory): `npm run dev`

### PHASE 2: PERSONAL PRODUCTIVITY MVP (Backend Focus - Estimated Duration: 3-4 Weeks)
*Implement DB models & APIs for *user-scoped* items (visions, goals, tasks, etc.), core TRO logic.*

**Database Implementation (Personal Scope):**
*   [ ] **Schema (Inbox):** Implement `inbox` table schema & migration.
*   [ ] **Schema (Notes):** Implement `notes` table schema & migration (include linking fields like `task_id`, `project_id`, `source_inbox_id`).
    *   *Future Requirement (Phase 7):* Add `google_calendar_event_id` (TEXT), `meeting_start_time` (TIMESTAMPTZ), `meeting_end_time` (TIMESTAMPTZ), `attendee_emails` (TEXT[]). Consider `note_attendees` linking table (`note_id`, `user_id`).
*   [ ] **Schema (Projects):** Implement `projects` table schema & migration.
*   [x] **Schema (Tasks - Initial):** Implement database schema & migrations for `tasks`. (`supabase/migrations/20250405125315_create_tasks_table.sql`)
*   [x] **Schema (Tasks - Enhancements):** Implement migration to add new columns: `project_id`, `recurring_rule`, `completed_at`, `do_date`, `follow_up_date`, `waiting_on_details`, `context_tenant_id`, `scope`. (`supabase/migrations/20250405233121_add_task_enhancements.sql`)
    *   *Future Requirement (Phase 7):* Add `source_note_id` (UUID, nullable, FK to `notes.id`) to link tasks created from meeting notes.
*   [x] **Schema (Contexts):** Implement `contexts` and `task_contexts` tables schema & migration. (`supabase/migrations/20250405235843_create_contexts_schema.sql`)
*   [ ] **Schema (Other Personal):** Implement database schema & migrations for personal scope: ~~Visions, Cycles, Goals, Tactics,~~ Trackers. Ensure `created_by_user_id` and nullable `context_tenant_id` are present. - *Goal tables done.*
*   **Database Schema (Core Personal):**
    *   [x] Define initial schema for `users` (implicit via Supabase Auth). (`supabase/migrations/..._init.sql`)
    *   [x] Define schema & enhancements for `tasks` table (add `project_id`, `recurring_rule`, `completed_at`, `do_date`, `follow_up_date`, `waiting_on_details`, remove `context` text field). (`supabase/migrations/20250405233121_add_task_enhancements.sql`)
    *   [x] Define schema for `contexts` (for GTD-style contexts like `@home`) and `task_contexts` linking table. (`supabase/migrations/20250405235843_create_contexts_schema.sql`)
    *   [x] Define schema for `projects` table. (`supabase/migrations/20250406122908_create_projects_areas_schema.sql`)
    *   [x] Define schema for `areas` table. (`supabase/migrations/20250406122908_create_projects_areas_schema.sql`)
    *   [x] Define schema for `notes` table. (`supabase/migrations/20250406124045_create_notes_schema.sql`)
    *   [x] Define schema for `tags` table and linking tables (`task_tags`, `note_tags`, `project_tags`). (`supabase/migrations/20250406124410_create_tags_schema.sql`)
    *   [x] Define schema for `task_notes` linking table: Add a many-to-many linking table (`task_notes`) to allow direct association between any task and any note, supplementing the project/area links on the notes themselves. (`supabase/migrations/20250406133220_create_task_notes_schema.sql`)
    *   [x] Define schema for goal-tracking tables (`visions`, `twelve_week_cycles`, `twelve_week_goals`, `weekly_tactics`). (`supabase/migrations/20250406144500_create_goal_setting_schema.sql` - *Assuming this was the migration name*)

**Core Workflow Backend:**
*   [ ] **Capture:** Implement basic mechanism to add items to the `inbox` (e.g., API endpoint for manual entry).
*   [ ] **Triage Logic:** Implement API endpoints or server actions for Triage decisions (Create Task/Note/Project, Trash, Delegate, Someday) originating from the `inbox`.
    *   Ensure links (`source_inbox_id`) are created.
    *   Ensure inbox item is marked processed (or deleted).
*   [ ] **Processing Logic:** Implement API endpoints or server actions for updating tasks initially created with `status=\'inbox\'` (setting context, dates, project, changing status).

**Task Management APIs:**
*   [x] Implement REST API endpoints (CRUD) for Tasks (`apps/web/src/app/api/v1/tasks/route.ts`, `apps/web/src/app/api/v1/tasks/[taskId]/route.ts`) - *Note: Core CRUD exists, but specific TRO workflow logic (Triage/Process actions) is not implemented as dedicated endpoints.*
*   [x] Update Task API endpoints to handle new fields (`project_id`, dates, `waiting_on_details`, etc.) and **linking/unlinking contexts via `task_contexts` table**.
*   [ ] Implement API logic for recurring task generation (if applicable in backend).
*   [ ] Implement API logic for task filtering based on new fields/**contexts**.
*   [ ] **API Documentation:** Set up and maintain OpenAPI/Swagger documentation for Next.js API routes (Method TBD).

**Projects, Notes, Areas, Contexts, Tags, Goals APIs:**
*   [x] Implement REST API endpoints (CRUD) for Projects. (`apps/web/src/app/api/v1/projects/route.ts`, `apps/web/src/app/api/v1/projects/[projectId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Notes. (`apps/web/src/app/api/v1/notes/route.ts`, `apps/web/src/app/api/v1/notes/[noteId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Areas. (`apps/web/src/app/api/v1/areas/route.ts`, `apps/web/src/app/api/v1/areas/[areaId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Contexts (per user/tenant). (`apps/web/src/app/api/v1/contexts/route.ts`, `apps/web/src/app/api/v1/contexts/[contextId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Tags. (`apps/web/src/app/api/v1/tags/route.ts`, `apps/web/src/app/api/v1/tags/[tagId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Visions. (`apps/web/src/app/api/v1/visions/route.ts`, `apps/web/src/app/api/v1/visions/[visionId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for 12-Week Cycles. (`apps/web/src/app/api/v1/cycles/route.ts`, `apps/web/src/app/api/v1/cycles/[cycleId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for 12-Week Goals. (`apps/web/src/app/api/v1/goals/route.ts`, `apps/web/src/app/api/v1/goals/[goalId]/route.ts`)
*   [x] Implement REST API endpoints (CRUD) for Weekly Tactics. (`apps/web/src/app/api/v1/tactics/route.ts`, `apps/web/src/app/api/v1/tactics/[tacticId]/route.ts`)
*   [ ] Implement API logic for linking Notes to Tasks/Projects.

**Validation Point:** API endpoints exist and function correctly for creating/updating/linking Inbox items, Tasks, Notes, Projects based on the triage/process workflow. *(Note: Core CRUD exists, but specific Triage/Process flow logic is not yet implemented on backend.)*

### PHASE 3: PERSONAL PRODUCTIVITY MVP (Frontend Focus - Estimated Duration: 4-6 Weeks)
*Build the UI for personal capture, triage, processing, task/project/notes management, goal planning, trackers, weekly routines.*

**Core Workflow Frontend:**
*   [ ] **Inbox Triage UI:** Build UI view to display unprocessed `inbox` items.
*   [ ] **Triage Actions UI:** Implement UI elements (buttons, forms) to trigger Triage API actions (Make Task/Note/Project, Trash, Delegate, Someday).
*   [ ] **Process Tasks UI:** Build UI view/filter to display `tasks` with `status='inbox'`. Implement UI elements to trigger Processing API actions (update task details, change status).
*   [ ] **Quick Capture UI:** Implement a simple UI element (e.g., header input) to quickly add items to the `inbox`.

**Task Management UI:**
*   [x] Create intuitive task list/board UI for desktop (`apps/web/src/app/_components/tasks/TaskList.tsx`, `apps/web/src/app/_components/tasks/TaskItem.tsx`, `apps/web/src/app/tasks/page.tsx`).
*   [x] Implement Task creation/editing modal (`apps/web/src/app/_components/tasks/TaskModal.tsx`).
*   [x] Implement context selection/management in `TaskModal`.
*   [~] Update `TaskItem` UI to display related contexts and new task fields (do_date, follow_up_date, waiting_on_details). *(Contexts displayed, other fields pending)*.
*   [~] Implement UI for filtering tasks by status, **context**, project, dates. *(Status/Date basic filtering exists; Context/Project filtering missing)*.
*   [ ] Implement UI for managing recurring tasks.
*   [ ] Fix `TaskList handleSaveTask` to send all fields (incl. new fields & relations like context_ids, tag_ids, note_ids) from `TaskModal` to API.
*   [ ] Implement Task UI for mobile.

**Notes UI:**
*   [x] Implement basic Note list/grid view. (`apps/web/src/app/_components/notes/NoteList.tsx`, `apps/web/src/app/notes/page.tsx`)
*   [x] Implement Note viewing/editing UI (consider basic Markdown support). (`apps/web/src/app/_components/notes/NoteModal.tsx`)
*   [ ] Implement UI for linking Notes to Tasks/Projects.

**Projects, Areas, Contexts, Tags UI:** *(Assuming basic CRUD UIs exist)*
*   [x] Implement basic List/Modal UI for Projects. (`apps/web/src/app/_components/projects/ProjectList.tsx`, `apps/web/src/app/_components/projects/ProjectModal.tsx`, `apps/web/src/app/projects/page.tsx`)
*   [x] Implement basic List/Modal UI for Areas. (`apps/web/src/app/_components/areas/AreaList.tsx`, `apps/web/src/app/_components/areas/AreaModal.tsx`, `apps/web/src/app/areas/page.tsx`)
*   [x] Implement basic List/Modal UI for Contexts. (`apps/web/src/app/_components/contexts/ContextList.tsx`, `apps/web/src/app/_components/contexts/ContextModal.tsx`, `apps/web/src/app/contexts/page.tsx`)
*   [x] Implement basic List/Modal UI for Tags. (`apps/web/src/app/_components/tags/TagList.tsx`, `apps/web/src/app/_components/tags/TagModal.tsx`, `apps/web/src/app/tags/page.tsx`)

**Goal Setting UI:**
*   [x] Create List UI for Visions (`apps/web/src/app/_components/visions/VisionList.tsx`, `apps/web/src/app/visions/page.tsx`).
*   [x] Implement Vision creation/editing modal (`apps/web/src/app/_components/visions/VisionModal.tsx`).
*   [x] Create List UI for Cycles (`apps/web/src/app/_components/cycles/CycleList.tsx`, `apps/web/src/app/cycles/page.tsx`).
*   [x] Implement Cycle creation/editing modal (`apps/web/src/app/_components/cycles/CycleModal.tsx`).
*   [x] Create List UI for Goals (`apps/web/src/app/_components/goals/GoalList.tsx`, `apps/web/src/app/goals/page.tsx`).
*   [x] Implement Goal creation/editing modal (`apps/web/src/app/_components/goals/GoalModal.tsx`).
*   [x] Create List UI for Tactics (`apps/web/src/app/_components/tactics/TacticList.tsx`, `apps/web/src/app/tactics/page.tsx`).
*   [x] Implement Tactic creation/editing modal (`apps/web/src/app/_components/tactics/TacticModal.tsx`).
*   [x] Implement basic navigation between Visions -> Cycles -> Goals -> Tactics. (`apps/web/src/app/_components/visions/VisionList.tsx`, `apps/web/src/app/_components/cycles/CycleList.tsx`, `apps/web/src/app/_components/goals/GoalList.tsx`).

**Dashboard UI:**
*   [x] Implement basic dashboard layout. (`apps/web/src/app/dashboard/page.tsx`)
*   [~] Display count of tasks due today. *(Needs re-verification)* (`apps/web/src/app/dashboard/page.tsx`)
*   [ ] Enhance dashboard with other summaries (Inbox count, Tasks to Process count, Next Actions count, Overdue count, Project/Goal counts).

**Milestone:** Core personal productivity features are usable via the web interface. Triage and Processing workflows are functional. *(Note: Basic CRUD UIs exist, but core Triage/Processing workflow UI and full Task editing integration need completion.)*

**Refinement:**
*   [ ] Review and remove temporary `console.log` statements added for debugging purposes during Phase 3.

**Note Integration in Task View:**
*   Display related notes: Query and show notes linked directly via `task_notes` AND notes linked to the task's `project_id` (potentially distinct UI).
*   Add new note: Button to create a new note; automatically create a `task_notes` link. If task has a project, pre-fill `notes.project_id`.
*   Attach existing note: UI to search/select existing notes and create a `task_notes` link.

### PHASE 4: TENANT & TEAM FOUNDATIONS (5 Weeks)
*Expands from personal-only to multi-tenant capability*

**Multi-Tenant Infrastructure:**
- [ ] Enhance database schema for tenant contexts
- [ ] Implement tenant creation and management
- [ ] Create tenant-user membership system
- [ ] Build context-switching UI between personal and tenant spaces
- [ ] Implement tenant data isolation security

**Role-Based Access Control:**
- [ ] Design and implement permissions system
- [ ] Create standard and custom roles
- [ ] Build role assignment mechanisms
- [ ] Implement permission checks throughout the application
- [ ] Create tenant admin role with management capabilities

**Tenant Administration:**
- [ ] Implement user invitation system
- [ ] Build tenant user management interface
- [ ] Create white-label configuration UI
- [ ] Implement tenant settings management

**Milestone:** Working multi-tenant system with basic organizational features

### PHASE 5: COLLABORATION FEATURES (To Do)
*Adds team collaboration capabilities within tenant contexts*

**Shared Items:**
- [ ] Enable company-scoped goals, projects, and resources
- [ ] Implement shared visibility rules
- [ ] Build UI for company vs. personal items
- [ ] Create team creation and management

**RACI Implementation:**
- [ ] Design and implement RACI assignment system
- [ ] Build UI for assigning RACI roles
- [ ] Create visibility rules based on RACI assignments
- [ ] Implement RACI-based notifications

**Team Workflows:**
- [ ] Build team dashboards
- [ ] Implement @mentions in comments
- [ ] Create shared contexts/tags at tenant level
- [ ] Develop team progress tracking

**Validation Point:** Limited tenant pilot with selected partner organizations

**Milestone:** Functional team collaboration system within tenant contexts

### PHASE 6: DELEGATION & COACHING FEATURES (To Do)
*Implements connection and visibility between individual users and introduces templating*

**User-to-User Delegation:**
- [ ] Design and implement delegation data model
- [ ] Build delegation request/accept workflow
- [ ] Create delegated task management interface
- [ ] Implement notification system for delegation events
- [ ] Develop delegation tracking and reporting

**Coach-Client Connections:**
- [ ] Implement connection request/management system
- [ ] Build permission-based visibility controls
- [ ] Create coaching dashboard with client overview
- [ ] Implement in-app commenting/feedback system
- [ ] Build client progress tracking features

**Templating Engine:**
- [ ] Design and implement core database schema for templates (Goals, Projects, Tasks, Trackers, Routines)
- [ ] Build backend API for creating, reading, updating, and deleting templates
- [ ] Develop UI for coaches/admins to manage templates
- [ ] Implement mechanism for users/coaches to apply templates to their own or clients' accounts
- [ ] Build initial template library functionality
- [ ] **Example Use Case:** Support creation of custom mindset routines (visualizations, journaling) and specific programs like C² (Cashflow Cadence) as templates.

**Milestone:** Complete coaching platform and delegation system
**Official Launch:** Full product with personal and organizational features

### PHASE 7: INTEGRATIONS & ADVANCED FEATURES (To Do)
*   Goal: Implement full Google Calendar sync, GHL activation logic, bi-directional linking, advanced search, enhanced mobile experience.
*   [ ] **Google Calendar Integration:** Implement sync for time blocking and meeting notes.
    *   [ ] Request necessary Google Calendar API scopes (read initially, write for bidirectional).
    *   [ ] Implement OAuth flow for Google Calendar.
    *   [ ] Create UI view to display calendar events.
    *   [ ] **Meeting Notes Feature:**
        *   [ ] Use "Meeting" tag on `notes` table to identify meeting notes.
        *   [ ] Link `notes`