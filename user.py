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

        type(self).profiles[self.username] = {
            'id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'password': self.password
        }

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
            cls(
                username,
                phone_number,
                password
            )

        if User.exists_user(username):
            return f"Profile of '{username}' successfully created."

        return Exception('Somethings was wrong.')

    @staticmethod
    def sign_in(username, password):
        """

        """
        if not User.exists_user(username):
            raise ValueError('username or password is wrong.')

        profile = User.profiles.get(username)
        password = Utils.hashing_password(password)

        if profile['password'] != password:
            raise ValueError('username or password is wrong.')

        return profile

    @staticmethod
    def update(profile, username: str, phone_number: str):
        """

        """
        if User.exists_user(username):
            raise ValueError('This username already exists.')

        user_id = profile['id']
        old_username = profile['username']
        password = profile['password']

        update_profile = User.profiles[username] = {
            'id': user_id,
            'username': username,
            'phone_number': phone_number,
            'password': password,
        }
        User.profiles.pop(old_username)

        return update_profile

    @staticmethod
    def update_password(username, new_password, confirm_password):
        if not Utils.confirm_password(new_password, confirm_password):
            raise Exception('Password does`n match.')

        password = Utils.check_password(new_password)
        print(Utils.hashing_password(new_password))
        profile = User.profiles.get(username)
        profile['password'] = password

    def __str__(self):
        return self.profiles



