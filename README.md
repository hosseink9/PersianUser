# PersianUser

A Python library for creating and validating Persian user information, including email, phone number, Iranian national ID, and additional optional fields.

## Installation
```bash
pip install persianuser
```

## Requirements
- Python >= 3.8
- phonenumbers>=8.12.0
- py3-validate-email>=1.0.6

## Usage
```python
from persianuser import User

# Create a user with required and optional fields, with real email validation
try:
    user = User(
        username="ali_rezaei",
        email="ali.rezaei@example.com",
        phone="+989123456789",
        national_id="0060374689",
        age=30,
        address="Tehran, Iran",
        description="A software developer",
        gender="مرد",
        religion="اسلام",
        education="کارشناسی",
        verify_email=True
    )
    print(f"User created: {user.username}, {user.email}, {user.phone}, {user.national_id}, "
          f"Age: {user.age}, Address: {user.address}, Description: {user.description}, "
          f"Gender: {user.gender}, Religion: {user.religion}, Education: {user.education}")
except ValueError as e:
    print(f"Error: {e}")

# Extend the User class
class CustomUser(User):
    def __init__(self, username, email, phone, national_id, extra_field, age=None, address=None, description=None, gender=None, religion=None, education=None, verify_email=False):
        super().__init__(username, email, phone, national_id, age, address, description, gender, religion, education, verify_email)
        self.extra_field = extra_field
```

## Features
- Email validation (format and optional real email verification)
- Phone number validation (using phonenumbers library)
- Iranian national ID validation
- Optional fields: age, address, description, gender, religion, education
- Gender options: زن, مرد, سایر موارد
- Religion options: اسلام, مسیحیت, یهودیت, سایر موارد
- Education options: کم سواد, سیکل, دیپلم, کاردانی, کارشناسی, کارشناسی ارشد, دکتری
- Easy-to-use class with inheritance support

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.