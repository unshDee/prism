"""Indian recognizers package, holds all recognizers related to India"""

from .aadhaar_card_recognizer import AadhaarRecognizer
from .driving_license_recognizer import DrivingLicenseRecognizer

__all__ = [
    "AadhaarRecognizer",
    "DrivingLicenseRecognizer"
]