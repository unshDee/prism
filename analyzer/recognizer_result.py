from typing import Dict



class RecognizerResult:
    """
    Recognizer Results detects the findings of the detected entities.
    
    :param entity_type: the type of the entity
    :param start: the start location of the detected entity
    :param end: the end location of the detected entity
    :param score: the score of the detection
    """
    
    def __init__(
        self,
        entity_type: str,
        start: int,
        end: int,
        score: float,
    ):

        self.entity_type = entity_type
        self.start = start
        self.end = end
        self.score = score

    def to_dict(self) -> Dict:
        """
        Convert instance to dictionary.
        
        :return: a dictionary
        """
        
        return self.__dict__