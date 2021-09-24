import re
from ..entity import Entity
from typing import List

class EmailRecognizer:

    """
    Recognizes email addresses.

    :param text: Text string to check for emails
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "EMAIL"
        self.entityList = []

    def __analyze(self) -> None:

        regex = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        pattern = re.compile(regex)

        matches = re.findall(pattern, self.text)

        for match in matches:
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                sensitivityScore=float(0.5)
            )
            self.entityList.append(entity)

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList
