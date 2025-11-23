# How to Add a New Validation Rule

The `validate` tool uses **Gherkin** (a plain-English language) to define rules and **Python** to implement the logic.

## 1. Where Rules Live
*   **Feature Files (The Rule)**: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/features/rules/`
    *   These files describe *what* to check.
*   **Step Definitions (The Logic)**: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/features/steps/`
    *   These Python files describe *how* to check it.

## 2. Example: Adding a "Wall Height" Rule
Let's say you want to enforce that **all walls must be taller than 2 meters**.

### Step A: Create the Feature File
Create a new file: `.../features/rules/MY_RULES/WALL001_Wall-Height.feature`

```gherkin
Feature: WALL001 - Wall Height Check
  All walls must be at least 2.0 meters high.

  Scenario: Verify Wall Height
    Given An IfcWall
    Then The value of attribute 'NominalHeight' must be greater than '2.0'
```

### Step B: Implement the Logic (If needed)
The tool already has many pre-defined steps (like checking attribute values), so you might not need to write any Python code!

For example, the step `The value of attribute '{attribute}' must be greater than '{value}'` is already implemented in `attributes.py`.

**If you need a custom check:**
1.  Open `.../features/steps/thens/attributes.py` (or create a new file).
2.  Add a Python function with the `@gherkin_ifc.step` decorator.

```python
@gherkin_ifc.step("The wall must be made of concrete")
def step_impl(context, inst):
    # 'inst' is the IFC entity (the Wall)
    material = get_material(inst) # pseudo-code
    if "Concrete" not in material.Name:
         yield ValidationOutcome(inst=inst, severity=OutcomeSeverity.ERROR)
```

## 3. Running Your Rule
Once added, the system automatically picks up the new `.feature` file.
1.  Restart the backend (if running locally).
2.  Upload a file.
3.  The report will now include `WALL001`.

## 4. Summary
*   **Simple Checks**: Just write a Gherkin feature file using existing steps (Attribute values, Property sets, etc.).
*   **Complex Checks**: Write a Gherkin feature file AND a Python step definition.
