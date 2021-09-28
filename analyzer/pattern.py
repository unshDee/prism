import json
from typing import Dict


class Pattern:
    """
    A class that represents a regex pattern.
    
    :param label: the label of pattern
    :param regex: the regex pattern to detect
    :param score: the strength of pattern (0.0 to 1.0)
    """

    def __init__(self, label: str, regex: str, score: float):
        
        self.label = label
        self.regex = regex
        self.score = score
        
    def to_dict(self) -> Dict:
        """
        Turns this instance into a dictionary.
        
        :return: dictionary
        """
        return {"label": self.label, "score": self.score, "regex": self.regex}
    
    def __str__(self):
        """Return string representation of instance."""
        return json.dumps(self.to_dict())