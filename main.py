from user import User
from getpass import getpass


def sign_up():
    """

    :return:
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


def update_profile(profile):
    """

    :return:
    """
    print('-- Edit Profile. --')

    username = input('New username: ')
    phone_number = input('New phone number: ')

    profile.update(username, phone_number)

    print('Edit profile successfully.')


def update_password(profile):
    """

    :return:
    """

    print('-- Change password --')
    old_password = getpass('Old password: ')
    new_password = getpass('New password: ')
    confirm_password = getpass('Confirm password: ')

    profile.update_password(old_password, new_password, confirm_password)

    print('Password successfully updated.')


def show_profile(profile: User):
    """

    :return:
    """
    print(profile)


def sign_in():
    """

    :return:
    """
    print('-- Welcome to signin form. --')
    username = input('Username: ')
    password = getpass('Password: ')

    if not User.exists_user(username):
        raise ValueError('username or password is wrong.')

    profile = User.profiles.get(username)

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


def main():
    """

    :return:
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

