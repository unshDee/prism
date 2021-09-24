import re
from entity_recognizer.entity import Entity
from typing import List

class AadhaarRecognizer:

    """
    Recognizes aadhaar card numbers.

    :param text: Text string to check for aadhaar card numbers
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "IN_AADHAAR_CARD"
        self.entityList = []

    def __analyze(self) -> None:

        regex = r"\D[2-9]{1}[0-9]{3}\s?[0-9]{4}\s?[0-9]{4}(?:\s+|\W|$)"
        pattern = re.compile(regex)

        matches = re.findall(pattern, self.text)

        for match in matches:
            match = match.strip()
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                sensitivityScore=0.9,
                entityType="INDIA"
            )
            self.entityList.append(entity)

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList
