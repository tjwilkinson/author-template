# Technology Stack Research: Cadence Cornerstone OS

This document outlines the technology stack used for the Cadence Cornerstone OS project, including core application technologies, cloud services, development tools, and local setup requirements.

## 1. Core Application Stack

*   **Frontend (Web):** Next.js (React framework) - Using App Router.
*   **Frontend (Mobile):** React Native with Expo.
*   **Backend/API:** Next.js API Routes (co-located with the web frontend).
*   **Database:** PostgreSQL (managed via Supabase in the cloud, local instance for development).
*   **Language:** TypeScript (used across frontend, backend, and shared packages).

## 2. Cloud Platform & Services

*   **Hosting (Web/API):** Vercel.
*   **Database & Backend Services:** Supabase
    *   Managed PostgreSQL Database
    *   Authentication (Supabase Auth - primarily Google Sign-In)
    *   Storage (Supabase Storage - likely needed later)
    *   Edge Functions (Potential future use)
*   **Version Control Hosting:** GitHub.

## 3. Development Tools & Workflow

*   **Version Control System (VCS):** Git.
*   **Monorepo Management:** pnpm Workspaces (indicated by `pnpm-workspace.yaml`).
*   **Package Manager:** pnpm.
*   **Database Migrations:** Supabase Migrations (using the Supabase CLI).
*   **Continuous Integration/Continuous Deployment (CI/CD):** GitHub Actions.
*   **Code Sharing:** Monorepo `packages/` directory (`shared-types`, potentially `utils`, `ui-components`).
*   **State Management (Web):** Context API or Zustand (to be decided/implemented).
*   **Monitoring/Logging:** Vercel Analytics, Sentry (or similar - planned).

## 4. Integrations

*   **Google Calendar API:** For two-way calendar synchronization.
*   **GoHighLevel (GHL) API:** For managing tenant subscription status via webhooks.

## 5. Local Development Requirements

*   **Node.js:** JavaScript runtime (specific version likely defined in `.nvmrc` or `package.json`).
*   **pnpm:** Package manager for managing monorepo dependencies.
*   **Git:** For version control.
*   **Docker:** Containerization platform. Used for running Supabase services locally (including PostgreSQL, Auth, Storage, etc.) via the Supabase CLI.
*   **Supabase CLI:** For managing local Supabase environment (starting/stopping services, generating migrations, deploying functions).
*   **PostgreSQL Client:** (Optional but helpful) A tool to directly interact with the local or remote PostgreSQL database (e.g., `psql`, pgAdmin, TablePlus, DBeaver).
*   **(Implicit) Operating System:** Development seems feasible on macOS (user's OS), Linux, and Windows (with appropriate setup like WSL).
*   **(Implicit) Code Editor:** Such as VS Code / Cursor.

## Summary

The project utilizes a modern TypeScript-based stack leveraging Next.js for the web frontend and API, React Native/Expo for mobile, and Supabase for backend services like database and authentication. Development workflow relies on Git/GitHub, pnpm workspaces for monorepo management, Supabase CLI for local development and migrations, and Vercel for deployment. Docker is essential for running the Supabase stack locally. 