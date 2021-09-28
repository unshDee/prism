from typing import List, Optional

from analyzer import Pattern, PatternRecognizer


class InDriverLicense(PatternRecognizer):
    """
    Recognize IN driver license using regex.

    :param patterns: List of patterns to be used by the recognizer
    :param entity_name: The name of entity which can be detected
    """

    PATTERN = [
        Pattern(
            "Driver License",
            r"\b\b",
            0.5,
        ),
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        entity_name: str = "IN_DRIVER_LICENSE"
    ):
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            patterns=patterns,
            entity_name=entity_name,
        )

    def invalidate(self, pattern_text: str) -> bool:
        """
        Check if the pattern text cannot be validated as a IN_AADHAAR_CARD entity.

        :param pattern_text: Text detected as pattern by regex
        :return: True if invalidated
        """
        pattern_text = pattern_text.replace(" ", "")

        if int(pattern_text[0]) in [0, 1]:
            # first digit cannot be 0 or 1
            return True

        return False
