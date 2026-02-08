class InsertError:
    """
    Represents a syntax or structural error in an insert SQL query.
    """

    def __init__(self, message: str, explanation: str, position: str = None):
        """
        Initializes an InsertError instance.

        :param message: A brief description of the error.
        :param explanation: A detailed explanation of why it is incorrect.
        :param position: Optional hint about where the error occurred in the query.
        """
        self.message = message
        self.explanation = explanation
        self.position = position

    def to_dict(self) -> dict:
        """
        Returns error details as a dictionary.
        """
        return {
            "message": self.message,
            "explanation": self.explanation,
            "position": self.position
        }
    
    def __str__(self) -> str:
        """
        Human readable error format for console output.
        """
        output = f"Error: {self.message}\nWhy: {self.explanation}"
        if self.position:
            output += f"\nWhere: {self.position}"
        return output