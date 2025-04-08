# Multi-Project Collection Folder Structure

This reference file provides guidance for organizing a workspace containing multiple related writing projects, such as a book series or educational library. The structure is designed to facilitate both project-specific work and cross-project consistency.

## Core Directory Structure

```
workspace/
├── Projects/              # Contains all individual project folders
│   ├── Project1/          # First project (e.g., Book 1, Course 1)
│   │   ├── Manuscript/    # Actual writing content
│   │   ├── Outlines/      # Project-specific outlines
│   │   └── Research/      # Project-specific research
│   ├── Project2/          # Second project
│   │   ├── Manuscript/
│   │   ├── Outlines/
│   │   └── Research/
│   └── ...                # Additional projects as needed
├── Shared/                # Resources used across multiple projects
│   ├── Characters/        # Character profiles for characters in multiple projects
│   ├── Settings/          # Setting descriptions used across projects
│   ├── Terminology/       # Glossary and terminology consistent across projects
│   ├── Timeline/          # Master timeline showing chronology across projects
│   └── Templates/         # Document templates for maintaining consistency
├── Meta/                  # Collection-wide planning and documentation
│   ├── collection_outline.md   # Master outline showing relationships between projects
│   ├── style_guide.md          # Collection-wide style guidelines
│   └── development_notes.md    # Notes on the development of the entire collection
├── .cursor/               # System files and author profile
│   ├── Author/            # Author profile information
│   ├── rules/             # System rules
│   └── templates/         # Document templates
└── docs/                  # Documentation and guides
    ├── collection_plan.md # Master plan for the entire collection
    └── ...                # Other documentation
```

## Structure Variations

### Book Series Structure

For fiction series, consider this organization:

```
workspace/
├── Series/                        # Main container for the series
│   ├── Book1_Title/               # First book in the series
│   │   ├── Manuscript/
│   │   │   ├── Chapter01.md
│   │   │   ├── Chapter02.md
│   │   │   └── ...
│   │   ├── Outlines/
│   │   │   ├── book1_outline.md
│   │   │   └── detailed_outline.md
│   │   └── Research/
│   │       ├── book1_specific_characters.md
│   │       └── book1_specific_settings.md
│   ├── Book2_Title/               # Second book
│   │   └── ...
│   └── Book3_Title/               # Third book
│       └── ...
├── Shared/                        # Series-wide elements
│   ├── Characters/
│   │   ├── protagonist.md
│   │   ├── antagonist.md
│   │   └── supporting_cast.md
│   ├── Settings/
│   │   ├── world_map.md
│   │   ├── major_locations.md
│   │   └── rules_of_magic.md
│   ├── Terminology/
│   │   └── glossary.md
│   └── Timeline/
│       ├── series_chronology.md
│       └── historical_events.md
└── Meta/
    ├── series_arc.md              # Overall series arc
    ├── series_themes.md           # Themes that develop across books
    └── marketing_notes.md         # Notes on series branding and marketing
```

### Educational Library Structure

For educational content collections:

```
workspace/
├── Courses/                      # Main container for educational content
│   ├── Course1_Title/            # First course or educational module
│   │   ├── Lessons/              # Instead of Manuscript
│   │   │   ├── Lesson01.md
│   │   │   ├── Lesson02.md
│   │   │   └── ...
│   │   ├── Exercises/            # Practice materials
│   │   │   ├── Exercise01.md
│   │   │   └── ...
│   │   ├── Assessments/          # Tests or quizzes
│   │   └── Resources/            # Course-specific resources
│   └── Course2_Title/
│       └── ...
├── Shared/
│   ├── Concepts/                 # Core concepts used across courses
│   ├── Examples/                 # Examples that may be referenced in multiple courses
│   ├── Diagrams/                 # Visual assets shared across courses
│   ├── Terminology/              # Glossary and key terms
│   └── Templates/                # Standardized formats for lessons, exercises, etc.
└── Meta/
    ├── curriculum_map.md         # How courses relate to each other
    ├── learning_objectives.md    # Overall learning goals
    └── instructional_design.md   # Notes on pedagogical approach
```

### Content Collection Structure

For mixed-format collections (books, articles, etc.):

```
workspace/
├── Content/                      # Main container for content
│   ├── Books/                    # Book-length content
│   │   ├── Book1/
│   │   └── Book2/
│   ├── Articles/                 # Article-length content
│   │   ├── Article1.md
│   │   └── Article2.md
│   ├── Scripts/                  # Scripts for audio/video content
│   │   └── ...
│   └── Presentations/            # Slide decks and presentation materials
│       └── ...
├── Shared/
│   ├── Topics/                   # Topic guides referenced across content
│   ├── Research/                 # Research materials used in multiple pieces
│   ├── Media/                    # Images, diagrams, and other media
│   └── Boilerplate/              # Standard text sections reused across content
└── Meta/
    ├── content_calendar.md       # Publication schedule
    ├── audience_profiles.md      # Target audience information
    └── style_guide.md            # Brand voice and style guidelines
```

## Project-Specific Structure

Each individual project within the collection should follow an appropriate structure based on its specific type and the chosen narrative framework (Three-Act, Hero's Journey, etc.). Refer to the corresponding structure reference files for details:

- `.cursor/Research/folder_structures/heroes_journey_folders.md`
- `.cursor/Research/folder_structures/three_act_folders.md`
- `.cursor/Research/folder_structures/save_the_cat_folders.md`
- `.cursor/Research/folder_structures/snowflake_folders.md`
- `.cursor/Research/folder_structures/generic_novel_folders.md`
- `.cursor/Research/folder_structures/nonfiction_folders.md`

## Best Practices for Multi-Project Management

1. **Consistent Naming Conventions**: Use clear, consistent naming patterns across all projects.
2. **Clear Separation of Concerns**: Clearly distinguish between project-specific and shared resources.
3. **Cross-Reference Documentation**: Maintain explicit references between related elements in different projects.
4. **Version Control**: Consider using version control for tracking changes across multiple projects.
5. **Centralized Timeline**: For chronological works, maintain a single source of truth for timeline information.
6. **Modular Approach**: Design content to be modular where possible to allow reuse and recombination.
7. **Progressive Enhancement**: Start with core shared elements and progressively enhance with project-specific details.

## Recommendations for Different Collection Types

### For Book Series
- Maintain character consistency sheets that track character evolution across books
- Create a series bible that documents all world rules and prevents contradictions
- Develop a series arc document showing how themes and plots evolve across books

### For Educational Content
- Create learning paths that show prerequisites and connections between modules
- Maintain consistent formatting and layout across all educational materials
- Develop scaffolded content that builds on previously introduced concepts

### For Mixed Content Collections
- Use consistent terminology and style across different content formats
- Create content blocks that can be repurposed across different formats
- Maintain a unified voice and brand identity across all content types 