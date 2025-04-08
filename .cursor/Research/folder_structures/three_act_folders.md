# Three-Act Structure Folder Organization

This reference guide provides a recommended folder structure for projects following the classic Three-Act Structure narrative framework.

## Core Concept

The Three-Act Structure is a storytelling model that divides a narrative into three parts (setup, confrontation, and resolution), with key turning points that shift the direction of the story. This folder organization aligns with this framework to help track plot development, character arcs, and narrative pacing.

## Recommended Folder Structure

```
Project Root/
│
├── Manuscript/                   # Contains the actual writing that will be compiled
│   ├── Act_1-Setup/              # 25% of story - Establishes characters, world, and conflict
│   │   ├── 01-Opening_Image/
│   │   ├── 02-Setup/
│   │   ├── 03-Inciting_Incident/
│   │   └── 04-Plot_Turn_1/       # First major turning point/plot point
│   │
│   ├── Act_2-Confrontation/      # 50% of story - Develops the conflict, raises stakes
│   │   ├── 05-Rising_Action/
│   │   ├── 06-Midpoint/          # Central turning point - shifts from reaction to action
│   │   ├── 07-Complications/
│   │   └── 08-Plot_Turn_2/       # Second major turning point/plot point
│   │
│   └── Act_3-Resolution/         # 25% of story - Climax and resolution
│       ├── 09-Final_Push/
│       ├── 10-Climax/
│       └── 11-Resolution/
│
├── Outlines/
│   ├── project_outline.md           # High-level outline of the entire project
│   ├── structure_beats.md           # Tracks key structural beats and turning points
│   ├── character_arcs.md            # Maps character development across the three acts
│   ├── theme_development.md         # Tracks thematic development across acts
│   └── detailed_outline/            # Folder for detailed scene/chapter outlines
│       ├── act1_scenes.md
│       ├── act2_scenes.md
│       └── act3_scenes.md
│
├── Research/
│   ├── Characters/
│   │   ├── Protagonist/          # Main character(s)
│   │   ├── Antagonist/           # Opposition characters
│   │   ├── Supporting/           # Secondary and tertiary characters
│   │   └── Character_Relationships/ # Relationship dynamics
│   │
│   ├── Settings/
│   │   ├── Primary_Locations/    # Main settings
│   │   └── Secondary_Locations/  # Less frequently used settings
│   │
│   ├── Plot/
│   │   ├── main_conflict.md      # Central conflict documentation
│   │   ├── subplots.md           # Supporting storylines
│   │   ├── plot_twists.md        # Planned surprises and reversals
│   │   └── backstory.md          # Relevant history and background
│   │
│   ├── Themes/                   # Thematic elements
│   │
│   └── Research_Notes/           # General research for the story
│
└── docs/
    └── plan.md                   # Project plan and progress tracking
```

## Adaptation Guidelines

This structure can be adapted based on:

1. **Project Complexity:**
   - For simpler projects, consider combining scenes within act folders
   - For complex projects, you might add additional sub-folders for sequences within acts
   - Act 2 can be split into 2A and 2B at the midpoint for better organization

2. **Genre Specifics:**
   - Thriller: Add plot twist tracking under Plot
   - Romance: Add relationship development arc
   - Mystery: Add clues/red herrings tracking

3. **Narrative Variations:**
   - Non-linear narratives: Add timeline tracking document
   - Multiple POVs: Consider organizing by character arcs or POV scenes

## Key Benefits of This Structure

1. **Structural Clarity:** Clear visualization of the three-act progression
2. **Pacing Control:** Easy to assess and balance content across acts
3. **Turning Point Focus:** Highlights critical narrative shifts
4. **Progress Tracking:** See at a glance how much of each act is completed
5. **Balance Assessment:** Ensure appropriate proportion between setup, confrontation and resolution

## Implementation Notes

- Name files with numbering (e.g., `01_Opening.md`) to maintain sequence
- Consider using prefixes to indicate act number (A1_, A2_, A3_)
- Each act folder can include notes about the function and purpose of that act
- The midpoint in Act 2 is a critical structural element - consider highlighting it
- Keep turning points (Plot Turn 1, Midpoint, Plot Turn 2) in separate files to emphasize their importance 