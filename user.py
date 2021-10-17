import hashlib
import pickle

from os import path

INVALID_USERNAME_ERROR_MESSAGE = "The username is empty."
USERNAME_IN_USE_ERROR_MESSAGE = "The username is in use."
PASSWORD_LENGTH_ERROR_MESSAGE = "The password must have between 8 and 12 characters."
PASSWORD_CAPITAL_LETTER_ERROR_MESSAGE = "The password must have at least one capital letter."
PASSWORD_DIGIT_ERROR_MESSAGE = "The password must have at least one digit."
PASSWORD_NON_ALPHA_ERROR_MESSAGE = "The password must have at least one non-alpha character."
MAX_ALLOWED_ACCOUNTS_ERROR_MESSAGE = "All permitted accounts have been created, please come backlater"
CONNECT_TO_SELF_ERROR_MESSAGE = "You can not connect to yourself."
CONNECT_TO_FRIEND_ERROR_MESSAGE = "You are already its friend."
RESEND_CONNECT_ERROR_MESSAGE = "You have already requested connection."
CONNECTION_REQUEST_PENDING_ERROR_MESSAGE = "You have a pending connection with this user."
CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE = "Connetion request not found."
CONNECTION_NOT_FOUND_ERROR_MESSAGE = "Connection not found."

MAX_USERS = 10

class User:
    USERS_FILE_NAME = "users.pickle"
    users = {}

    def __init__(self, username, password, first_name, last_name, app_language):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.profile = None
        self.email_notifications = True
        self.sms_notifications = True
        self.targeted_ads = True
        self.app_language = app_language
        self.friends = []
        self.sent_friend_requests = []
        self.received_friend_requests = []

    # Opens and loads the uses file. If the path isn't found, it creates one.
    @staticmethod
    def load_users_file():
        # If the user.pickle file not found, creates one through the update function.
        if not path.isfile(User.USERS_FILE_NAME):
            User.update_users_file()

        # If it exists, then open for reading as users_file.
        with open(User.USERS_FILE_NAME, "rb") as users_file:
            User.users = pickle.load(users_file)

    # Creates the users file and dumps User.users dict.
    @staticmethod
    def update_users_file():
        with open(User.USERS_FILE_NAME, "wb") as users_file:
            pickle.dump(User.users, users_file)

    # Hash encrypts input parameter and returns it.
    @staticmethod
    def hash_password(password):
        return hashlib.md5(password.encode()).hexdigest()

    # Login method for the main screen.
    @staticmethod
    def login(username, password):
        """
        log_in method returns the logged-in User object on a successful login
        and None on a failed login.
        """
        if username not in User.users:
            return None
        
        user = User.users[username]
        if user.password != User.hash_password(password):
            return None

        return user

    # Saves username as key and User object as value in a dictionary to pickle file.
    def save(self):
        """
        save method returns a user intended message when the username 
        or password does not meet the requirements, and None when
        the saving was successful.
        """

        if len(User.users) >= MAX_USERS:
            return MAX_ALLOWED_ACCOUNTS_ERROR_MESSAGE

        if len(self.username) == 0:
            return INVALID_USERNAME_ERROR_MESSAGE

        if self.username in User.users:
            return USERNAME_IN_USE_ERROR_MESSAGE

        if len(self.password) < 8 or len(self.password) > 12:
            return PASSWORD_LENGTH_ERROR_MESSAGE

        has_non_alpha = False
        has_capital_letter = False
        has_digit = False
        for character in self.password:
            if character.isupper():
                has_capital_letter = True

            if character.isnumeric():
                has_digit = True

            if not character.isalnum():
                has_non_alpha = True

        if not has_non_alpha:
            return PASSWORD_NON_ALPHA_ERROR_MESSAGE

        if not has_capital_letter:
            return PASSWORD_CAPITAL_LETTER_ERROR_MESSAGE

        if not has_digit:
            return PASSWORD_DIGIT_ERROR_MESSAGE

        self.password = User.hash_password(self.password)
        User.users[self.username] = self
        User.update_users_file()

    def toggle_email_notifications(self):
        self.email_notifications = not self.email_notifications
        User.update_users_file()

    def toggle_sms_notifications(self):
        self.sms_notifications = not self.sms_notifications
        User.update_users_file()

    def toggle_targeted_ads(self):
        self.targeted_ads = not self.targeted_ads
        User.update_users_file()

    @staticmethod
    def find_by_name(first_name, last_name):
        """
        find_by_name method returns the found User object when a user registered 
        with the provided name is found in the database and None when no user
        is found.
        """
        for email in User.users:
            user = User.users[email]
            if first_name.lower() != user.first_name.lower():
                continue
            
            if last_name.lower() == user.last_name.lower():
                return user
        
        return None

    @staticmethod
    def find_users_by_last_name(last_name):
        users = []
        for user in User.users.values():
            if user.last_name.lower() == last_name.lower():
                users.append(user)
        
        return users

    @staticmethod
    def find_users_by_university(university):
        users = []
        for user in User.users.values():
            if user.profile and user.profile.university.lower() == university.lower():
                users.append(user)
        
        return users
    
    @staticmethod
    def find_users_by_major(major):
        users = []
        for user in User.users.values():
            if user.profile and user.profile.major.lower() == major.lower():
                users.append(user)
        
        return users
    
    def request_connection(self, user):
        if self == user:
            return CONNECT_TO_SELF_ERROR_MESSAGE

        if user.username in self.sent_friend_requests:
            return RESEND_CONNECT_ERROR_MESSAGE
        
        if user.username in self.received_friend_requests:
            return CONNECTION_REQUEST_PENDING_ERROR_MESSAGE

        if user.username in self.friends:
            return CONNECT_TO_FRIEND_ERROR_MESSAGE
        
        self.sent_friend_requests.append(user.username)
        user.received_friend_requests.append(self.username)
        User.update_users_file()

    def accept_connection(self, user):
        if user.username not in self.received_friend_requests:
            return CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
        
        self.friends.append(user.username)
        self.received_friend_requests.remove(user.username)
        
        user.friends.append(self.username)
        user.sent_friend_requests.remove(self.username)
        User.update_users_file()

    def reject_connection(self, user):
        if user.username not in self.received_friend_requests:
            return CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
        
        self.received_friend_requests.remove(user.username)
        user.sent_friend_requests.remove(self.username)
        User.update_users_file()

    def disconnect(self, user):
        if user.username not in self.friends:
            return CONNECTION_NOT_FOUND_ERROR_MESSAGE
        
        self.friends.remove(user.username)
        user.friends.remove(self.username)
        User.update_users_file()
    