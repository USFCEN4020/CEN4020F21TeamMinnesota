from user import User

MAX_EXPERIENCE = 3
MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE = "Maximum number of job experience reached. (3)"
EXPERIENCE_INDEX_OUT_OF_RANGE = "Experience index out of range."
EDUCATION_INDEX_OUT_OF_RANGE = "Education index out of range."


class Profile:
    def __init__(self):
        self.title = ""
        self.major = ""
        self.university = ""
        self.about = ""
        self.experience = []
        self.education = []

    def add_experience(self, experience):
        if len(self.experience) >= MAX_EXPERIENCE:
            return MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE

        self.experience.append(experience)
        User.update_users_file()

    def delete_experience(self, index):
        if index < 0 or index >= len(self.experience):
            return EXPERIENCE_INDEX_OUT_OF_RANGE

        self.experience.pop(index)
        User.update_users_file()

    def add_education(self, education):
        self.education.append(education)
        User.update_users_file()

    def delete_education(self, index):
        if index < 0 or index >= len(self.education):
            return EDUCATION_INDEX_OUT_OF_RANGE

        self.education.pop(index)
        User.update_users_file()
