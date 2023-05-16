"""
This module use for User module menu.
"""

from user import User
from exceptions import *
from getpass import getpass


def sign_up():
    """
    Display a form for signing up a new user.

    The function prompts the user to enter their username, phone number, and password.
    Once the information is provided, the function calls the 'create' method of the 'User' class to create a new user.
    If the user is created successfully, a message is printed to the console.

    :return: Success message or Error message.
    """

    print('-- Welcome to signup form. --')
    username = input('Your username: ')
    phone_number = input('Your phone number: ')
    password = getpass('Your password: ')

    try:
        User.create(
            username,
            phone_number,
            password,
        )
    except ExistsUserError as err:
        print(err)
    except PasswordError as err:
        print(err)
    else:
        print(f"User '{username}' created successfully.")


def update_username(profile: 'User') -> 'User':
    """
    Update the user username.

    The function updates the user username using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: The instance of User.
    """
    print('-- Edit username --')
    new_username = input('New username: ')
    if profile.username != new_username:
        try:
            profile.update_username(
                new_username,
            )
        except ExistsUserError as err:
            print(err)
        else:
            print('Username updated successfully.')
    else:
        print('You don`t change your username.')

    return profile


def update_phone_number(profile: 'User') -> 'User':
    """
    Update the user phone number.

    The function updates the user phone number using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: The instance of User.
    """

    print('-- Edit phone number --')
    new_phone_number = input('New phone number: ')
    if profile.phone_number != new_phone_number:
        profile.update_phone_number(
            new_phone_number,
        )
        print('phone number updated successfully.')
    else:
        print('You don`t change your phone number.')

    return profile


def update_profile(profile: User) -> None:
    """
    Update the user profile.

    The function updates the user profile using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: None.
    """
    while True:
        print('-- [0] Cancel [1] Edit username  [2] Edit phone number --')
        edit_inp = input('Your choice is: ')

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

    print('-- Change password --')
    old_password = getpass('Old password: ')
    new_password = getpass('New password: ')
    confirm_password = getpass('Confirm password: ')

    try:
        profile.update_password(old_password, new_password, confirm_password)
    except PasswordError as err:
        print(err)
    except ConfirmPasswordError as err:
        print(err)
    else:
        print('Password successfully updated.')


def sign_in() -> None:
    """
    Display a form for user sign-in.

    The function prompts the user to enter their username and password.
    If the username and password are correct, the function displays a menu with options to view the user profile, edit
    the user profile, change the user password, or logout.
    If the username or password is incorrect, the function raises a ValueError.

    :return: None.
    """

    print('-- Welcome to signin form. --')
    username = input('Username: ')
    password = getpass('Password: ')

    try:
        profile = User.get_profile(username)
        profile.sign_in(password)
    except ExistsUserError as err:
        print(err)
    except SigninError as err:
        print(err)
    else:
        print(f"Welcome Dear '{username}'")

        while True:
            print('-- [1] Profile  [2] Edit profile [3] Change password [4] Logout --')
            register_inp = input('Your choice is: ')

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
        print('-- [0] End process  [1] Signup  [2] Signin --')
        inp = input('Your choice is: ')
        match inp:
            case '0':
                break
            case '1':
                sign_up()
            case '2':
                sign_in()


if __name__ == '__main__':
    main()

