from typing import Dict

class Entity:

    def __init__(self, text = "NO_TEXT", label = "UNKNOWN", start = 0, end = 0, sensitivityScore = 0.0, country = "GENERIC") -> None:
        self.text = text
        self.label = label
        self.span = [start, end]
        self.sensitivityScore = sensitivityScore
        self.country = country
        
    def returnDict(self) -> Dict  :
      returnDict = {
        "text": self.text,
        "label": self.label,
        "span": self.span,
        "sensitivityScore": self.sensitivityScore,
        "country": self.country
      }
      return returnDict