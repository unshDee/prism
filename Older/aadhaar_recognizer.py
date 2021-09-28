import re
from entity import Entity
from typing import List


class AadhaarRecognizer:

    """
    Recognizes Aadhaar Card numbers

    :param text: Pass string to check for emails
    """

    def __init__(self, text) -> None:
        self.text = text
        self.entityName = "AADHAAR_CARD"
        self.entityList = []

    def getRegex(self) -> None:

        regex = r"[2-9]{1}[0-9]{3}\s?[0-9]{4}\s?[0-9]{4}\s"
        pattern = re.compile(regex)

        matches = re.findall(pattern, self.text)

        for match in matches:
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                sensitivityScore=0.9,
                country="INDIA"
            )
            self.entityList.append(entity)

    @staticmethod
    def validate() -> None:
        pass

    def getEntity(self) -> List:
        self.getRegex()
        self.validate()
        return self.entityList


sample = AadhaarRecognizer(
    text="Input: str = 367598346012 Output: true Explanation:  The given string satisfies all the above mentioned conditions. Therefore, it is a valid Aadhar number. Input: str = 3675983460128  Output: false  Explanation:  The given string contains 13 digits. Therefore, it is not a valid Aadhar number. "
)

# print(emails.getEntity())
# for ent in sample.getEntity():
#     print(ent.returnDict())
