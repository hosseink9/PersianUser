from user.validators import (
    validate_email,
    validate_phone_number,
    validate_iran_national_id,
    validate_age,
)
from user.validators import Gender, Religion, Education


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid.email") is False


def test_validate_phone_number():
    assert validate_phone_number("+989123456789") is True
    assert validate_phone_number("12345") is False


def test_validate_iran_national_id():
    assert validate_iran_national_id("1234567890") is False
    assert validate_iran_national_id("1111111111") is False
    assert validate_iran_national_id("0060374689") is True


def test_validate_age():
    assert validate_age(30) is True
    assert validate_age(111) is False
    assert validate_age(-1) is False
    assert validate_age(0) is True


def test_gender_enum():
    assert Gender.MALE.value == "مرد"
    assert Gender.FEMALE.value == "زن"
    assert Gender.OTHER.value == "سایر موارد"


def test_religion_enum():
    assert Religion.ISLAM.value == "اسلام"
    assert Religion.CHRISTIANITY.value == "مسیحیت"
    assert Religion.JUDAISM.value == "یهودیت"
    assert Religion.OTHER.value == "سایر موارد"


def test_education_enum():
    assert Education.ILLITERATE.value == "کم سواد"
    assert Education.PRIMARY.value == "سیکل"
    assert Education.HIGH_SCHOOL.value == "دیپلم"
    assert Education.ASSOCIATE.value == "کاردانی"
    assert Education.BACHELOR.value == "کارشناسی"
    assert Education.MASTER.value == "کارشناسی ارشد"
    assert Education.PHD.value == "دکتری"
