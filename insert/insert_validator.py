from insert.insert_errors import InsertError

def validate_insert(parsed: dict) -> list:
    """
    Validates the structure of an INSERT SQL query.
    Returns a list of InsertError objects.
    """

    errors = []

    raw_query = parsed.get("raw", "")
    if not raw_query or not isinstance(raw_query, str):
        errors.append(
            InsertError(
                message="Empty or invalid query.",
                explanation="INSERT query cannot be empty."
            )
        )
        return errors

    upper_query = raw_query.upper()

    # ---------- Edge case: Missing space between INSERT and INTO ----------
    if "INSERTINTO" in upper_query:
        errors.append(
            InsertError(
                message="Missing space between INSERT and INTO.",
                explanation="SQL keywords must be separated by spaces. "
                            "Use 'INSERT INTO' instead of 'INSERTINTO'.",
                position="Start of query"
            )
        )
        return errors

    # ---------- Rule 1: Must start with INSERT ----------
    if not upper_query.strip().startswith("INSERT"):
        errors.append(
            InsertError(
                message="Query does not start with INSERT.",
                explanation="INSERT statements must begin with the INSERT keyword.",
                position="Start of query"
            )
        )
        return errors  # no point checking further

    # ---------- Rule 2: INTO keyword ----------
    if "INTO" not in upper_query:
        errors.append(
            InsertError(
                message="Missing INTO keyword.",
                explanation="INSERT statements must use INSERT INTO <table_name>.",
                position="After INSERT"
            )
        )

    # ---------- Rule 3: Table name ----------
    if parsed.get("has_into") and not parsed.get("table"):
        errors.append(
            InsertError(
                message="Missing table name.",
                explanation="INSERT requires a target table after the INTO keyword.",
                position="After INTO"
            )
        )

    # ---------- Rule 4: VALUES keyword ----------
    if "VALUES" not in upper_query:
        errors.append(
            InsertError(
                message="Missing VALUES clause.",
                explanation="INSERT statements must specify VALUES to be inserted.",
                position="After table name"
            )
        )
        return errors

    # ---------- Rule 5: VALUES parentheses ----------
    if not parsed.get("values"):
        errors.append(
            InsertError(
                message="VALUES clause is incorrectly formatted.",
                explanation="VALUES must be followed by one or more parenthesized value lists.",
                position="VALUES clause"
            )
        )
        return errors

    # ---------- Rule 6: Column–value count mismatch ----------
    columns = parsed.get("columns", [])
    values = parsed.get("values", [])

    if columns:
        column_count = len(columns)

        for row in values:
            if len(row) != column_count:
                errors.append(
                    InsertError(
                        message="Column-value count mismatch.",
                        explanation=(
                            f"{column_count} columns specified but "
                            f"{len(row)} values provided."
                        ),
                        position="VALUES clause"
                    )
                )
                break

    # ---------- Rule 7: Empty VALUES ----------
    for row in values:
        if all(val == "" for val in row):
            errors.append(
                InsertError(
                    message="Empty VALUES list.",
                    explanation="VALUES clause cannot be empty.",
                    position="VALUES clause"
                )
            )
            break

    return errors
