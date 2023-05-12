from getpass import getpass


def user_register():
    """

    :return:
    """

    print('Register.')
    username = input('username: ')
    phone_number = input('phone_number: ')
    password = getpass('password: ')

    # do some things for register.


def user_profile():
    """
    
    :return: 
    """
    pass


def update_user_profile():
    """
    
    :return: 
    """
    pass


def change_user_password():
    """

    :return:
    """

    print('Change password.')
    old_password = getpass('Old password: ')
    new_password = getpass('New password: ')
    confirm_password = getpass('Confirm password: ')

    # do something


def logout():
    """

    :return:
    """

    pass


def user_login():
    """

    :return:
    """

    print('Login')
    username = input('username: ')
    password = getpass('password: ')

    # if err
    #     raise err

    print('1: Profile.  2: Edit profile.  3: Change password.  4: Logout.')
    
    register_inp = input('Yor choice: ')
    
    match register_inp:
        case '1':
            user_profile()
        case '2':
            update_user_profile()
        case '3':
            change_user_password()
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
    print(
        main()
    )