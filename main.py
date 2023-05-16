"""
This module use for User module menu.
"""

from user import User
from exceptions import SigninError
from getpass import getpass


def sign_up() -> None:
    """
    Display a form for signing up a new user.

    The function prompts the user to enter their username, phone number, and password.
    Once the information is provided, the function calls the 'create' method of the 'User' class to create a new user.
    If the user is created successfully, a message is printed to the console.

    :return: None.
    """

    print('-- Welcome to signup form. --')
    username = input('Your username: ')
    phone_number = input('Your phone number: ')
    password = getpass('Your password: ')

    status = User.create(
        username,
        phone_number,
        password,
    )
    if status:
        print(f"User '{username}' created successfully.")


def update_profile(profile: User) -> None:
    """
    Update the user profile.

    The function updates the user profile using the given 'profile' object.

    :param profile: A User object representing the user profile to be updated.
    :return: None.
    """
    print('-- Edit Profile. --')

    username = input('New username: ')
    phone_number = input('New phone number: ')

    profile.update(username, phone_number)

    print('Edit profile successfully.')


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

    profile.update_password(old_password, new_password, confirm_password)

    print('Password successfully updated.')


def show_profile(profile: User) -> None:
    """
    Display the user profile.

    The function displays the user profile information, including the username, phone number, and email address.

    :param profile: A User object representing the user profile to be displayed.
    :return: None.
    """
    print(profile)


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

    profile = User.get_profile(username)
    profile.sign_in(password)

    print(f"Welcome '{username}'")

    while True:
        print('-- [1] Profile  [2] Edit profile [3] Change password [4] Logout --')
        register_inp = input('Your choice is: ')
        match register_inp:
            case '1':
                show_profile(profile)
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

