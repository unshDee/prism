import spacy
from entity import Entity
from typing import List

nlp = spacy.load("en_core_web_sm")


class PersonRecognizer:

    """
    Recognizes Person names

    :param text: Pass string to check for emails
    """

    def __init__(self, text) -> None:
        self.text = text
        self.entityName = "PERSON"
        self.entityList = []

    def getRegex(self) -> None:
        pass

    def getPerson(self) -> None:

        doc = nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entity = Entity(
                    text=ent.text,
                    label=self.entityName,
                    start=self.text.index(ent.text),
                    end=self.text.index(ent.text) + len(ent.text),
                    score=0.3
                )
                self.entityList.append(entity)

    @staticmethod
    def validate() -> None:
        pass

    def getEntity(self) -> List:
        self.getRegex()
        self.getPerson()
        self.validate()
        return self.entityList


# sample = PersonRecognizer(
#     text="NASA awarded Elon Musk SpaceX a $2.9 billion contract to build the lunar lander. Warren Edward Buffett is an American investor, business tycoon, philanthropist, and the chairman and CEO of Berkshire Hathaway."
# )

# # print(emails.getEntity())
# for ent in sample.getEntity():
#     print(ent.returnDict())
