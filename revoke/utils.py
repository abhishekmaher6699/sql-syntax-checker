"""
Utility helper functions used revoke module.
"""

def tokenize(query: str):
    """ 
      Split query into tokens.
    """

     # Remove spaces and semicolon
    query = query.strip().rstrip(";")
   
     # Split query into list of words
    return query.split()
