import re
import spacy
from entity_recognizer.entity import Entity
from typing import List

nlp = spacy.load("en_core_web_sm")

class DrivingLicenseRecognizer:

    """
    Recognizes aadhaar card numbers.

    :param text: Text string to check for aadhaar card numbers
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "IN_DRIVING_LICENSE"
        self.entityList = []

    def __analyze(self) -> None:

        regex = r"(AN|AP|AR|AS|BR|CH|DN|DD|DL|GA|GJ|HR|HP|JK|KA|KL|LD|MP|MH|MN|ML|MZ|NL|OR|PY|PN|RJ|SK|TN|TR|UP|WB)[0-9]{2}((19|20)[0-9][0-9])[0-9]{7}$"
        pattern = re.compile(regex)

        matches = []
        doc = nlp(self.text)
        for token in doc:
            res = re.match(pattern, token.text)
            if res:
                matches.append(token.text)

        for match in matches:
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
