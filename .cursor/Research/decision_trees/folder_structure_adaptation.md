# Folder Structure Adaptation Decision Tree

```mermaid
flowchart TD
    A[Start Folder Structure Setup] --> B{Selected Project Template?}
    
    %% Fiction Templates
    B -->|Hero's Journey| C[Base Hero's Journey Structure]
    B -->|Three-Act| D[Base Three-Act Structure]
    B -->|Save the Cat| E[Base Save the Cat Structure]
    B -->|Snowflake| F[Base Snowflake Structure]
    B -->|Generic Novel| G[Base Generic Novel Structure]
    
    %% Non-Fiction Templates
    B -->|Academic| H[Base Academic Structure]
    B -->|Memoir| I[Base Memoir Structure]
    B -->|Self-Help| J[Base Self-Help Structure]
    B -->|Technical| K[Base Technical Structure]
    B -->|Generic Non-Fiction| L[Base Generic Non-Fiction]
    
    %% Common Adaptation Point for All Templates
    C --> M{Additional Components?}
    D --> M
    E --> M
    F --> M
    G --> M
    H --> M
    I --> M
    J --> M
    K --> M
    L --> M
    
    %% Additional Components
    M -->|World Building Needed| N[Add World Building Directory]
    M -->|Character Development| O[Add Character Directory]
    M -->|Plot Complexity| P[Add Plot Directory]
    M -->|Heavy Research| Q[Add Research Directory]
    M -->|Timeline Tracking| R[Add Timeline Directory]
    M -->|Multiple POVs| S[Add POV Directory]
    M -->|Visual Elements| T[Add Visual Directory]
    
    %% Advanced Customization
    N --> U{Complexity Level?}
    O --> U
    P --> U
    Q --> U
    R --> U
    S --> U
    T --> U
    
    U -->|Basic| V[Standard Structure]
    U -->|Intermediate| W[Enhanced Structure]
    U -->|Complex| X[Comprehensive Structure]
    
    %% Output Integration
    V --> Y{Integration Style?}
    W --> Y
    X --> Y
    
    Y -->|Separate Workspaces| Z[Parallel Directory Structure]
    Y -->|Integrated| AA[Nested Directory Structure]
    Y -->|Hybrid| AB[Linked Directory Structure]
```

## Folder Structure Adaptation Factors

### Base Template Selection
- Each project type starts with a predefined base folder structure
- Base structures align with specific writing methodologies
- All base structures include core components (manuscript, notes, etc.)

### Additional Component Factors
- **World Building**: For projects with complex settings or fictional worlds
  - Basic: Single folder for world notes
  - Intermediate: Categorized world elements (locations, cultures, etc.)
  - Complex: Hierarchical world database with cross-references

- **Character Development**: For character-driven narratives
  - Basic: Character profiles
  - Intermediate: Character arcs and relationship charts
  - Complex: Psychological profiles, evolution maps, connection networks

- **Plot Complexity**: For intricate or multi-layered plots
  - Basic: Plot point outlines
  - Intermediate: Scene-by-scene breakdowns
  - Complex: Multi-thread tracking system with cross-plot dependencies

- **Research Components**: For research-heavy projects
  - Basic: General research notes
  - Intermediate: Categorized research by topic
  - Complex: Annotated reference system with citation links

- **Timeline Tracking**: For non-linear or complex chronologies
  - Basic: Simple timeline
  - Intermediate: Parallel timeline tracking
  - Complex: Interactive timeline with event dependencies

- **Multiple POVs**: For stories with multiple perspectives
  - Basic: POV character list
  - Intermediate: POV-specific plot tracking
  - Complex: POV intersection mapping

- **Visual Elements**: For projects with visual components
  - Basic: Reference images folder
  - Intermediate: Categorized visual references
  - Complex: Storyboarding system

### Integration Methods
- **Parallel Structure**: Independent directories with minimal cross-referencing
- **Nested Structure**: Hierarchical organization with components as subdirectories
- **Linked Structure**: Independent directories with explicit cross-reference system

## Implementation Notes
- All folder structures include README files explaining purpose and organization
- Adaptation logic includes creation of templates for documents within each component
- Each folder structure is generated with example files to demonstrate usage 