import re
from entity import Entity
from typing import List


class EmailRecognizer:

    """
    Recognizes email IDs

    :param text: Pass string to check for emails
    """

    def __init__(self, text) -> None:
        self.text = text
        self.entityName = "EMAIL"
        self.entityList = []

    def getRegex(self) -> None:

        regex = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        pattern = re.compile(regex)

        matches = re.findall(pattern, self.text)

        for match in matches:
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                score=0.5
            )
            self.entityList.append(entity)

    @staticmethod
    def validate() -> None:
        pass

    def getEntity(self) -> List:
        self.getRegex()
        self.validate()
        return self.entityList


sample = EmailRecognizer(
    text="This is my email address person_name@email.com and this is my friend's email: friend_of_person@friend.com"
)

# for ent in sample.getEntity():
#     print(ent.returnDict())
