import re
import phonenumbers
from phonenumbers import NumberParseError
from validate_email import validate_email as real_email_validation
from enum import Enum


class Gender(Enum):
    FEMALE = "زن"
    MALE = "مرد"
    OTHER = "سایر موارد"


class Religion(Enum):
    ISLAM = "اسلام"
    CHRISTIANITY = "مسیحیت"
    JUDAISM = "یهودیت"
    OTHER = "سایر موارد"


class Education(Enum):
    ILLITERATE = "کم سواد"
    PRIMARY = "سیکل"
    HIGH_SCHOOL = "دیپلم"
    ASSOCIATE = "کاردانی"
    BACHELOR = "کارشناسی"
    MASTER = "کارشناسی ارشد"
    PHD = "دکتری"


def validate_email(email: str, verify: bool = False) -> bool:
    """Validate email address format and optionally verify its existence."""
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        return False
    if verify:
        return real_email_validation(email, verify=True, check_mx=True, smtp_timeout=10)
    return True


def validate_phone_number(phone: str, region: str = "IR") -> bool:
    """Validate phone number using phonenumbers library."""
    try:
        parsed_number = phonenumbers.parse(phone, region)
        return phonenumbers.is_valid_number(parsed_number)
    except NumberParseError:
        return False


def validate_iran_national_id(national_id: str) -> bool:
    """Validate Iranian National ID (10 digits, with checksum validation)."""
    if not national_id.isdigit() or len(national_id) != 10:
        return False

    # Check for invalid same-digit patterns (e.g., 1111111111)
    if len(set(national_id)) == 1:
        return False

    # Calculate checksum
    total = 0
    for i in range(9):
        total += int(national_id[i]) * (10 - i)
    remainder = total % 11
    check_digit = int(national_id[9])

    if remainder < 2:
        return check_digit == remainder
    return check_digit == 11 - remainder


def validate_age(age: int) -> bool:
    """Validate age is an integer and not more than 110."""
    return isinstance(age, int) and 0 <= age <= 110
