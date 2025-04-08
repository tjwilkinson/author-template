# Workflow Rules

This rule file governs the core workflow processes that must be followed throughout the author workspace.

## Content Analysis and Quality Control

### Automated Analysis

1. **Server Activation**: 
   - The Author Workspace Server must be started at the beginning of each writing session:
   ```bash
   source .cursor/Server/venv/bin/activate
   python .cursor/Server/app.py --mode continuous
   ```
   - The web interface will be available at http://127.0.0.1:5000

2. **Progressive Analysis**:
   - After each significant writing stage (chapter completion, major revision, etc.), perform analysis via the web interface
   - Enter the path to the written content in the analysis panel
   - Address any critical issues identified before proceeding

3. **Pre-Submission Analysis**:
   - Before finalizing any major section, run a validation check:
   ```bash
   python .cursor/Server/app.py --mode validate --target "path/to/content.md"
   ```
   - All critical issues must be resolved before a section is considered complete

4. **Regular Full-Project Scans**:
   - Schedule regular comprehensive analyses of the entire project:
   ```bash
   python .cursor/Server/app.py --mode batch --target "Projects/MyProject"
   ```
   - Document all issues found in the project notes

## Plan Maintenance

1. **Checklist Updates**: 
   - Always maintain and update the checklist in the plan document after completing any item
   - Mark tasks as completed with date and notes
   - Add new tasks as they emerge during the writing process

2. **Milestone Tracking**:
   - Record completion dates for major milestones
   - Update estimated completion dates based on actual progress
   - Document any significant deviations from the original plan

## Outline Maintenance

1. **Synchronize with Drafts**: 
   - After each section or chapter is drafted, immediately update the detailed outline to reflect any changes from the initial plan
   - The outline must be EXTREMELY comprehensive and include:
     - All plot points and narrative developments
     - Character appearances, development, and key dialogue concepts
     - Setting details and descriptions
     - Thematic elements and symbolism
     - Foreshadowing elements and their eventual payoffs
     - Cross-references to related sections or chapters
     - Any narrative devices or techniques used
     - Status of the section (draft, revised, final)
     - Notes about future implications of events in this section

2. **Version Control**:
   - When making significant changes to the outline, preserve the previous version
   - Note the rationale for major structural changes

## Progressive Writing

1. **Outline-First Approach**:
   - Use the outline as your PRIMARY source of information and context
   - The detailed outline should contain ALL essential information needed for continuity and consistency
   - Only consult the full manuscript when:
     - The outline doesn't contain a specific detail you need
     - You need to verify exact wording of previous dialogue or descriptions
     - You need to check subtle narrative elements not captured in the outline
     - The user specifically requests a close match to previous sections' style or tone

2. **Consistency Verification**:
   - Before writing new sections, verify character and setting consistency using the analysis server
   - Check for style consistency with previous sections

## Regular Status Updates

1. **Progress Reporting**:
   - Periodically remind the user of overall project progress by referencing the plan checklist
   - Provide statistics on completed sections, word count, and estimated completion

2. **Quality Metrics**:
   - Track the number and severity of issues identified by the analysis server
   - Report on consistency metrics and improvement over time

## Multi-Project Management

1. **Cross-Project Consistency**: 
   - When working on any element that appears in multiple projects, check all relevant shared resources
   - Run cross-project analysis to identify potential inconsistencies:
   ```bash
   python .cursor/Server/app.py --mode batch --target "Shared"
   ```

2. **Update Propagation**: 
   - When a shared element is modified, identify all projects affected and update accordingly
   - Run targeted analysis on affected projects

3. **Collection Overview**: 
   - Periodically provide updates on the status of the entire collection, not just individual projects
   - Generate comprehensive reports through the analysis server 