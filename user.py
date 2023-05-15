"""

"""
import re

from dataclasses import dataclass
from utils import Utils


@dataclass
class User(Utils):
    """

    """
    profiles = {}

    def __init__(self, username, phone_number, password):
        self.id = Utils.id_generator()
        self.username = username
        self.phone_number = phone_number
        self.__password = Utils.check_password(password)

        type(self).profiles[self.username] = self

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        """

        """
        self.__password = self.check_password(password)

    @staticmethod
    def exists_user(username) -> bool:
        """

        """
        if username in User.profiles:
            return True
        return False

    @classmethod
    def create(cls, username: str, phone_number: str, password: str):
        """

        :return:
        """

        if User.exists_user(username):
            raise Exception('This username already exists.')

        if Utils.check_password(password):
            profile = cls(
                username,
                phone_number,
                password
            )
            print(User.profiles)
            return profile

        if not User.exists_user(username):
            return Exception('Somethings was wrong.')

    def sign_in(self, password):
        """

        """

        password = Utils.hashing_password(password)

        if self.password != password:
            raise ValueError('username or password is wrong.')

        return self

    def update(self, username: str, phone_number: str):
        """

        """
        if User.exists_user(username):
            raise ValueError('This username already exists.')

        self.username = username
        self.phone_number = phone_number

        return self

    def update_password(self, old_password, new_password, confirm_password):

        old_password = Utils.hashing_password(old_password)

        if self.password != old_password:
            raise ValueError('Wrong password!')

        if not Utils.match_password(new_password, confirm_password):
            raise Exception('Password does`n match.')


        self.password = new_password

        return self

    def __str__(self):
        return f"----------------------------------------------------------------------\n" \
               f"Hi dear '{self.username}'. Hope you are well :)\n" \
               f"Your id is '{self.id}' and your phone number is '{self.phone_number}'\n" \
               f"----------------------------------------------------------------------"



