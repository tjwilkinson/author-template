# Branch Tracking

This file maintains a record of all branches in the repository, their purpose, associated authors, and status.

## Active Branches

| Branch Name | Purpose | Author | Created | Last Updated | Status |
|-------------|---------|--------|---------|-------------|--------|
| main | Template branch - contains template files only | System | 2023-04-08 | 2023-04-08 | Active |

## Archived Branches

| Branch Name | Purpose | Author | Created | Last Updated | Archived Date | Final Status |
|-------------|---------|--------|---------|-------------|--------------|--------------|
| *No archived branches* | | | | | | |

## Branch Management Instructions

### When Creating New Branches

When a new branch is created, add an entry to the Active Branches table with:
- Branch name (should follow convention: `universe-<name>` for writing branches)
- Purpose (brief description of the branch's content)
- Author (the author associated with the branch)
- Creation date
- Last updated date (initially same as creation date)
- Status (Active)

Example:
```
| universe-fantasy | Fantasy novel series | Jane Doe | 2023-04-09 | 2023-04-09 | Active |
```

### When Updating Branches

When significant changes are made to a branch:
- Update the "Last Updated" field with the current date

### When Archiving Branches

When a branch is no longer needed:
- Move its entry from "Active Branches" to "Archived Branches"
- Add an "Archived Date" field
- Update the "Final Status" field (Completed, Abandoned, Merged, etc.)

### When Deleting Branches

When a branch is deleted:
- If it was never pushed to remote, you may remove its entry entirely
- If it was pushed to remote at any point, move it to Archived Branches and mark status as "Deleted" 