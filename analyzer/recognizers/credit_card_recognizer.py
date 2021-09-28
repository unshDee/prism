from typing import List, Tuple, Optional

from analyzer import Pattern, PatternRecognizer


class CreditCardRecognizer(PatternRecognizer):
    """
    Recognize email address using regex.

    :param patterns: List of patterns to be used by the recognizer
    :param entity_name: The name of entity which can be detected
    """

    PATTERNS = [
        Pattern(
            "All Credit Cards (weak)",
            r"\b((4\d{3})|(5[0-5]\d{2})|(6\d{3})|(1\d{3})|(3\d{3}))[- ]?(\d{3,4})[- ]?(\d{3,4})[- ]?(\d{3,5})\b",
            0.3
        )
    ]
    
    CONTEXT = [
        "credit",
        "visa",
        "mastercard",
        "amex",
        "maestro",
        "diners",
        "discover",
        "jcb",
        "cc",
        "instapayment",
        "rupay",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        entity_name: str = "CREDIT_CARD"
    ):
        self.replacement_pairs = [("-", ""), (" ", "")]
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            patterns=patterns,
            entity_name=entity_name,
        )
        
    def validate(self, pattern_text: str) -> bool:
        cleaned_value =  self.__clean_value(pattern_text, self.replacement_pairs)
        checksum = self.__luhn_checksum(cleaned_value)
        return checksum
    
    @staticmethod 
    def __luhn_checksum(cleaned_value: str) -> bool:
        def digits_of(n: str) -> List[int]:
            return [int(digit) for digit in n]
        
        digits = digits_of(cleaned_value)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(str(digit * 2)))
        return checksum % 10 == 0
    
    @staticmethod
    def __clean_value(text: str, replacement_pairs: List[Tuple[str, str]]) -> str:
        for search, replace in replacement_pairs:
            text = text.replace(search, replace)
        return text