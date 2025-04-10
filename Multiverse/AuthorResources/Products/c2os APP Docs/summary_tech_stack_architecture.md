# Summary: Technology Stack & Architecture

## Core Stack
*   **Frontend (Web):** Next.js (React) - App Router
*   **Frontend (Mobile):** React Native with Expo
*   **Backend/API:** Next.js API Routes
*   **Database:** PostgreSQL (via Supabase)
*   **Cloud Services:** Supabase (DB, Auth, Storage), Vercel (Hosting)
*   **Language:** TypeScript
*   **Monorepo:** pnpm Workspaces
*   **CI/CD:** GitHub Actions

## Local Development Requirements
*   Node.js (Check `.nvmrc` / `package.json`)
*   pnpm
*   Git
*   Docker (for Supabase local dev stack via CLI)
*   Supabase CLI

## Monorepo Structure (High-Level)
*   `apps/web`, `apps/mobile`
*   `packages/shared-types`, `packages/utils` (etc.)
*   See `project_rules.mdc` for full structure.

## CI/CD
*   GitHub Actions deploying to Vercel based on branch (`main`->prod, `staging`->staging, `develop`->preview). See `.github/workflows/deploy.yml`. 