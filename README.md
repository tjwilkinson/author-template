# Author Template

A template for authors to organize and manage writing projects with AI assistance. This repository is structured to allow both writing work and template improvements.

## Repository Structure

- `.cursor/` - Contains system files, templates, rules, and implementation details
- `docs/` - Documentation, guides, and writing templates

## Branches

- `main` - The clean template branch, used as a starting point for new projects
- `writing-project` - Your active writing work branch

## Working with this Repository

### For Writing

1. Work in the `writing-project` branch for all your writing
2. All changes to content folders (Series, Manuscript, etc.) will be tracked here
3. This branch won't be merged back into main

### For Template Improvements

When you find improvements that should be made to the template itself:

1. Run the template mode script: `./template-mode.sh on`
2. Make your changes to template files (in .cursor/, docs/, etc.)
3. Commit your changes
4. Push only these template changes to main: `git push origin HEAD:main`
5. Switch back to writing mode: `./template-mode.sh off`

This way, your writing content stays in the writing branch, while template improvements can be pushed to the main branch.

## Template Mode Script

The `template-mode.sh` script helps you switch between writing mode and template update mode:

- `./template-mode.sh on` - Switch to template mode (content changes ignored)
- `./template-mode.sh off` - Switch back to writing mode (all changes tracked)

When in template mode, only changes to template files will be tracked, making it easy to selectively push template improvements without including your writing content. 