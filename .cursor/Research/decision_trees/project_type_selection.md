# Project Type Selection Decision Tree

```mermaid
flowchart TD
    A[Start Project Setup] --> B{Fiction or Non-Fiction?}
    B -->|Fiction| C{Novel Length?}
    B -->|Non-Fiction| D{Non-Fiction Type?}
    
    C -->|Full Novel| E{Genre?}
    C -->|Novella| F[Simplified Novel Structure]
    C -->|Short Story| G[Basic Beginning/Middle/End]
    
    E -->|Fantasy/Sci-Fi| H[Complex World-Building Template]
    E -->|Mystery/Thriller| I[Plot-Driven Template]
    E -->|Literary| J[Character-Driven Template]
    E -->|Romance| K[Relationship-Focused Template]
    E -->|Historical| L[Research-Heavy Template]
    E -->|Other| M[Generic Novel Template]
    
    D -->|Academic| N[Research-Based Structure]
    D -->|Memoir| O[Personal Narrative Structure]
    D -->|Self-Help| P[Chapter-Based Instructional]
    D -->|Technical| Q[Structured Documentation]
    D -->|Other Non-Fiction| R[Generic Non-Fiction Template]
    
    H --> S{Preferred Writing Approach?}
    I --> S
    J --> S
    K --> S
    L --> S
    M --> S
    
    N --> T{Research Level?}
    O --> U{Chronological or Thematic?}
    P --> V{Exercise-Based?}
    Q --> W{Code Examples?}
    R --> X{Research-Heavy?}
    
    S -->|Outline First| AA[Outliner Approach]
    S -->|Discovery Writer| AB[Discovery Approach]
    S -->|Structured Method| AC{Choose Writing Method}
    
    AC -->|Hero's Journey| AD[Hero's Journey Template]
    AC -->|Three-Act| AE[Three-Act Template]
    AC -->|Save the Cat| AF[Save the Cat Template]
    AC -->|Snowflake| AG[Snowflake Method Template]
    
    T -->|Heavy Research| AH[Research-First Structure]
    T -->|Moderate| AI[Balanced Structure]
    T -->|Light| AJ[Content-First Structure]
    
    U -->|Chronological| AK[Timeline Structure]
    U -->|Thematic| AL[Topic-Based Structure]
    
    V -->|Yes| AM[Workbook Structure]
    V -->|No| AN[Concept Structure]
    
    W -->|Yes| AO[Documentation Structure]
    W -->|No| AP[Conceptual Structure]
    
    X -->|Yes| AQ[Research-Heavy Structure]
    X -->|No| AR[Standard Structure]
```

## Decision Points and Outcomes

### Initial Project Type
- **Fiction vs Non-Fiction**: Determines the primary branch of the decision tree
- **Novel Length**: For fiction, determines complexity of structure needed
- **Non-Fiction Type**: For non-fiction, determines specialized structure

### Fiction Specifics
- **Genre Selection**: Determines specialized templates with focus on relevant elements
- **Writing Approach**: Determines organization of project files and workflow
  - **Outline First**: Heavily structured with detailed planning documents
  - **Discovery Writer**: Minimal structure with focus on draft folders
  - **Structured Method**: Follows specific writing methodology

### Non-Fiction Specifics
- **Research Level**: Determines balance between research and content files
- **Organization Approach**: Determines how content is structured (chronological/thematic/etc.)
- **Format Requirements**: Determines specialized templates for workbooks, technical docs, etc.

## Output
Each endpoint in this decision tree will map to a specific template configuration combining:
1. Folder structure
2. Document templates
3. Writing guidance
4. Research organization
5. Reference materials 