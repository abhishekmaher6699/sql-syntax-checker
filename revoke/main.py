from parser import parse_query
from revoke_validator import validate_revoke

query = input("Enter REVOKE query: ")

# Parse the query and get keyword and tokens
keyword, tokens = parse_query(query)

if keyword == "REVOKE":
    # Parse the query and get keyword and tokens
    print(validate_revoke(tokens))
else:
    print("Invalid REVOKE query.")
