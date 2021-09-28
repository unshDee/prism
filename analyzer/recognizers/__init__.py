"""Recognizers package. Holds all recognizers."""

from .credit_card_recognizer import CreditCardRecognizer
from .email_recognizer import EmailRecognizer
from .in_aadhaar_card_recognizer import InAadhaarCardRecognizer
from .in_driver_license_recognizer import InDriverLicense
from .ip_recognizer import IpRecognizer
from .spacy_recognizer import SpacyRecognizer
from .us_ssn_recognizer import UsSsnRecognizer

__all__ = [
    "CreditCardRecognizer",
    "EmailRecognizer",
    "InAadhaarCardRecognizer",
    "InDriverLicense",
    "IpRecognizer",
    "SpacyRecognizer",
    "UsSsnRecognizer",
]