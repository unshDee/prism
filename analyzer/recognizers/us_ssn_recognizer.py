from typing import List, Optional

from analyzer import Pattern, PatternRecognizer


class UsSsnRecognizer(PatternRecognizer):
    """
    Recognize US Social Security Number (SSN) using regex.

    :param patterns: List of patterns to be used by the recognizer
    :param entity_name: The name of entity which can be detected
    """

    PATTERN = [
        Pattern("SSN1", r"\b([0-9]{5})-([0-9]{4})\b", 0.05),
        Pattern("SSN2", r"\b([0-9]{3})-([0-9]{6})\b", 0.05),
        Pattern("SSN3", r"\b([0-9]{9})\b", 0.1),
        Pattern("SSN4", r"\b([0-9]{3})-([0-9]{2})-([0-9]{4})\b", 0.1),
        Pattern("SSN5", r"\b([0-9]{3})[- .]([0-9]{2})[- .]([0-9]{4})\b", 0.5)
    ]
    
    CONTEXT = [
        "social",
        "security",
        "ssn",
        "ssns",
        "ssn#",
        "ss#",
        "ssid",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        entity_name: str = "US_SSN"
    ):
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            patterns=patterns,
            entity_name=entity_name,
        )

    def invalidate(self, pattern_text: str):
        """
        Check if the pattern text cannot be validated as a US_SSN entity.

        :param pattern_text: Text detected as pattern by regex
        :return: True if invalidated
        """
        # check if all separators are of same type
        separator_type = {}
        for separator in pattern_text:
            if separator in (".", "-", " "):
                separator_type[separator] = True
        if len(separator_type.keys()) > 1:
            # separators not matching
            return True
        
        digits = "".join(digit for digit in pattern_text if digit.isdigit())
        
        if all(digits[0] == digit for digit in digits):
            # all digits cannot be same
            return True
        
        if digits[3:5] == "00" or digits[5:] == "0000":
            # groups cannot be zeroes only
            return True
        
        for invalid_ssn in ("000", "666", "123456789", "98765432", "9"):
            if digits.startswith(invalid_ssn):
                return True
            
        return False