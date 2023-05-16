"""
This module create for manage users.
"""

from dataclasses import dataclass
from utils import Utils
from typing import Union
from exceptions import *


@dataclass
class User(Utils):
    """
    A class used to represent User.
    """
    __profiles = {}

    def __init__(self, username: str, phone_number: str, password: str):
        self.id = Utils.id_generator()
        self.username = username
        self.phone_number = phone_number
        self.__password = Utils.check_password(password)

    @staticmethod
    def get_profile(username: str) -> 'User':
        """
        Returns the profile of the user with the given username.

        :param username: str, the username of the user.
        :return: the profile of the user.
        :raises: ExistsUserError, if the user with the given username does not exist.
        """

        if not User.exists_user(username):
            raise ExistsUserError('Username does not exist.')

        return User.__profiles[username]

    def save(self) -> None:
        """
        Saves the user profile to the class variable `User.profiles` under the username key.

        :return: None
        """
        type(self).__profiles[self.username] = self

    @staticmethod
    def exists_user(username: str) -> bool:
        """
        Check whether the given username exists in the profiles list.

        :param username: A string representing the username to be checked.
        :return: True if the username exists in the profiles list, False otherwise.
        """

        return username in User.__profiles

    @classmethod
    def create(cls, username: str, phone_number: str, password: str) -> Union['User', Exception]:
        """
        Create a new user profile with the given username, phone_number, and password.

        :param username: A string representing the username.
        :param phone_number: A string representing the phone number.
        :param password: A string representing the password.
        :return: If the input is valid, return a new instance of User. Otherwise, return an Exception object.
        """

        if cls.exists_user(username):
            raise ExistsUserError('This username already exists.')

        if not Utils.check_password(password):
            raise PasswordError('Wrong password!')

        profile = cls(
            username,
            phone_number,
            password
        )
        profile.save()

        if not cls.exists_user(username):
            return Exception('Somethings was wrong.')

        return profile

    def sign_in(self, password: str) -> 'User':
        """
        Sign in the user with the given password.

        :param password: A string representing the password of the user.
        :return: The instance of User.
        :raises ValueError: If the given password is wrong.
        """

        password = Utils.hashing_password(password)

        if self.__password != password:
            raise SigninError('username or password is wrong.')

        return self

    def update_username(self, username: str) -> 'User':
        """
        Update the username of the user.

        :param username: A string representing the new username.
        :return: The instance of User.
        :raises ValueError: If the given username already exists.
        """

        if type(self).exists_user(username):
            raise ExistsUserError('This username already exists.')

        old_username = self.username
        del type(self).__profiles[old_username]

        self.username = username
        type(self).__profiles[username] = self

        return self

    def update_phone_number(self, phone_number: str) -> 'User':
        """
        Update the phone number of the user.

        :param phone_number: A string representing the new phone_number.
        :return: The instance of User.
        """

        self.phone_number = phone_number

        return self

    def update_password(self, old_password: str, new_password: str, confirm_password: str) -> 'User':
        """
        Update the password of the user.

        :param old_password: A string representing the old password.
        :param new_password: A string representing the new password.
        :param confirm_password: A string representing the new password confirmation.
        :return: The instance of User.
        :raises ValueError: If the given old password is wrong.
        :raises Exception: If the new password doesn't match the confirmation.
        """
        old_password = Utils.hashing_password(old_password)

        if self.__password != old_password:
            raise PasswordError('Wrong password!')

        if not Utils.is_valid_password(new_password):
            raise PasswordError('The password must contain uppercase and lowercase letters, numbers and special symbols'
                                ' and must have at least 4 characters.')

        if not Utils.match_password(new_password, confirm_password):
            raise ConfirmPasswordError('Password does`n match.')

        self.__password = Utils.check_password(new_password)

        return self

    def __str__(self) -> str:
        """
        Return the string representation of the User object.

        :return: A string representing the User object.
        """
        return f"----------------------------------------------------------------------\n" \
               f"Hi dear '{self.username}'. Hope you are well :)\n" \
               f"Your id is '{self.id}' and your phone number is '{self.phone_number}'\n" \
               f"----------------------------------------------------------------------"
