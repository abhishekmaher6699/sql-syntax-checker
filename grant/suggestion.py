"""
Suggestions for correcting GRANT queries.
"""

def grant_fix(privilege, table, user):
    # Suggest corrected GRANT query.

    return (
        "\nSuggested Fix:\n"
        f"GRANT {privilege} ON {table} TO {user};"
)
