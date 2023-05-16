class Message:
    """
    A class that contains various messages used in different parts of the program.
    """

    NOT_EXIST_USER_MESSAGE = "\033[91m{}\033[00m" .format(
        'Username does not exist.'
    )
    EXIST_USER_MESSAGE = "\033[91m{}\033[00m" .format(
        'This username already exists.'
    )
    WRONG_PASSWORD = "\033[91m{}\033[00m" .format(
        'Wrong password!'
    )
    SOMETHING_WRONG = "\033[91m{}\033[00m" .format(
        'Somethings was wrong.'
    )
    WRONG_USERNAME_PASSWORD = "\033[91m{}\033[00m" .format(
        'username or password is wrong.'
    )
    WHAT_PASSWORD = "\033[91m{}\033[00m" .format(
        'The password must contain uppercase and lowercase letters, numbers and special symbols' \
        ' and must have at least 4 characters.'
    )
    NOT_MATCH_PASSWORD = "\033[91m{}\033[00m" .format(
        'Password does`n match.'
    )
    SUCCESS_USERNAME_UPDATE_MESSAGE = "\033[92m{}\033[00m" .format(
        'Username updated successfully.'
    )
    NOT_CHANGE_USERNAME_MESSAGE = "\033[93m{}\033[00m" .format(
        'You don`t change your username.'
    )
    SUCCESS_UPDATE_PHONE_NUMBER_MESSAGE = "\033[92m{}\033[00m" .format(
        'phone number updated successfully.'
    )
    NOT_CHANGE_PHONE_NUMBER_MESSAGE = "\033[93m{}\033[00m" .format(
        'You don`t change your phone number.'
    )
    SUCCESS_PASSWORD_UPDATE_MESSAGE = "\033[92m{}\033[00m" .format(
        'Password successfully updated.'
    )
    WELCOME_USER = "\033[92m{}\033[00m" .format(
        'Welcome Dear'
    )
    WRONG_PHONE_NUMBER = "\033[91m{}\033[00m" .format(
        'phone number format is wrong.'
    )
    WRONG_USERNAME = "\033[91m{}\033[00m" .format(
        'Username is wrong.'
    )

    @staticmethod
    def welcome_user_message(username: str) -> str:
        """
        Returns a welcome message with the given username.

        :param username: str, the username of the user.
        :return: str, the welcome message.
        """
        return "\033[92mWelcome Dear '{}'\033[00m".format(
            username
        )

    @staticmethod
    def success_signup(username: str) -> str:
        """
        Returns a success message for a new user signup.

        :param username: str, the username of the new user.
        :return: str, the success message.
        """
        return "\033[92mUser '{}' created successfully.\033[00m".format(
            username
        )

    # menu prompts
    SIGNUP_TITLE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- Welcome to signup form. --'
    )
    USERNAME_INPUT_PROMPT = 'Your username: '
    PHONE_NUMBER_INPUT_PROMPT = 'Your phone number: '
    PASSWORD_INPUT_PROMPT = 'Your password: '
    EDIT_USERNAME_TITLE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- Edit username --'
    )
    NEW_USERNAME_INPUT_PROMPT = 'New username: '
    EDIT_PHONE_NUMBER_TITLE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- Edit phone number --'
    )
    NEW_PHONE_NUMBER_INPUT_PROMPT = 'New phone number: '
    MENU_EDIT_PROFILE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- [0] Cancel [1] Edit username  [2] Edit phone number --'
    )
    MENU_EDIT_SELECTED_ITEM_INPUT_PROMPT = 'Your choice is: '
    EDIT_PASSWORD_TITLE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- Change password --'
    )
    EDIT_OLD_PASSWORD_INPUT_PROMPT = 'Old password: '
    EDIT_NEW_PASSWORD_INPUT_PROMPT = 'New password: '
    EDIT_CONFIRM_PASSWORD_INPUT_PROMPT = 'Confirm password: '
    SIGNIN_TITLE_PROMPT = "\033[96m{}\033[00m" .format(
        '-- Welcome to signin form. --'
    )
    SIGNIN_USERNAME_INPUT_PROMPT = 'Username: '
    SIGNIN_PASSWORD_INPUT_PROMPT = 'Password: '
    MENU_SIGNIN_PROMPT = "\033[96m{}\033[00m" .format(
        '-- [1] Profile  [2] Edit profile [3] Change password [4] Logout --'
    )
    MENU_SIGNIN_SELECTED_ITEM_PROMPT = 'Your choice is: '
    MENU_MAIN_PROMPT = "\033[96m{}\033[00m" .format(
        '-- [0] End process  [1] Signup  [2] Signin --'
    )
    MENU_MAIN_SELECTED_PROMPT = 'Your choice is: '
