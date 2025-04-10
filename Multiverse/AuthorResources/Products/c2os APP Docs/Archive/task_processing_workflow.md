# Analysis: TRO Processing Flow Chart

This document details the workflow for processing tasks identified as actionable during Triage, based on the provided TRO Processing Flow Chart.

This flow begins when an item from the "Unprocessed Tasks List" is selected.

## Processing Workflow Steps:

1.  **Define the Action/Project:**
    *   **Input:** One Unprocessed Task.
    *   **Decision:** Does this require more than one step?
        *   **NO (Multi-step):** Define as a **Project**.
            *   Specify Project Goal/Outcome.
            *   Determine the **very next physical action** for the project.
        *   **YES (Single-step):** Clarify the **very next physical action**.
    *   **Output:** A clearly defined **Next Action** (potentially linked to a Project).

2.  **Immediate Action Check:**
    *   **Input:** The defined Next Action.
    *   **Decision:** Can this Next Action be done *right now* in 2 minutes or less?
        *   **YES:** **Do It Now**.
            *   Perform the action.
            *   Mark complete (or determine the next action if part of a project).
            *   -> **End Processing for this item.**
        *   **NO:** Proceed.

3.  **Delegation Check:**
    *   **Input:** The Next Action.
    *   **Decision:** Can this be delegated?
        *   **YES:** **Delegate**.
            *   Assign to the appropriate person.
            *   Create a "Waiting For" item/task to track it (assigned to you, noting person and follow-up).
            *   -> **End Processing for this item.**
        *   **NO:** Proceed to Defer.

4.  **Defer (Clarify for Future Action):**
    *   **Input:** The Next Action that will be done later by you.
    *   **Actions:**
        *   **Record Next Step:** Ensure action clarity. Link to Project if applicable.
        *   **Add Notes:** Include necessary context, future steps ideas, resource links (only enough to clear the mind).
        *   **Schedule Next Step:** Assign dates:
            *   **Soft Date (Do Date/Defer Date):** *Required*. When to see/consider the task again.
            *   **Hard Date (Due Date/Deadline):** Optional. Only for external deadlines with consequences.
            *   **Calendar:** Optional. Block time if needed (e.g., >30min task, appointment).
            *   **Someday/Maybe:** Assign this status/list if no specific timeframe.
        *   **Assign Contexts:** Tag where/how the action occurs:
            *   **Major Context (Required):** e.g., `@Computer`, `@Office`, `@Home`, `@Errands`.
            *   **Other Contexts (Optional):** e.g., `@Meeting-ProjectX`, `@Agenda-John`.
    *   -> **End Processing for this item.**

## Key Concepts for App Implementation:

*   **Task vs. Project Distinction:** Need clear ways to manage both single actions and multi-step projects.
*   **Next Action Focus:** Task descriptions prioritize the immediate physical step.
*   **2-Minute Rule:** Implemented via the "Do It Now" path.
*   **Delegation / Waiting For:** Requires specific tracking functionality (e.g., a dedicated list, status, or assigned user).
*   **Scheduling:** Primary focus on "Do Dates" (when to resurface the task). Secondary support for "Due Dates". Calendar integration and a Someday/Maybe list are valuable.
*   **Contexts:** Essential for filtering tasks later. Requires a flexible tagging system. 