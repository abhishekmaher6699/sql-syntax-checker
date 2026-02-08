"""
Error messages for REVOKE validation.
"""
# Called when query does not contain enough parts
def incomplete_query():
    return "Error: Incomplete REVOKE query."


 # Called when required keyword is missing
def missing_clause(clause):
    return (
        f"Error: Missing '{clause}' clause.\n"
        "Expected format: REVOKE privilege ON table FROM user;"
    )
