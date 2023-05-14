import json, re

from uuid import uuid4
from hashlib import sha256

# class MyExceptions(Exception):
#     def


class Utils:
    @staticmethod
    def id_generator():
        return uuid4().int

    @staticmethod
    def check_password(password: str) -> str:
        """

        """
        if not Utils.is_valid_password(password):
            raise Exception('The password must contain uppercase and lowercase letters, numbers and special symbols'
                            ' and must have at least 4 characters..')
        return Utils.hashing_password(password)

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """

        """
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[a-zA-Z0-9\W]{4,}$'
        if not re.match(pattern, password):
            return False
        return True

    @staticmethod
    def hashing_password(password: str) -> str:
        """

        :param password:
        :return:
        """

        hash_pass = sha256(
            password.encode()
        ).hexdigest()

        return hash_pass

    @staticmethod
    def save_data(data: list):
        """

        """
        with open('database.json', 'a', encoding='utf-8') as file:
            json.dumps(
                data
            )

    @staticmethod
    def confirm_password(password: str, other: str) -> bool:
        """

        """
        if password != other:
            return False
        return True

