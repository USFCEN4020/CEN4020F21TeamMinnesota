import pickle

from os import path
from user import User
MAX_EXPRIENCE = 3
MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE = "Maximum number of job experience reached. (3)"


class Profile:
    PROFILE_FILE_NAME = "profiles.pickle"

    def __init__(self):
        self.title = ""
        self.major = ""
        self.university = ""
        self.about = ""
        self.exprience = []
        self.education = []

    def save(self, experience):
        if len(self.exprience) >= MAX_EXPRIENCE:
            return MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE

        self.exprience.append(experience)
        User.update_users_file()

    def save_education(self, education):
        self.education.append(education)
        User.update_users_file()




