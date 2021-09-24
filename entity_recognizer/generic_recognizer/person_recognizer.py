import spacy
from ..entity import Entity
from typing import List

nlp = spacy.load("en_core_web_sm")

class PersonRecognizer:

    """
    Recognizes person names.

    :param text: Text string to check for person names
    """

    def __init__(self, text):
        self.text = text
        self.entityName = "PERSON"
        self.entityList = []

    def __analyze(self) -> None:
        doc = nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
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