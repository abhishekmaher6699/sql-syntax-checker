"""
Error messages for GRANT validation.
"""

# Called when query does not contain enough parts
def incomplete_query():
    return "Error: Incomplete GRANT query."

 # Called when required keyword is missing
def missing_clause(clause):
    return (
        f"Error: Missing '{clause}' clause.\n"
        "Expected format: GRANT privilege ON table TO user;"
    )
