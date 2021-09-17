from typing import Dict

class Entity:

    def __init__(self, text = "NO_TEXT", label = "UNKNOWN", start = 0, end = 0, score = 0.0) -> None:
        self.text = text
        self.label = label
        self.span = [start, end]
        self.score = score
        
    def returnDict(self) -> Dict  :
      returnDict = {
        "text": self.text,
        "label": self.label,
        "span": self.span,
        "score": self.score
      }
      return returnDict