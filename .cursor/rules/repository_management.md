# Repository Management Rules

This rule file defines when and how to use the repository management scripts within this project. These scripts help maintain separation between template structure and writing content.

## Content Organization

**CRITICAL RULE: The `main` branch must ONLY contain template and server files.**

### Simplified Content Structure

All author content MUST be organized within a single top-level directory:

- **`Author/`** - This directory contains the entire author multiverse
  - This folder exists in the template but is ignored by default in git
  - ALL writing content must be placed inside this directory
  - The `Author/` directory serves as a clean boundary between template and content

Inside the `Author/` directory, writers can organize their multiverse:
- `Author/Series/` - Multiple books in a series
- `Author/Education/` - Related educational materials
- `Author/Shared/` - Resources shared across projects
- `Author/Meta/` - Collection-wide planning

This organization provides several benefits:
1. Clear separation between template files and writing content
2. Simplified gitignore rules (just ignore one folder)
3. Makes it obvious to users where content should go
4. Easy to maintain separation when pushing template improvements

### Branch Structure

- **Main Branch**: 
  - Reserved exclusively for template files and server implementation
  - NEVER commit writing content to the main branch
  - Only push template improvements to main

- **Writing Branches**:
  - ALL writing work must be done in separate branches
  - Each branch contains its author content within the `Author/` directory
  - A single branch can contain multiple related projects within appropriate subdirectories
  - The branch structure supports the full project organization described in the setup guide

## Core Scripts

The following scripts must be used in specific scenarios:

### 1. Template Mode Script (`template-mode.sh`)

This script toggles between writing mode and template update mode. **Always use this script when making template modifications.**

- **When to use `./template-mode.sh on`**:
  - Before making changes to any template files (in `.cursor/` or `docs/`)
  - Before improving the server implementation
  - Before updating any project structure or rule files
  - Before pushing template improvements to the main branch

- **When to use `./template-mode.sh off`**:
  - After completing template improvements
  - After pushing changes to the main branch
  - When returning to writing content

- **How to use**:
  ```bash
  # To switch to template mode (content changes ignored)
  ./template-mode.sh on
  
  # Make template improvements
  # Commit changes
  # Push to main: git push origin HEAD:main
  
  # To switch back to writing mode
  ./template-mode.sh off
  ```

### 2. GitIgnore Update Script (`update-gitignore.sh`)

This script automatically adds content directories to the appropriate ignore files. **Always run this script after creating new content directories.**

- **When to use**:
  - After the initial project setup when content folders are created
  - Whenever new top-level content directories are added within `Author/`
  - After restructuring project content organization

- **How to use**:
  ```bash
  # Scan for content directories and update gitignore files
  ./update-gitignore.sh
  ```

## Standard Operating Procedures

### For Template Improvements

1. Identify template improvement needed (structure, rules, server, etc.)
2. Run `./template-mode.sh on`
3. Make the necessary improvements to template files only
4. Commit the changes
5. Push only to main: `git push origin HEAD:main`
6. Run `./template-mode.sh off`
7. Continue with writing work

### For Project Setup

1. Guide the user through the setup process following the setup guide
2. Create the appropriate folder structure within the `Author/` directory
3. **After creating content directories, run `./update-gitignore.sh`**
4. Complete the setup process
5. Inform the user about the repository structure and available scripts

### For Writing Activities

1. Ensure template mode is off (normal writing mode)
2. Work in content directories within `Author/` as needed
3. If new top-level directories are created, run `./update-gitignore.sh`

### For Starting a New Project

1. If the user wants to start a new, separate writing project:
   - Create a new branch from main: `git checkout -b new-writing-project`
   - This ensures they start with a clean template without existing content
   - Complete the setup process for this new branch, creating content within `Author/`
   - Run `./update-gitignore.sh` after folder creation

## Error Prevention

If the user attempts to push template changes without using template mode:
1. Alert them to the potential issue
2. Recommend running `./template-mode.sh on` first
3. Explain that this prevents accidental inclusion of writing content

If the user attempts content creation while in template mode:
1. Alert them that template mode is active
2. Recommend running `./template-mode.sh off` first
3. Explain that their content changes may not be properly tracked in this mode

If the user attempts to commit writing content directly to main:
1. Immediately alert them that this violates the repository structure
2. Recommend creating or switching to a writing branch
3. Explain that main is reserved exclusively for template files

If the user attempts to create content outside the `Author/` directory:
1. Alert them that all content must be placed inside the `Author/` directory
2. Explain the benefits of this organization
3. Offer to help them move the content to the correct location 