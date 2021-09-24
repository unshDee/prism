import re
import spacy
from ..entity import Entity
from typing import List

nlp = spacy.load("en_core_web_sm")

class CreditCardRecognizer:

    """
    Recognizes credit card numbers.

    :param text: Text string to check for credit card numbers
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "CREDIT_CARD"
        self.entityList = []

    def __analyze(self) -> None:

        regex = r"(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)"
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
                sensitivityScore=1.0,
            )
            self.entityList.append(entity)

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList
