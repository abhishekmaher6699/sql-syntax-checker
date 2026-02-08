def suggest_insert_fix(raw_query: str, parsed: dict, errors: list):
    """
    Generates a suggested corrected INSERT query
    when the fix is unambiguous.

    Returns a string or None.
    """

    if not errors:
        return None

    upper_query = raw_query.upper()

    # ---------- Missing INTO ----------
    for error in errors:
        if error.message == "Missing INTO keyword.":
            tokens = raw_query.split()
            if len(tokens) > 1:
                return f"INSERT INTO {' '.join(tokens[1:])}"

    # ---------- Missing VALUES ----------
    for error in errors:
        if error.message == "Missing VALUES clause.":
            table = parsed.get("table")
            if table:
                return f"INSERT INTO {table} VALUES (...);"

    # ---------- Incorrect VALUES formatting ----------
    for error in errors:
        if error.message == "VALUES clause is incorrectly formatted.":
            return "INSERT INTO <table_name> VALUES (...);"

    # ---------- Column-value mismatch (simple case) ----------
    for error in errors:
        if error.message == "Column-value count mismatch.":
            columns = parsed.get("columns")
            if columns:
                placeholders = ", ".join(["..."] * len(columns))
                return f"INSERT INTO {parsed.get('table')} ({', '.join(columns)}) VALUES ({placeholders});"

    return None