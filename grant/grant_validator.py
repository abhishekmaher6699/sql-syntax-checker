"""
Validate GRANT SQL syntax.
Format:
GRANT privilege ON table TO user
"""

from errors import *
from suggestion import *

def grant_validator(tokens):
 
  # Step 1: Check if query is complete
    if len(tokens) < 6:
        return incomplete_query()

 # Step 2: Check if ON keyword exists
    if "ON" not in tokens:
        return missing_clause(
            "ON",
            "GRANT privilege ON table TO user;"
        )

# Step 3: Check if TO keyword exists
    if "TO" not in tokens:
        return missing_clause(
            "TO",
            "GRANT privilege ON table TO user;"
        )

 # Step 4: Get privilege, table name, and user
    privilege = tokens[1]
    table = tokens[tokens.index("ON") + 1]
    user = tokens[tokens.index("TO") + 1]

# Step 5: Show valid structure message
    result = (
        "Query Structure Valid.\n"
        f"Privilege: {privilege}\n"
        f"Table: {table}\n"
        f"User: {user}"
    )

    result += grant_fix(privilege, table, user)

    return result
