from entity import Entity
from typing import List

class Recognizer:

    """
    Base class for recognizers

    :param text: Text string containing sample input
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "LABEL NAME"
        self.entityList = []

    def __analyze(self) -> None:
        pass
    
    def __validate() -> None:
        pass

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList
