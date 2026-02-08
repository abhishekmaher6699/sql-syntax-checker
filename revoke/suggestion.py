"""
Suggestions for correcting REVOKE queries.
"""

def revoke_fix(privilege, table, user):
   
    # Suggest corrected REVOKE query.
    return (
        "\nSuggested Fix:\n"
        f"REVOKE {privilege} ON {table} FROM {user};"
    )
