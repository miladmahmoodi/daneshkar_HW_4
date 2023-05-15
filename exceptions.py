"""
This module defines custom exception classes for a user authentication system.
"""


class ExistsUserError(Exception):
    """
    Raised when a user with the given username already exists.
    """
    pass


class SigninError(Exception):
    """
    Raised when there is an error during the sign-in process.
    """
    pass


class PasswordError(Exception):
    """
    Raised when the password provided is invalid.
    """
    pass


class ConfirmPasswordError(Exception):
    """
    Raised when the passwords don`t match.
    """
    pass

