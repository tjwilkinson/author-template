# Repository Management Rules

This rule file defines when and how to use the repository management scripts within this project. These scripts help maintain separation between template structure and writing content.

## Content Organization

**CRITICAL RULE: The `main` branch must ONLY contain template files, server files, and the empty Multiverse directory structure.**

### Simplified Content Structure

All writing content MUST be organized within a single top-level directory:

- **`Multiverse/`** - This directory contains the entire author multiverse
  - This folder is included in the main branch as an empty structure
  - All actual writing content should be committed only to writing branches
  - The `Multiverse/` directory serves as a clean boundary between template and content

Inside the `Multiverse/` directory, writers can organize their work:
- `Multiverse/Series/` - Multiple books in a series
- `Multiverse/Education/` - Related educational materials
- `Multiverse/Shared/` - Resources shared across projects
- `Multiverse/Meta/` - Collection-wide planning

This organization provides several benefits:
1. Clear separation between template files and writing content
2. Standard directory structure included in the main branch
3. Makes it obvious to users where content should go
4. Easy to create new writing projects by branching from main

### Branch Structure

- **Main Branch**: 
  - Contains template files, server implementation, and the empty Multiverse/ directory structure
  - NEVER commit actual writing content to the main branch
  - Only push template improvements and structure changes to main

- **Writing/Universe Branches**:
  - ALL writing work must be done in separate branches
  - Each branch contains its author content within the `Multiverse/` directory
  - A single branch can contain multiple related projects within appropriate subdirectories
  - The branch structure supports the full project organization described in the setup guide
  - **IMPORTANT:** When pushing to GitHub, the Multiverse directory and its content SHOULD be included
  - **IMPORTANT:** When merging with main, ONLY template improvements should be included, NOT Multiverse content

## Pushing and Merging Rules

### Pushing to GitHub from Writing/Universe Branches

When pushing a writing/universe branch to GitHub:

1. **Include Multiverse Content**:
   - The entire Multiverse directory and all writing content within it SHOULD be pushed
   - This preserves the complete writing project in the remote repository
   - Run a normal `git push origin <branch-name>` to include all content

2. **Backing Up Content**:
   - Pushing to GitHub serves as a backup of your writing content
   - All content organization, structure, and files are preserved

### Merging with Main Branch

When you need to merge template improvements TO the main branch:

1. **Use Template Mode**:
   - Always use the template mode script before merging to main
   - Run `./template-mode.sh on` to activate template mode
   - This ensures Multiverse content changes are ignored

2. **Push Only Template Changes**:
   - Use `git push origin HEAD:main` to push ONLY template changes to main
   - This preserves the empty Multiverse structure in main
   - Multiverse content stays in the writing branch and is NOT merged to main

3. **Return to Writing Mode**:
   - After pushing template changes, run `./template-mode.sh off`
   - This ensures your content continues to be tracked correctly in your writing branch

## Author Profile Management

When branching from an existing universe branch (not main), the following rules MUST be followed:

1. **Determine Author Identity**:
   - Explicitly ask the user whether the new branch will be for the same author or a different author
   - This determination is CRITICAL for maintaining appropriate author profiles

2. **Same Author Scenario**:
   - If the same author will be writing in the new branch, copy all author profile files:
     - `.cursor/Author/profile.md`
     - `.cursor/Author/vocabulary.md`
     - `.cursor/Author/style_guide.md`
     - `.cursor/Author/influences.md`
   - This ensures style consistency across the author's projects
   - Any style updates should be propagated across all of the author's branches

3. **Different Author Scenario**:
   - If a different author will be writing, create new author profile files through the setup process
   - Do NOT copy the previous author's profile files
   - Guide the new author through creating their unique profile
   - Ensure clear separation between different authors' styles and preferences

4. **Collaborative Writing**:
   - For collaborative projects, create a specialized collaborative profile
   - Document the agreed-upon style, vocabulary, and approach for the collaboration
   - Note individual author contributions and style variances where relevant

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

This script automatically handles gitignore rules. Since the Multiverse directory is now part of the repository structure, it ensures that the directory exists but does not ignore it.

- **When to use**:
  - After the initial project setup
  - When setting up a new writing branch

- **How to use**:
  ```bash
  # Ensure the Multiverse directory structure exists
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

### Automatic Template Mode for Non-Multiverse Files

**CRITICAL RULE: Any time a file outside of the Multiverse/ directory is created or edited, template mode MUST be toggled before and after.**

1. **Before editing any non-Multiverse file**:
   - Automatically run `./template-mode.sh on`
   - Inform the user that template mode has been activated
   - Explain that changes to these files affect the template structure

2. **During non-Multiverse file editing**:
   - Clearly indicate to the user that they are editing template files
   - Remind the user that these changes should eventually be pushed to main

3. **After completing non-Multiverse file edits**:
   - Commit the changes with a clear message about the template improvements
   - If pushing to main now, use `git push origin HEAD:main`
   - If not pushing to main yet, run `./template-mode.sh off` to return to writing mode
   - Inform the user that template mode has been deactivated

4. **Exception for Temporary Files**:
   - Temporary files or logs that are already ignored in .gitignore do not require template mode
   - For all other non-Multiverse files, this rule is mandatory

### For Project Setup

1. Guide the user through the setup process following the setup guide
2. Create the appropriate folder structure within the `Multiverse/` directory
3. **After creating content directories, run `./update-gitignore.sh`**
4. Complete the setup process
5. Inform the user about the repository structure and available scripts

### For Writing Activities

1. Ensure template mode is off (normal writing mode)
2. Work in content directories within `Multiverse/` as needed

### For Starting a New Project

1. If the user wants to start a new, separate writing project:
   - Create a new branch from main: `git checkout -b new-writing-project`
   - This ensures they start with a clean template with the empty Multiverse structure
   - Complete the setup process for this new branch, creating content within `Multiverse/`
   - Run `./update-gitignore.sh` after setup

## Error Prevention

If the user attempts to push template changes without using template mode:
1. Alert them to the potential issue
2. Recommend running `./template-mode.sh on` first
3. Explain that this ensures proper handling of template vs content

If the user attempts content creation while in template mode:
1. Alert them that template mode is active
2. Recommend running `./template-mode.sh off` first
3. Explain that their content changes may not be properly tracked in this mode

If the user attempts to commit actual writing content directly to main:
1. Immediately alert them that this violates the repository structure
2. Recommend creating or switching to a writing branch
3. Explain that main should only contain the structure, not actual content

If the user attempts to create content outside the `Multiverse/` directory:
1. Alert them that all content must be placed inside the `Multiverse/` directory
2. Explain the benefits of this organization
3. Offer to help them move the content to the correct location

### Branch Creation for Writing in Multiverse

**CRITICAL RULE: If a user attempts to write inside the Multiverse folder or start any writing process while in the main branch, a new universe branch MUST be created first.**

When this situation is detected:

1. **Interrupt the writing attempt**:
   - Immediately inform the user that writing in main is not allowed
   - Explain that a dedicated branch is required for writing content

2. **Guide branch creation process**:
   - Ask the user for a universe/branch name
   - Have a conversation to help the user decide on an appropriate name if needed
   - Suggest names related to their writing project (e.g., "fantasy-series", "mystery-novel", etc.)

3. **Create the branch**:
   - Create a new branch with the desired name: `git checkout -b <universe-name>`
   - Run `./update-gitignore.sh` to ensure the Multiverse structure is properly set up
   - Set up author profile files if needed (following the Author Profile Management rules)

4. **Redirect writing activity**:
   - Once the branch is created, direct the user to continue their writing within the new branch
   - Remind the user that all writing content must stay within the Multiverse directory

5. **Never allow exceptions**:
   - Under NO circumstances should writing be allowed to start in the main branch
   - This rule must be enforced without exception to maintain repository integrity 