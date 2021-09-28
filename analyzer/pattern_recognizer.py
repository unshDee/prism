from typing import Dict, List, Optional

import re

from analyzer import (
    Pattern,
    RecognizerResult
)

class PatternRecognizer:
    """
    PII entity recognizer using regular expressions.
    
    :param patterns: A list of patterns to detect
    """
    
    def __init__(self, patterns: List[Pattern]):
        if patterns is None:
            patterns = []
        else:
            self.patterns = patterns
    
    def analyze(
        self,
        text: str,
        
    ) -> List[RecognizerResult]:
        if self.patterns:
            pattern_result = self.__analyze_patterns(text)
            
    def validate(self, pattern_text: str) -> Optional[bool]:
        
        return None
    
    def invalidate(self, pattern_text: str) -> Optional[bool]:
        
        return None
            
    def __analyze_patterns(self, text: str):
        
        for pattern in self.pattern:
            matches = re.finditer(pattern.regex, text)
            for match in matches:
                start, end = match.span()
                text_match = text[start:end]
                
                # Skip empty results
                if text_match == "":
                    continue
                
                score = pattern.score
                
                validation = self.validate(text_match)
                pattern_result = RecognizerResult()
                