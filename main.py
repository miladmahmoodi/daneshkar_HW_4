#! /usr/bin/python3

"""
This module use for User module menu.
"""

from user import User
from utils.exceptions import *
from getpass import getpass
from utils.messages import Message


def sign_up():
    """
    Display a form for signup a new user.

    The function prompts the user to enter their username, phone number, and password.
    Once the information is provided, the function calls the 'create' method of the 'User' class to create a new user.
    If the user is created successfully, a message is printed to the console.

    :return: Success message or Error message.
    """

    print(Message.SIGNUP_TITLE_PROMPT)
    username = input(Message.USERNAME_INPUT_PROMPT)
    phone_number = input(Message.PHONE_NUMBER_INPUT_PROMPT)
    password = getpass(Message.PASSWORD_INPUT_PROMPT)

    try:
        User.create(
            username,
            phone_number,
            password,
        )
    except ExistsUserError as err:
        print(err)
    except NotExistsUserError as err:
        print(err)
    except PasswordError as err:
        print(err)
    else:
        print(Message.success_signup(username))


def update_username(profile: 'User') -> 'User':
    """
    Update the user username.

    The function updates the user username using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: The instance of User.
    """
    print(Message.EDIT_USERNAME_TITLE_PROMPT)
    new_username = input(Message.NEW_USERNAME_INPUT_PROMPT)
    if profile.username != new_username:
        try:
            profile.update_username(
                new_username,
            )
        except ExistsUserError as err:
            print(err)
        except WrongUserName as err:
            print(err)
        else:
            print(Message.SUCCESS_USERNAME_UPDATE_MESSAGE)
    else:
        print(Message.NOT_CHANGE_USERNAME_MESSAGE)

    return profile


def update_phone_number(profile: 'User') -> 'User':
    """
    Update the user phone number.

    The function updates the user phone number using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: The instance of User.
    """

    print(Message.EDIT_PHONE_NUMBER_TITLE_PROMPT)
    new_phone_number = input(Message.NEW_PHONE_NUMBER_INPUT_PROMPT)
    if profile.phone_number != new_phone_number:
        try:
            profile.update_phone_number(
                new_phone_number,
            )
        except WrongPhoneNumber as err:
            print(err)
        else:
            print(Message.SUCCESS_UPDATE_PHONE_NUMBER_MESSAGE)
    else:
        print(Message.NOT_CHANGE_PHONE_NUMBER_MESSAGE)

    return profile


def update_profile(profile: User) -> None:
    """
    Update the user profile.

    The function updates the user profile using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: None.
    """
    while True:
        print(Message.MENU_EDIT_PROFILE_PROMPT)
        edit_inp = input(Message.MENU_EDIT_SELECTED_ITEM_INPUT_PROMPT)

        match edit_inp:
            case '0':
                break
            case '1':
                update_username(profile)
            case '2':
                update_phone_number(profile)


def update_password(profile: User) -> None:
    """
    Display a form for updating the user password.

    The function prompts the user to enter their old password and new password.
    Once the information is provided, the function calls the 'update_password' method of the given 'profile' object to
    update the user password.
    If the password is updated successfully, a message is printed to the console.

    :param profile: A User object representing the user profile whose password needs to be updated.
    :return: None.
    """

    print(Message.EDIT_PASSWORD_TITLE_PROMPT)
    old_password = getpass(Message.EDIT_OLD_PASSWORD_INPUT_PROMPT)
    new_password = getpass(Message.EDIT_NEW_PASSWORD_INPUT_PROMPT)
    confirm_password = getpass(Message.EDIT_CONFIRM_PASSWORD_INPUT_PROMPT)

    try:
        User.update_password(
            profile,
            old_password,
            new_password,
            confirm_password
        )
    except PasswordError as err:
        print(err)
    except ConfirmPasswordError as err:
        print(err)
    else:
        print(Message.SUCCESS_PASSWORD_UPDATE_MESSAGE)


def sign_in() -> None:
    """
    Display a form for user sign-in.

    The function prompts the user to enter their username and password.
    If the username and password are correct, the function displays a menu with options to view the user profile, edit
    the user profile, change the user password, or logout.
    If the username or password is incorrect, the function raises a ValueError.

    :return: None.
    """

    print(Message.SIGNIN_TITLE_PROMPT)
    username = input(Message.SIGNIN_USERNAME_INPUT_PROMPT)
    password = getpass(Message.SIGNIN_PASSWORD_INPUT_PROMPT)

    try:
        profile = User.get_profile(username)
        profile.sign_in(password)
    except ExistsUserError as err:
        print(err)
    except SigninError as err:
        print(err)
    else:
        print(Message.welcome_user_message(username))

        while True:
            print(Message.MENU_SIGNIN_PROMPT)
            register_inp = input(Message.MENU_SIGNIN_SELECTED_ITEM_PROMPT)

            match register_inp:
                case '1':
                    print(profile)
                case '2':
                    update_profile(profile)
                case '3':
                    update_password(profile)
                case '4':
                    break


def main() -> None:
    """
    Display the main menu.

    The function displays a menu with options to end the process, sign up, or sign in.
    If the user selects sign up, the function calls the 'sign_up' function to register a new user.
    If the user selects sign in, the function calls the 'sign_in' function to authenticate the user.

    :return: None.
    """

    while True:
        print(Message.MENU_MAIN_PROMPT)
        inp = input(Message.MENU_MAIN_SELECTED_PROMPT)
        match inp:
            case '0':
                break
            case '1':
                sign_up()
            case '2':
                sign_in()


if __name__ == '__main__':
    main()

