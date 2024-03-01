"""file for define the exceptions in ragrank"""


class RagRankError(Exception):
    """Exception class for ragrank"""


class EvaluationError(RagRankError):
    """Evaluation Exception for ragrank"""

    def __init__(self, message: str = "Error during evaluation.") -> None:
        self.message = message
        super().__init__(self.message)
