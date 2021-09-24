import re
from entity_recognizer.entity import Entity
from typing import List

class SSNRecognizer:

    """
    Recognizes social security numbers (SSNs).

    :param text: Text string to check for SSNs
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "US_SSN"
        self.entityList = []

    def __analyze(self) -> None:

        regex = r"(?!0{3})(?!6{3})[0-8]\d{2}-(?!0{2})\d{2}-(?!0{4})\d{4}"
        pattern = re.compile(regex)

        matches = re.findall(pattern, self.text)

        for match in matches:
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                sensitivityScore=1.0,
                entityType="USA"
            )
            self.entityList.append(entity)

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList
