from typing import List, Optional

from analyzer import Pattern, PatternRecognizer


class EmailRecognizer(PatternRecognizer):
    """
    Recognize email address using regex.

    :param patterns: List of patterns to be used by the recognizer
    :param entity_name: The name of entity which can be detected
    """

    PATTERN = [
        Pattern(
            "Email",
            r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b",
            0.5,
        ),
    ]
    
    CONTEXT = [
        "email",
        "gmail",
        "yahoo",
        "mail",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        entity_name: str = "EMAIL_ADDRESS"
    ):
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            patterns=patterns,
            entity_name=entity_name,
        )
