# Existing Capabilities - Check Before Adding Features

**Last Updated**: 2024-11-23

## Regex / Pattern Validation

### ✅ Already Exists

**Location**: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/features/steps/givens/attributes.py:37`

**Syntax**:
```gherkin
Given Its value {regex_condition} to the expression /{regex_pattern}/
```

**Supported Conditions**: `conforms`, `does not conform`, `must not conform`

**Example in Production** (PSE002):
```gherkin
Given An .IfcPropertySet.
Given Its attribute .Name.
Given Its value ^does not start^ with 'Pset_'
Then Its value must not conform to the expression /^[Pp][Ss][Ee][Tt]/
```

### How It Works
- Uses GIVEN step (semantically for filtering, but does validate)
- Yields ERROR on pattern mismatch
- Handles IfcOpenShell values via `attributes.condition_met()`
- Proven in production rules

### When to Use
For validating property values against regex patterns - **use this existing functionality** instead of creating new steps.

## Property Set Validation

### ✅ CSV-Based Validation Exists

**Location**: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/features/csvs/pset_definitions.csv`

**What It Does**:
- Validates property names against standard Psets
- Checks property data types (IfcLabel, IfcInteger, etc.)
- Verifies property associations with entity types

**Before creating custom property validation**:
1. Check if property is in `pset_definitions.csv`
2. Check if data type validation already covers your need
3. Review existing PSE001/PSE002 rules

## Standard Gherkin Steps

### Entity Selection
```gherkin
Given An .{EntityType}.          # Select all entities of type
Given {count:d} {EntityType}     # Expect specific count
```

### Attribute Navigation
```gherkin
Given Its attribute .{AttributeName}.              # Navigate to attribute
Given Its .{AttributeName}. attribute ^starts^ with '{value}'  # Filter by value
```

### Value Filtering
```gherkin
Given Its value ^starts^ with '{value}'
Given Its value ^does not start^ with '{value}'
Given Its value conforms to the expression /{regex}/
```

### Assertions (THEN steps)
```gherkin
Then The value must be '{value}'
Then The {value_or_type} must be in '{csv_file}.csv'
Then Its value must not conform to the expression /{regex}/
```

## CSV Definition Files

Located in: `backend/apps/ifc_validation/checks/ifc_gherkin_rules/features/csvs/`

- `pset_definitions.csv` - Standard property sets and properties
- `related_entity_attributes.csv` - Relationship attributes
- `relating_entity_attributes.csv` - Relationship attributes
- Various entity-specific CSVs

**Check these before assuming validation doesn't exist!**

## Utilities Available

### In `utils/attributes.py`
- `condition_met()` - String comparison with regex support

### In `utils/misc.py`  
- `strip_split()` - Parse multiple values
- `do_try()` - Safe attribute access
- `map_state()` - Handle nested structures

### In `utils/geometry.py`
- Geometric validation functions
- Precision comparison

## Common Patterns to Reuse

### Pattern 1: Property Value Validation
```gherkin
Given An .IfcPropertySingleValue.
Given Its .Name. attribute ^starts^ with 'PropertyName'
Given Its attribute .NominalValue.
Given Its value conforms to the expression /pattern/
```

### Pattern 2: Property Set Name Validation  
```gherkin
Given An .IfcPropertySet.
Given Its attribute .Name.
Then The value must be in 'pset_definitions.csv'
```

### Pattern 3: Entity Type Checks
```gherkin
Given An .{EntityType}.
Then The type of attribute {AttributeName} must be {ExpectedType}
```

## Before Adding New Features: Checklist

- [ ] Searched existing steps in `features/steps/`
- [ ] Checked CSV definitions in `features/csvs/`
- [ ] Reviewed similar rules in `features/rules/`
- [ ] Confirmed functionality doesn't exist
- [ ] Understood domain requirements (not just technical)
- [ ] Have real data examples to test against

## When Existing Functionality Is Sufficient

**Prefer existing over new** - even if syntax is less elegant. Reasons:
1. Already tested in production
2. No maintenance burden
3. Consistent with other rules
4. Team already knows how to use it

Only add new features when:
- Functionality genuinely doesn't exist
- Clear advantage over existing approach
- Willing to maintain additional code path
