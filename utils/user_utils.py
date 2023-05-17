"""
This module is used for User module utilities.
"""

import re

from uuid import uuid4
from hashlib import sha256
from utils.exceptions import *
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
        return bool(re.match(
            pattern,
            password,
        ))

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
    def valid_phone_number(phone_number: str | None) -> bool:
        """
        Validates an Iranian mobile phone number.

        :param phone_number: str, the phone number to validate
        :return: bool, True if the phone number is valid, False otherwise
        """
        pattern = r"^(\+98|0)?9\d{9}$"
        return bool(re.match(pattern, phone_number))

    @staticmethod
    def check_phone_number(phone_number: str | None):
        """
        Check the validity of a phone number and return it if it is valid.

        :param phone_number: str or None, the phone number to validate
        :return: str, the validated phone number
        :raises: WrongPhoneNumber, if the phone number is not valid
        """

        if not Utils.valid_phone_number(phone_number):
            raise WrongPhoneNumber(Message.WRONG_PHONE_NUMBER)
        elif phone_number is None and phone_number == '':
            return ''
        return phone_number