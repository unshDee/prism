import re
from entity import Entity
from typing import List


class IPRecognizer:

    """
    Recognizes IP addresses.

    :param text: Text string to check for IP addresses
    """

    def __init__(self, text) -> None:
        self.text = text
        self.entityName = "IP_ADDRESS"
        self.entityList = []

    def getRegex(self) -> None:

        regexIp6 = r"\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*"
        regexIp4 = r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
        
        pattern4 = re.compile(regexIp6)
        pattern6 =re.compile(regexIp4)

        matches = re.findall(pattern4, self.text) + re.findall(pattern6, self.text)
        for match in matches:
            entity = Entity(
                text=match,
                label=self.entityName,
                start=self.text.index(match),
                end=self.text.index(match) + len(match),
                sensitivityScore=0.9
            )
            self.entityList.append(entity)

    @staticmethod
    def validate() -> None:
        pass

    def getEntity(self) -> List:
        self.getRegex()
        self.validate()
        return self.entityList