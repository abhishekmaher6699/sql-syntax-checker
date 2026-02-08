"""
Utility helper functions used grant module.
"""

 # Split query into tokens.
def tokenize(query: str) :

# Removes semicolon and trims spaces.
    query=query.strip().rstrip(";")

# Split query into list of words
    return query.split()
