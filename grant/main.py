from parser import parse_query
from grant_validator import grant_validator

query = input("Enter GRANT query: ")

# Parse the query and get keyword and tokens
keyword, tokens = parse_query(query)

if keyword == "GRANT":
    # Parse the query and get keyword and tokens
    print(grant_validator(tokens))
else:
    print("Invalid GRANT query.")
