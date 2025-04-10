# Productivity System Research for Second Brain App

This document summarizes research on three productivity systems relevant to the development of a new second brain/ultimate brain application.

## 1. Ultimate Brain (Thomas Frank)

*   **Platform:** Notion Template
*   **Core Idea:** An all-in-one "second brain" integrating tasks, projects, notes, and goals within Notion.
*   **Methodology:** Heavily based on Tiago Forte's **P.A.R.A.** (Projects, Areas, Resources, Archives) method for organization and incorporates principles from David Allen's **GTD** (Getting Things Done).
*   **Key Features:**
    *   Unified dashboard for tasks, notes, projects.
    *   "My Day" dashboard for daily planning.
    *   "Quick Capture" view for fast input.
    *   Supports sub-tasks, recurring tasks, priorities.
    *   Advanced archiving (Cold Tasks, Snoozed Tasks, Someday list).
    *   Optimized for different screen sizes.
    *   Includes bonus dashboards (e.g., recipes, book tracker).
*   **Target User:** Notion users looking for a comprehensive, pre-built system for personal productivity and knowledge management, particularly those familiar with or interested in P.A.R.A. and GTD.
*   **Source:** [https://thomasjfrank.com/brain/](https://thomasjfrank.com/brain/)

## 2. PPV (Pillars, Pipelines, Vaults) (August Bradley)

*   **Platform:** Notion System/Template (often delivered via a course)
*   **Core Idea:** A "Life Operating System" designed for **Focus** (on daily execution) and **Alignment** (connecting daily tasks to long-term goals and values).
*   **Methodology:** Custom framework (PPV) built specifically for Notion. Integrates robust **Personal Knowledge Management (PKM)**.
    *   **Pillars:** Represent core life areas or values.
    *   **Pipelines:** Manage the flow of tasks and projects towards goals.
    *   **Vaults:** Store and organize knowledge and resources.
*   **Key Features:**
    *   Emphasis on System Design and Systems Thinking.
    *   Action Zone (daily tasks), Alignment Zone (goals, values).
    *   Structured reviews (Daily, Weekly, Monthly, Quarterly).
    *   Mind Expansion Dashboard (PKM).
    *   Mindset & Identity Sculpting components.
    *   Designed to leverage Notion's unique capabilities (relations, rollups).
*   **Target User:** Individuals seeking a deep, integrated system for life management, goal alignment, and knowledge work within Notion. Appeals to knowledge workers, creators, and solopreneurs ready for a structured, comprehensive approach.
*   **Source:** [https://www.yearzero.io/notion-course](https://www.yearzero.io/notion-course)

## 3. TRO (Total Relaxed Organization) (Priacta)

*   **Platform:** Methodology with Training/Coaching (tool-agnostic, but provides tool-specific guidance)
*   **Core Idea:** Achieve "relaxed control" over workflow and time management, reducing stress and increasing productive time.
*   **Methodology:** Fuses concepts from **GTD**, **Covey's 7 Habits**, and other methods into a refined, easier-to-implement system. It's a form of "contextual productivity".
*   **Key Features/Advantages over traditional GTD:**
    *   Faster initial setup and control (no need to process everything at once).
    *   Prioritized task views (avoids scanning long lists).
    *   Very quick weekly reviews (e.g., 5 minutes).
    *   Automatic follow-up for delegated/"Waiting For" items.
    *   Strategies for handling overload/crises.
    *   Natural integration of life balance.
    *   Automatic focus on high-priority goals/projects.
    *   Step-by-step, tool-specific implementation guidance (unlike GTD's tool-agnostic nature).
    *   Less stressful email management ("Inbox Zero").
    *   Provides a daily prioritized "punch list".
*   **Target User:** Individuals and teams feeling overwhelmed, seeking stress reduction and significant productivity gains through a structured, coached methodology adaptable to their existing tools.
*   **Source:** [https://priacta.com/training/](https://priacta.com/training/), [https://priacta.com/total-relaxed-organization-faqs/](https://priacta.com/total-relaxed-organization-faqs/)

### TRO Review Process Details (Based on Toodledo Implementation)

*   **Philosophy:** Reviewing is "Previewing" – future-focused planning (5 mins/day, 5 mins/week, 5+ mins/month) rather than past analysis. Aims to ensure goals move forward steadily without daily re-evaluation of the entire task list, relying on smart dates.
*   **Core Lists:**
    *   **Do Today List (Starred in Toodledo):** Shows absolute "must-do" items for the day (hard date arrived or manually promoted). Sorted primarily by Priority (descending), then Auto. Kept short via correct processing and daily reviews.
    *   **Hotlist (Custom Search in Toodledo):** Shows tasks "heating up" (e.g., Medium+ priority, due in next few days, starred). Reviewed daily to identify tasks needing promotion to "Do Today".
    *   **Weekly Review List (Custom Search in Toodledo):** Shows "may do" tasks (no hard date, future start date, not starred, not negative priority) to catch items needing attention. Sorted primarily by Start Date (ascending), then Importance (descending).
    *   **Someday/Maybe List (Negative Priority in Toodledo):** Holds potential tasks deferred for later consideration. Kept out of most active views and reviewed monthly.

#### Daily Review (5 minutes, First thing AM)

1.  **Check Calendar:** Review appointments and strategic calendar for the day.
2.  **Clear Reminders:** Clear old appointment reminders.
3.  **Process Hotlist:** Star items to be done today, potentially reschedule others.
4.  **Validate Do Today:** Review starred list, unstar/reschedule anything not feasible today.
5.  **Budget Long Tasks:** Ensure tasks >30 mins are blocked on the calendar.
6.  **Reality Check:** Ensure the day's plan is ~80% doable and realistic.
7.  **Order (Optional):** Reorder Do Today list using priority if desired.
8.  **Print (Optional):** Print lists if needed.

#### Weekly Review (5 minutes, Recommended Monday AM after Daily Review)

1.  **Scan Weekly Review List:** Identify any "may do" tasks that have become important.
2.  **Re-process:** Assign hard dates or otherwise re-process these items to ensure they enter the daily workflow appropriately.
    *   *Alternative:* Review major context lists (less precise, requires ignoring starred/-1 priority).

#### Monthly Review (5+ minutes, Recommended 1st/Last Monday of Month after Weekly Review)

1.  **Review Someday/Maybe List:**
    *   Skim the list (e.g., Toodledo's -1 Negative Priority view).
    *   Promote items ready for action by assigning appropriate dates.
    *   Delete irrelevant/expired tasks.
    *   Consider scheduling enjoyable/"fun" items to ensure personal goals aren't neglected.
2.  **Reassess Time Use & Strategic Calendar (Quarterly Recommended):**
    *   Review strategic calendar and time budget worksheets.
    *   Evaluate progress on Most Profitable Activities (MPAs) and long-term goals.
    *   Adjust time allocations and strategic calendar as needed.

#### Mobile Considerations

*   Similar review process using mobile app/site views (Starred list for Do Today, Hotlist).
*   Emphasis on checking sort order frequently.
*   Option to schedule Do Today tasks directly onto the calendar for mobile-only days.

#### Extreme TRO (XTRO)

*   For highly overwhelming workloads.
*   **Key Changes:**
    *   Strict differentiation: **Must Do** (hard dates, processed) vs. **May Do** (soft dates only, often not processed) vs. **Someday/Maybe**.
    *   Use physical/digital "May Do" boxes/folders instead of processing these items into the main system.
    *   Skip Weekly and Monthly reviews (except during retreats).
    *   Heavy focus on delegation, strategic alignment, multipurposing, and agile execution.

#### Troubleshooting/Common Issues

*   Extensive list provided addressing common stress points (feeling stressed, tasks slipping, planning issues, etc.) with specific TRO-based diagnoses and prescriptions (e.g., "Trust the System," "Lifecycle of a Task," correct review habits, using contexts, processing correctly, managing interruptions).
*   Emphasizes contacting a coach for persistent issues or complex situations.
*   Addresses handling excessive workload (XTRO, hiring help, re-allocating time, discussing with management).

#### Benefits of Regular Reviews

*   **Efficiency:** Reviews remain short (5 mins daily/weekly) due to proactive processing.
*   **Control:** Daily load balancing prevents overwhelm.
*   **Clarity:** Start each day with a clear picture of priorities.
*   **Reliability:** Ensures important tasks don't slip through; neglected tasks are regularly revisited.
*   **Visibility:** Someday/Maybe items are tracked and periodically reviewed.
*   **Alignment:** Keeps the strategic calendar up-to-date and focused on goals.

## Synthesis for App Development

*   **Common Ground:** Capture, organization (tasks, projects, knowledge), linking daily actions to goals. GTD influence is notable.
*   **Notion Systems (UB & PPV):** Rely heavily on relational databases. The app needs native equivalents. Offer pre-built structures (P.A.R.A./PPV).
*   **TRO:** Focuses on workflow, control, simplicity, sustainability. Quick reviews, auto-follow-ups, prioritized daily views are key concepts. The "relaxed" aspect is a potential differentiator.
*   **Potential App Concepts:**
    *   Choose/develop an organizational philosophy (P.A.R.A., PPV, TRO-inspired, unique).
    *   Implement robust capture, task/project management, PKM, reviews, and goal alignment features.
    *   Prioritize seamless cloud sync and native mobile experience.
    *   Consider TRO's emphasis on ease of use and sustainability. 