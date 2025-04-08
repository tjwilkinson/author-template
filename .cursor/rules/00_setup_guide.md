# Author Project Setup Guide

**IMPORTANT:** This is a temporary rule file that will guide you (the AI assistant) through helping the user set up their writing project. After completing setup, you should move this file to `.cursor/Archive/`.

## Core Instructions for AI Assistant

When a user opens this project for the first time, you should:

1. Identify that this is a new author project that needs setup.
2. Inform the user that you'll guide them through an interactive setup process.
3. Follow the workflow outlined below.
4. After setup completion, move this file to `.cursor/Archive/00_setup_guide.md`.

## Interactive Setup Workflow

### 1. Project Type & Purpose

Begin by having a conversation with the user about their writing project. Ask about:

- What type of writing project they're creating (novel, short story, screenplay, non-fiction book, etc.)
- The genre (if applicable)
- Their experience level with writing
- Their goals for the project

Explain that this information will help customize the project structure to best suit their needs.

### 2. Project Organization (Single vs. Multi-Project)

Discuss with the user whether they want to set up:

- **Single Project:** A standalone work (e.g., one novel, one non-fiction book)
- **Multi-Project Collection:** Multiple related works organized in one workspace, such as:
  - **Book Series:** Multiple books sharing characters, world, or timeline
  - **Educational Library:** Related educational materials with consistent formatting and cross-references
  - **Content Collection:** Various formats (books, articles, scripts) sharing themes or subject matter

For multi-project collections, discuss:
- How the projects are related to each other
- What elements are shared across projects (characters, settings, terminology, style)
- Whether they prefer hierarchical organization (e.g., series/book/chapter) or flat organization with cross-references
- Timeline for development (sequential or parallel work on multiple projects)

Based on their response, adjust the folder structure recommendations in later steps to accommodate the appropriate organization.

### 3. Writing Structure Education & Selection

Educate the user about common writing structures/templates and help them select one:

- **Hero's Journey:** Explain this 12-stage narrative framework popular for mythic stories and character transformations.
- **Three-Act Structure:** Describe this classic beginning-middle-end structure used in novels and screenplays.
- **Save the Cat:** Outline this 15-beat screenplay structure that can be adapted for novels.
- **Snowflake Method:** Explain this approach of starting with a simple premise and expanding outward.
- **Custom Structure:** Offer the option to create a customized structure.

Provide brief explanations of each, highlighting strengths and typical use cases. Recommend structures based on their project type but let them choose.

For multi-project collections, discuss whether they want to:
- Apply the same structure across all projects
- Use different structures for different projects
- Create a hybrid structure specific to their collection

### 4. Folder Structure Creation

Based on the user's selections, create an appropriate folder structure:

1. **Reference Structure Files First:** Before creating any folders, consult the appropriate reference files:
   - `.cursor/Research/folder_structures/heroes_journey_folders.md` (for Hero's Journey projects)
   - `.cursor/Research/folder_structures/three_act_folders.md` (for Three-Act Structure projects)
   - `.cursor/Research/folder_structures/save_the_cat_folders.md` (for Save the Cat projects)
   - `.cursor/Research/folder_structures/snowflake_folders.md` (for Snowflake Method projects)
   - `.cursor/Research/folder_structures/generic_novel_folders.md` (for general novel projects)
   - `.cursor/Research/folder_structures/nonfiction_folders.md` (for non-fiction projects)
   - `.cursor/Research/folder_structures/multi_project_folders.md` (for multi-project collections)

2. **Customize Based on User Needs:** Adapt the reference structure based on:
   - The specific type of project (novel, non-fiction, screenplay, etc.)
   - Genre requirements (e.g., worldbuilding folders for fantasy)
   - Project complexity (simple vs. complex organizational needs)
   - User's experience level and preferences
   - For multi-project collections: shared resources, cross-referencing needs, and hierarchical organization
   
3. **Create the Core Structure:**
   
   For single projects:
   - Always create a `Manuscript/` folder at the root level
   - Based on the chosen structure, create appropriate sub-folders within `Manuscript/`
   - Create an `Outlines/` folder with appropriate sub-files
   - Create a `Research/` folder with appropriate sub-folders (e.g., Characters, Settings, Timeline)
   - Create any additional folders needed for their specific project type

   For multi-project collections:
   - Create a `Projects/` or `Series/` folder at the root level
   - Within this folder, create sub-folders for each individual project
   - Within each project folder, follow the single-project structure pattern
   - Create a `Shared/` folder at the root level for resources used across multiple projects, including:
     - `Shared/Characters/` for characters appearing in multiple projects
     - `Shared/Settings/` for locations used across projects
     - `Shared/Terminology/` for consistent terms and concepts
     - `Shared/Timeline/` for maintaining chronology across projects
     - `Shared/Templates/` for document templates to maintain consistency
   - Create a `Meta/` folder for series-wide or collection-wide planning and documentation

4. **Update GitIgnore Files:** After creating the folder structure:
   - Check if .gitignore and .gitignore-template files exist
   - If they exist, add any custom content folders to both files
   - Ensure all newly created top-level directories are added to both files
   - This will ensure content folders are properly excluded when pushing template updates

5. **Explain the Purpose:** As you create each folder, explain:
   - Its purpose within the chosen narrative structure
   - How it relates to the writing process
   - What types of content should be placed there
   - How it connects to other folders in the structure
   - For multi-project collections, explain the relationship between project-specific and shared resources

Remember that folder structures should facilitate the writing process based on the chosen narrative framework. The reference files provide patterns that should be adapted to the specific project, not followed rigidly.

### 5. Author Profile Development

Guide the user through creating their author profile:

- Ask questions about their writing style preferences.
- Discuss vocabulary level, sentence structure preferences, tone, etc.
- Inquire about favorite authors and literary influences.
- Discuss any specific stylistic elements they want to incorporate or avoid.

Based on their responses, create and populate:
- `.cursor/Author/profile.md`
- `.cursor/Author/vocabulary.md`
- `.cursor/Author/style_guide.md`
- `.cursor/Author/influences.md`

For multi-project collections, discuss whether they want to:
- Maintain a single consistent style across all projects
- Develop distinct styles for different projects or series
- Create a style guide with core elements and project-specific variations

### 6. Initial Outline Creation

Based on the selected structure template:

- Create a high-level outline in `Outlines/project_outline.md`
- Create a more detailed outline in `Outlines/detailed_outline.md`
- If using a specific structure (Hero's Journey, etc.), create a structure-specific outline with the appropriate beats/stages

For multi-project collections:
- Create a master outline in `Meta/collection_outline.md` showing the relationship between projects
- Create project-specific outlines in each project folder
- Set up cross-referencing between related elements across projects

Fill in template sections where possible based on information gathered during setup, but leave it flexible for the user to modify.

### 7. Project Plan Creation

Based on the project type and information gathered, create a customized project plan from scratch:

- Generate a tailored `docs/plan.md` with appropriate phases and checklist items for the specific project type.
- Customize the plan based on:
  - Project type (novel, non-fiction book, technical manual, "For Dummies"-style guide, etc.)
  - Selected structure and complexity
  - Project scope and timeline
  - Specific goals identified by the user

For multi-project collections:
- Create a master plan in `docs/collection_plan.md` showing the overall development timeline
- Create individual project plans in each project folder
- Set up dependencies between projects if they must be developed in a specific order
- Create resource allocation plans for shared elements

This plan should serve as a living document that will be maintained and updated throughout the project. The checklist items should reflect the actual workflow appropriate for the specific type of project.

For example:
- A novel project plan would include character development, plot structuring, and draft revisions
- A technical manual would focus on concept explanation, example creation, and technical accuracy
- An instructional guide might emphasize step-by-step procedures, visual aids, and beginner-friendly language

Do not rely on any templates - create a unique plan tailored to this specific project based on the information gathered during setup.

### 8. Project Rules Creation

Create the following standard rules files that will govern the AI's behavior throughout the project:

- `.cursor/rules/workflow_rules.md`: Define the core workflow processes that must be followed:
  - **Plan Maintenance:** Always maintain and update the checklist in the plan document after completing any item.
  - **Outline Maintenance:** After each section or chapter is drafted, immediately update the detailed outline to reflect any changes from the initial plan. The outline must be EXTREMELY comprehensive and include:
    - All plot points and narrative developments
    - Character appearances, development, and key dialogue concepts
    - Setting details and descriptions
    - Thematic elements and symbolism
    - Foreshadowing elements and their eventual payoffs
    - Cross-references to related sections or chapters
    - Any narrative devices or techniques used
    - Status of the section (draft, revised, final)
    - Notes about future implications of events in this section

  - **Progressive Writing:** When writing a new section, use the outline as your PRIMARY source of information and context. The detailed outline should contain ALL essential information needed for continuity and consistency. Only consult the full manuscript when:
    - The outline doesn't contain a specific detail you need
    - You need to verify exact wording of previous dialogue or descriptions
    - You need to check subtle narrative elements not captured in the outline
    - The user specifically requests a close match to previous sections' style or tone

  - **Regular Status Updates:** Periodically remind the user of overall project progress by referencing the plan checklist.

  - For multi-project collections, add:
    - **Cross-Project Consistency:** When working on any element that appears in multiple projects, check all relevant shared resources.
    - **Update Propagation:** When a shared element is modified, identify all projects affected and update accordingly.
    - **Collection Overview:** Periodically provide updates on the status of the entire collection, not just individual projects.

- `.cursor/rules/style_consistency.md`: Define how to:
  - **Author Profile Integration:** ALWAYS consult the author profile documents before generating any creative content. These documents should be viewed as authoritative references:
    - `.cursor/Author/profile.md`: Reference for overall writing approach, perspective, and author goals.
    - `.cursor/Author/vocabulary.md`: Pull specific words, phrases, and language patterns directly from this document to maintain the author's unique voice. When introducing new vocabulary, add it to this document.
    - `.cursor/Author/style_guide.md`: Apply the specific sentence structures, paragraph lengths, dialogue styles, and other technical elements defined here. This includes punctuation preferences, formatting choices, and structural patterns.
    - `.cursor/Author/influences.md`: Draw inspiration from the listed influences when suggesting new approaches or techniques.
  
  - **Character Consistency:** Maintain a consistent portrayal of all characters by:
    - Referencing character descriptions in the research and outline documents
    - Using consistent speech patterns, vocabulary, and mannerisms for each character
    - Ensuring character development follows the trajectory established in the outline
    - Flagging potential inconsistencies for the author to review
    
  - **Setting and Terminology Consistency:** Ensure all locations, items, concepts, and terminology are used consistently by:
    - Creating and maintaining a terminology list in the research documents
    - Using consistent descriptions for recurring settings
    - Maintaining consistent rules for any speculative elements (magic, technology, etc.)
    
  - **Genre Conventions:** Apply genre-specific conventions established during project setup:
    - Follow the tropes, patterns, and reader expectations for the chosen genre
    - Maintain the appropriate tone for the genre (serious, humorous, dark, uplifting, etc.)
    - Structure scenes according to genre expectations (pacing, conflict types, resolution patterns)

  - For multi-project collections, add:
    - **Project-Specific Style Variations:** Apply any project-specific style guidelines while maintaining collection-wide consistency.
    - **Cross-Project References:** Maintain consistent references to events, characters, or concepts that appear in multiple projects.
    - **Timeline Consistency:** Ensure chronological consistency for elements that span multiple projects.

These rules should be largely the same across all projects, focusing on *process consistency* rather than project-specific content details. The project-specific details will be contained in the outlines and author profile, which these rules will direct the AI to reference.

### 9. Setup Completion

Once setup is complete:

1. Provide a summary of everything created.
2. Explain to the user how to start using the project.
3. Move this file to `.cursor/Archive/00_setup_guide.md`.
4. Inform the user that the initial setup is complete and that you are now operating under the new project rules.

## Final Notes to AI Assistant

- Approach this interaction as an educational opportunity. Many users may be unfamiliar with formal writing structures.
- Be encouraging and positive, especially when working with beginning writers.
- Focus on flexibility—the structure should serve the author, not restrict them.
- If the user has specific needs that don't fit this template, adapt accordingly.
- If a directory or file already exists, check with the user before modifying it. 