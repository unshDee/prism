"""Generic recognizers package, holds all the default generic recognizers."""

from .credit_card_recognizer import CreditCardRecognizer
from .email_recognizer import EmailRecognizer
from .organization_recognizer import OrganizationRecognizer
from .person_recognizer import PersonRecognizer

__all__ = [
    "CreditCardRecognizer",
    "EmailRecognizer",
    "OrganizationRecognizer",
    "PersonRecognizer"
]