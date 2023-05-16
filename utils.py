"""
This module is used for User module utilities.
"""

import re

from uuid import uuid4
from hashlib import sha256
from exceptions import *
from messages import Message


class Utils:
    """
    A class representing utility functions for the User module.
    """

    @staticmethod
    def id_generator() -> int:
        """
        Generate a unique id using the uuid4 module.

        :return: An integer representing the unique id.
        """
        return uuid4().int

    @staticmethod
    def check_password(password: str) -> str:
        """
        Hash the given password using the sha256 algorithm.

        :param password: A string representing the password to be hashed.
        :return: A string representing the hashed password.
        """

        if not Utils.is_valid_password(password):
            raise PasswordError(Message.WHAT_PASSWORD)
        return Utils.hashing_password(password)

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """
        Check whether the given password is valid or not.

        The password must meet the following requirements:
        - At least 4 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        - Contains at least one special character from the set @#$%^&+=!

        :param password: A string representing the password to be checked.
        :return: True if the password is valid, False otherwise.
        """

        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).{4,}$"
        if re.match(pattern, password):
            return True
        return False

    @staticmethod
    def hashing_password(password: str) -> str:
        """
        Hashes the given password using the SHA-256 algorithm.

        :param password: A string representing the password to be hashed.
        :return: A string representing the hashed password.
        """

        hash_pass = sha256(
            password.encode()
        ).hexdigest()

        return hash_pass

    @staticmethod
    def match_password(password: str, other: str) -> bool:
        """
        Check whether the given password and other match or not.

        :param password: A string representing the first password.
        :param other: A string representing the second password to compare with the first one.
        :return: True if the passwords match, False otherwise.
        """

        return password == other

    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        """
        Validates an Iranian mobile phone number.

        :param phone_number: str, the phone number to validate
        :return: bool, True if the phone number is valid, False otherwise
        """
        pattern = re.compile(r"^(\+98|0)?9\d{9}$")
        return bool(re.match(pattern, phone_number))
