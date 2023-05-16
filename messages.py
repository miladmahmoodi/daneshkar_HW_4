class Message:
    """
    A class that contains various messages used in different parts of the program.
    """

    NOT_EXIST_USER_MESSAGE = 'Username does not exist.'
    EXIST_USER_MESSAGE = 'This username already exists.'
    WRONG_PASSWORD = 'Wrong password!'
    SOMETHING_WRONG = 'Somethings was wrong.'
    WRONG_USERNAME_PASSWORD = 'username or password is wrong.'
    WHAT_PASSWORD = 'The password must contain uppercase and lowercase letters, numbers and special symbols'\
                    ' and must have at least 4 characters.'
    NOT_MATCH_PASSWORD = 'Password does`n match.'
    SUCCESS_USERNAME_UPDATE_MESSAGE = 'Username updated successfully.'
    NOT_CHANGE_USERNAME_MESSAGE = 'You don`t change your username.'
    SUCCESS_UPDATE_PHONE_NUMBER_MESSAGE = 'phone number updated successfully.'
    NOT_CHANGE_PHONE_NUMBER_MESSAGE = 'You don`t change your phone number.'
    SUCCESS_PASSWORD_UPDATE_MESSAGE = 'Password successfully updated.'
    WELCOME_USER = 'Welcome Dear'

    @staticmethod
    def welcome_user_message(username: str) -> str:
        """
        Returns a welcome message with the given username.

        :param username: str, the username of the user.
        :return: str, the welcome message.
        """
        return f"Welcome Dear '{username}'"

    @staticmethod
    def success_signup(username: str) -> str:
        """
        Returns a success message for a new user signup.

        :param username: str, the username of the new user.
        :return: str, the success message.
        """
        return f"User '{username}' created successfully."

    # menu prompts
    SIGNUP_TITLE_PROMPT = '-- Welcome to signup form. --'
    USERNAME_INPUT_PROMPT = 'Your username: '
    PHONE_NUMBER_INPUT_PROMPT = 'Your phone number: '
    PASSWORD_INPUT_PROMPT = 'Your password: '
    EDIT_USERNAME_TITLE_PROMPT = '-- Edit username --'
    NEW_USERNAME_INPUT_PROMPT = 'New username: '
    EDIT_PHONE_NUMBER_TITLE_PROMPT = '-- Edit phone number --'
    NEW_PHONE_NUMBER_INPUT_PROMPT = 'New phone number: '
    MENU_EDIT_PROFILE_PROMPT = '-- [0] Cancel [1] Edit username  [2] Edit phone number --'
    MENU_EDIT_SELECTED_ITEM_INPUT_PROMPT = 'Your choice is: '
    EDIT_PASSWORD_TITLE_PROMPT = '-- Change password --'
    EDIT_OLD_PASSWORD_INPUT_PROMPT = 'Old password: '
    EDIT_NEW_PASSWORD_INPUT_PROMPT = 'New password: '
    EDIT_CONFIRM_PASSWORD_INPUT_PROMPT = 'Confirm password: '
    SIGNIN_TITLE_PROMPT = '-- Welcome to signin form. --'
    SIGNIN_USERNAME_INPUT_PROMPT = 'Username: '
    SIGNIN_PASSWORD_INPUT_PROMPT = 'Password: '
    MENU_SIGNIN_PROMPT = '-- [1] Profile  [2] Edit profile [3] Change password [4] Logout --'
    MENU_SIGNIN_SELECTED_ITEM_PROMPT = 'Your choice is: '
    MENU_MAIN_PROMPT = '-- [0] End process  [1] Signup  [2] Signin --'
    MENU_MAIN_SELECTED_PROMPT = 'Your choice is: '
