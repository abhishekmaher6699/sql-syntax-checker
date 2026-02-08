"""
Validate REVOKE SQL syntax.
Format:
REVOKE privilege ON table FROM user
"""

from errors import *
from suggestion import *

def validate_revoke(tokens):
# Step 1: Check if query is complete
    if len(tokens) < 6:
        return incomplete_query("REVOKE")

 # Step 2: Check if ON keyword exists
    if "ON" not in tokens:
        return missing_clause(
            "ON",
            "REVOKE privilege ON table FROM user;"
        )

# Step 3: Check if TO keyword exists
    if "FROM" not in tokens:
        return missing_clause(
            "FROM",
            "REVOKE privilege ON table FROM user;"
        )

 # Step 4: Get privilege, table name, and user
    privilege = tokens[1]
    table = tokens[tokens.index("ON") + 1]
    user = tokens[tokens.index("FROM") + 1]

    result = (
        "Query Structure Valid.\n"
        f"Revoked Privilege: {privilege}\n"
        f"Table: {table}\n"
        f"User: {user}"
    )

    result += revoke_fix(privilege, table, user)

    return result
