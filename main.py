"""

"""

from dataclasses import dataclass
from getpass import getpass


@dataclass()
class User:
    """

    """
    username = str
    phone_number = int, None
    __password = str
    id = ...

    @property
    def password(self):
        """

        :return:
        """
        return self.__password

    @password.setter
    def password(self, new_pass):
        """

        :param new_pass:
        :return:
        """
        self.__password = new_pass


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
                print('Register.')
                username = input('username: ')
                phone_number = input('phone_number: ')
                password = getpass('password: ')
                # do some things for register.
            case '2':
                print('Login')
                username = input('username: ')
                password = getpass('password: ')
                # if err
                #     raise err
                print('1: Profile.  2: Edit profile.  3: Change password.  4: Logout.')
                register_inp = input('Yor choice: ')
                match register_inp:
                    case '1':
                        pass
                        # show data
                        break
                    case '2':
                        pass
                        # edit profile
                        break
                    case '3':
                        pass
                        print('Change password.')
                        old_password = getpass('Old password: ')
                        new_password = getpass('New password: ')
                        confirm_password = getpass('Confirm password: ')
                        # do something
                    case '4':
                        break
                        # logout









if __name__ == '__main__':
    print(
        main()
    )