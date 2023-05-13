from user import User


from getpass import getpass


def register():
    """

    :return:
    """

    print('Register.')
    username = input('username: ')
    phone_number = input('phone_number: ')
    password = getpass('password: ')

    profile = User.create_user(
        username,
        phone_number,
        password,
    )

    print('User successfully created.')


def user_profile(profile):
    """
    
    :return: 
    """
    print(User.__str__(profile))


def update_profile(profile):
    """
    
    :return: 
    """
    print('Edit profile.')

    username = input('username: ')
    phone_number = input('phone_number: ')

    User.profile_update(
        profile,
        username,
        phone_number,
    )
    print('Edit profile successfully.')


def update_password(profile):
    """

    :return:
    """

    print('Change password.')
    old_password = getpass('Old password: ')
    new_password = getpass('New password: ')
    confirm_password = getpass('Confirm password: ')

    if new_password != confirm_password:
        raise Exception('password does`n match.')

    User.password_update(profile.get('username'), new_password)
    print('Success.')


def logout():
    """

    :return:
    """

    pass


def login():
    """

    :return:
    """

    print('Login')
    username = input('username: ')
    password = getpass('password: ')

    profile = User.login(
        username,
        password,
    )
    print(profile)

    print('1: Profile.  2: Edit profile.  3: Change password.  4: Logout.')
    
    register_inp = input('Yor choice: ')
    
    match register_inp:
        case '1':
            user_profile(profile)
        case '2':
            update_profile(profile)
        case '3':
            update_password(profile)
        case '4':
            logout()


def main():
    """

    :return:
    """

    print('0: End process.  1: Register  2: Login.')
    while True:
        inp = input('Enter your choices: ')
        match inp:
            case '0':
                break
            case '1':
                user_register()
            case '2':
                user_login()


if __name__ == '__main__':
    main()

