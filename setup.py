from setuptools import setup, find_packages

setup(
    name="persianuser",
    version="0.1.0",
    author="Hossein Kalantari",
    author_email="kalandevwork@gmail.com",
    description="A Python library for creating and validating Persian user information",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hosseink9/PersianUser",
    packages=find_packages(),
    install_requires=["phonenumbers>=8.12.0", "py3-validate-email>=1.0.5.post2"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
)
