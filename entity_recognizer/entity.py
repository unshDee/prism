import json
from typing import Dict

class Entity:
    """
    A class that represents entity data.
    
    :param text: String value which is recognized as an entity
    :param label: Type of entity recognized
    :param start: Start index of recognized entity in string
    :param end: End index of recognized entity in string
    :param sensitivityScore: Sensitivity score of entity (values varies 0 to 1)
    :param entityType: Entity's category (generic or other)
    """

    def __init__(
        self,
        text: str = "NO_TEXT",
        label: str = "UNKNOWN",
        start: int = 0,
        end: int = 0,
        sensitivityScore: float = 0.0,
        entityType: str = "GENERIC"
    ):
        self.text = text
        self.label = label
        self.span = [start, end]
        self.sensitivityScore = sensitivityScore
        self.entityType = entityType

    def to_dict(self) -> Dict:
        """
        Turn this instance into a dictionary.
        
        :return: a dictionary
        """
        returnDict = {
            "text": self.text,
            "label": self.label,
            "span": self.span,
            "sensitivityScore": self.sensitivityScore,
            "entityType": self.entityType
        }
        return returnDict

    @classmethod
    def from_dict(cls, entity_dict: Dict) -> "Entity":
        """
        Load Entity instance from dictionary.

        :param entity_dict: a dictionary holding the entity's parameters
        :return: an Entity instance
        """
        return cls(**entity_dict)

    def __repr__(self):
        """Return string representation of instance."""
        return json.dumps(self.to_dict())