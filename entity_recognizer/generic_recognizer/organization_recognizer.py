import spacy
from ..entity import Entity
from typing import List

nlp = spacy.load("en_core_web_sm")

class OrganizationRecognizer:

    """
    Recognizes organization names.

    :param text: Text string to check for organizations
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "ORG"
        self.entityList = []

    def __analyze(self) -> None:

        doc = nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "ORG":
                entity = Entity(
                    text=ent.text,
                    label=self.entityName,
                    start=self.text.index(ent.text),
                    end=self.text.index(ent.text) + len(ent.text),
                    sensitivityScore=0.3
                )
                self.entityList.append(entity)

    def getEntity(self) -> List:
        self.__analyze()
        return self.entityList