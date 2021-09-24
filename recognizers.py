"""Gets all detected entities from various recognizers."""

from typing import List
from entity_recognizer.generic_recognizer import *


def recognizers(sample: str, country: str = "GENERIC") -> List:
    """
    :param sample: Text string to ceh
    """
    recognizedEntities = []
    recognizedEntities.append(PersonRecognizer(sample).getEntity())
    recognizedEntities.append(EmailRecognizer(sample).getEntity())
    recognizedEntities.append(OrganizationRecognizer(sample).getEntity())
    recognizedEntities.append(CreditCardRecognizer(sample).getEntity())
    if country == "INDIA":
        import entity_recognizer.country_recognizer.ind as ind
        recognizedEntities.append(ind.AadhaarRecognizer(sample).getEntity())
        recognizedEntities.append(ind.DrivingLicenseRecognizer(sample).getEntity())
    if country == "USA":
        import entity_recognizer.country_recognizer.usa as usa
        recognizedEntities.append(usa.SSNRecognizer(sample).getEntity())
    
    return recognizedEntities