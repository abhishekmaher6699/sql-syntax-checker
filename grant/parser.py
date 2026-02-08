"""
Detect query type and route for validation.
"""

from utils import tokenize

def parse_query(query):
    tokens = tokenize(query)
    
     # If query is empty, return None
    if not tokens:
        return None, tokens
    
    # Return first word as query type (GRANT, REVOKE, etc.)
    # and the full token list
    return tokens[0].upper(), tokens
