from typing import Optional
from .validators import (
    validate_email,
    validate_phone_number,
    validate_iran_national_id,
    validate_age,
)
from .validators import Gender, Religion, Education


class PersianUser:
    """Base class for creating and validating a Persian user."""

    def __init__(
        self,
        username: str,
        email: str,
        phone: str,
        national_id: str,
        age: Optional[int] = None,
        address: Optional[str] = None,
        description: Optional[str] = None,
        gender: Optional[str] = None,
        religion: Optional[str] = None,
        education: Optional[str] = None,
        verify_email: bool = False,
    ):
        self._username = None
        self._email = None
        self._phone = None
        self._national_id = None
        self._age = None
        self._address = None
        self._description = None
        self._gender = None
        self._religion = None
        self._education = None

        self.set_username(username)
        self.set_email(email, verify_email)
        self.set_phone(phone)
        self.set_national_id(national_id)
        self.set_age(age)
        self.set_address(address)
        self.set_description(description)
        self.set_gender(gender)
        self.set_religion(religion)
        self.set_education(education)

    def set_username(self, username: str) -> None:
        """Set username with basic validation."""
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        self._username = username

    def set_email(self, email: str, verify: bool = False) -> None:
        """Set and validate email, optionally verifying its existence."""
        if not validate_email(email, verify=verify):
            raise ValueError("Invalid email format or email does not exist.")
        self._email = email

    def set_phone(self, phone: str) -> None:
        """Set and validate phone number."""
        if not validate_phone_number(phone):
            raise ValueError("Invalid phone number.")
        self._phone = phone

    def set_national_id(self, national_id: str) -> None:
        """Set and validate Iranian national ID."""
        if not validate_iran_national_id(national_id):
            raise ValueError("Invalid Iranian national ID.")
        self._national_id = national_id

    def set_age(self, age: Optional[int]) -> None:
        """Set and validate age."""
        if age is not None and not validate_age(age):
            raise ValueError("Age must be an integer between 0 and 110.")
        self._age = age

    def set_address(self, address: Optional[str]) -> None:
        """Set address."""
        self._address = address

    def set_description(self, description: Optional[str]) -> None:
        """Set description."""
        self._description = description

    def set_gender(self, gender: Optional[str]) -> None:
        """Set and validate gender."""
        if gender is not None:
            try:
                self._gender = Gender(gender).value
            except ValueError:
                raise ValueError("Gender must be one of: زن, مرد, سایر موارد")

    def set_religion(self, religion: Optional[str]) -> None:
        """Set and validate religion."""
        if religion is not None:
            try:
                self._religion = Religion(religion).value
            except ValueError:
                raise ValueError(
                    "Religion must be one of: اسلام, مسیحیت, یهودیت, سایر موارد"
                )

    def set_education(self, education: Optional[str]) -> None:
        """Set and validate education."""
        if education is not None:
            try:
                self._education = Education(education).value
            except ValueError:
                raise ValueError(
                    "Education must be one of: کم سواد, سیکل, دیپلم, کاردانی, کارشناسی, کارشناسی ارشد, دکتری"
                )

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def national_id(self) -> str:
        return self._national_id

    @property
    def age(self) -> Optional[int]:
        return self._age

    @property
    def address(self) -> Optional[str]:
        return self._address

    @property
    def description(self) -> Optional[str]:
        return self._description

    @property
    def gender(self) -> Optional[str]:
        return self._gender

    @property
    def religion(self) -> Optional[str]:
        return self._religion

    @property
    def education(self) -> Optional[str]:
        return self._education
