"""

"""
import re
import json
from builtins import staticmethod

from dataclasses import dataclass
from uuid import uuid4
from hashlib import sha256


class Utils:
    @classmethod
    def id_generator(cls):
        return uuid4().int

    @staticmethod
    def is_valid_password(password: str) -> bool:
        """

        """
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W)[a-zA-Z0-9\W]{4,}$'
        if not re.match(pattern, password):
            return False
        return True

    @staticmethod
    def password_hasher(password: str) -> str:
        """

        :param password:
        :return:
        """
        # if not cls.is_valid_password(password):
        #     raise Exception('Your password is easy.')

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


@dataclass()
class User(Utils):
    """

    """
    profiles = {}

    def __init__(self, username, phone_number, password):
        self.id = Utils.id_generator()
        self.username = username
        self.phone_number = phone_number
        self.__password = Utils.password_hasher(password)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        """

        """
        self.__password = self.password_hasher(password)

    def exists_user(self) -> bool:
        if self.username in User.profiles:
            return False
        return True

    def add_profiles(self):
        User.profiles[self.username] = {
            'id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'password': self.password
        }

    @classmethod
    def create_user(cls, username, phone_number, password):
        """

        :return:
        """
        if not User.is_valid_password(password):
            return 'Your password is easy.'

        user = cls(
            username,
            phone_number,
            password,
        )

        if not cls.exists_user(user):
            return 'user name already exists.'

        user.add_profiles()

        return user

    def save(self):
        self.profiles[self.username] = {
            'id': self.id,
            'username': self.username,
            'phone_number': self.phone_number,
            'password': self.password
        }

    @staticmethod
    def login(username, password):
        """

        """
        if not User.is_valid_password(password):
            return 'Your password is easy.'

        profile = User.profiles.get(username)
        if not profile:
            return 'username or password is wrong.'

        profile_password = profile.get('password')
        if Utils.password_hasher(password) != profile_password:
            return 'username or password is wrong.'

        return 'You`re logged in.'


    @staticmethod
    def profile_update(profile, username, phone_number):
        if username in User.profiles:
            raise Exception('This username already exists.')

        new_prof = User.profiles[username] = {
            'id': profile.get('id'),
            'phone_number': phone_number,
            'password': profile.get('password')
        }
        del User.profiles[profile.get('username')]

    @staticmethod
    def password_update(username, new_password):
        user = User.profiles.get(username)
        user['password'] = Utils.password_hasher(new_password)


    def __str__(self):
        return f'{User.profiles.get(self.username)}'



