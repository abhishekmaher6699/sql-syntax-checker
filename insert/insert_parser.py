import re

def parse_insert(query: str) -> dict:
    """
    Parses a raw INSERT SQL query and extracts the table name, columns (if provided), and values.
    """

    parsed = {
        "raw": query,
        "table": None,
        "columns": [],
        "values": []
    }

    if not query or not isinstance(query, str):
        return parsed
    
    # Clean up the query
    query = query.strip().rstrip(';')
    upper_query = query.upper()

    # Find VALUES keyword
    values_index = upper_query.find(" VALUES ")

    if values_index == -1:
        return parsed  # Invalid query, no VALUES found
    
    left_part = query[:values_index].strip()
    right_part = query[values_index + len(" VALUES "):].strip()

    # Table name
    left_tokens = left_part.split()

    if "INTO" in [t.upper() for t in left_tokens]:
        into_index = [t.upper() for t in left_tokens].index("INTO")
        if into_index + 1 < len(left_tokens):
            parsed["table"] = left_tokens[into_index + 1]

    # Columns (if provided)
    if "(" in left_part and ")" in left_part:
        start = left_part.find("(")
        end = left_part.find(")")
        column_section = left_part[start + 1:end]
        parsed["columns"] = [col.strip() for col in column_section.split(",") if col.strip()]
    
    # Values
    rows = []
    current = ""
    inside_parens = False

    for char in right_part:
        if char == '(':
            inside_parens = True
            current = ""
        elif char == ')':
            inside_parens = False
            rows.append(current)
        elif inside_parens:
            current += char
        
    for row in rows:
        values = [val.strip() for val in row.split(",")]
        parsed["values"].append(values)
    
    return parsed