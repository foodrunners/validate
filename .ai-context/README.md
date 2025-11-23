# AI Context - Read This First

**Purpose**: This folder contains essential context for AI assistants working on this project.

## Start Here

If you're an AI being asked to work on this codebase, **read these files in order**:

1. **[project_context.md](./project_context.md)** - MUST READ FIRST
   - Complete history of what was explored
   - Honest assessment of decisions made
   - Mistakes and lessons learned
   - What was NOT considered
   - Current state and recommendations

2. **[repository_overview.md](./repository_overview.md)**
   - How the `validate` tool works
   - Architecture and components
   - Key directories and files

3. **[existing_capabilities.md](./existing_capabilities.md)**
   - What the tool CAN already do
   - Existing validation features
   - Before adding new features, check here first

## Key Takeaways for AIs

### Before Implementing Anything

1. ✅ Check if functionality already exists
2. ✅ Understand the domain requirements (IFC, BIM standards)
3. ✅ Ask for real data/examples before making assumptions
4. ✅ Read existing rules in `features/rules/` for patterns

### User's Core Goal

> "I want confident validation - if it says wrong, it must be wrong; if right, it must be right"

This requires:
- Domain knowledge (IFC standards, building codes)
- Real test data from user's workflow
- Clear requirements, not technical assumptions
- Using existing proven patterns

### What NOT to Do

- ❌ Jump to implementation without checking existing code
- ❌ Add redundant features
- ❌ Make assumptions about IFC property formats
- ❌ Focus on technical solutions over domain understanding

## Quick Reference

| Task | File to Check |
|------|---------------|
| Add validation rule | `how_to_add_rule.md` |
| Understand architecture | `repository_overview.md` |
| Full project context | `project_context.md` |
| See what exists | `existing_capabilities.md` |

## Current State (as of 2024-11-23)

- Local setup working (SQLite, no Docker)
- Backend server running on port 8000
- Custom client script: `custom_client.py`
- **Decision pending**: Whether to keep or remove redundant regex THEN step

## Next Steps for Monday

1. Get real IFC files from user's workflow
2. Examine actual FireRating property values
3. Define specific validation requirements
4. Check if pset_definitions.csv already covers it
5. Use existing GIVEN regex step (not redundant THEN step)
