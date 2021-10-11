import profile
from user import User
from collections import deque
import textwrap
from job import Job
from profile import Profile
from experience import Experience
from education import Education

SKILLS = ["Communication", "Development", "Marketing", "Testing", "Equestrian"]
LANGUAGES = ["English", "Spanish"]
GO_BACK_KEY = "b"
TEXT_WIDTH = 120

GO_BACK_MESSAGE = "To go back to the previous screen, press 'b': "
UNDER_CONSTRUCTION_MESSAGE = "Under Construction."
SELECT_NEW_SKILL_MESSAGE = "Select a new skill: "
TYPE_USERNAME_MESSAGE = "Username: "
TYPE_PASSWORD_MESSAGE = "Password: "
TYPE_FIRST_NAME_MESSAGE = "First Name: "
TYPE_LAST_NAME_MESSAGE = "Last Name: "
EDIT_PROFILE_MESSAGE = "Please select what field you would like to edit: "
TYPE_TITLE_MESSAGE = "Title(e.g. 3rd year computer science student: "
TYPE_MAJOR_MESSAGE = "Major: "
TYPE_NAME_OF_UNIVERSITY = "Current university: "
TYPE_SUMMARY_MESSAGE = "Summary: "
UPDATE_WARRNING = "Warning: You will be updating this field\n"
LOGIN_SUCCESSFUL_MESSAGE = "You have successfully logged in"
USER_CREATED_MESSAGE = "User created successfully."
SELECT_OPTION_MESSAGE = "Please, choose which action you would like to take: "
SELECT_LANGUAGE_MESSAGE = "Please, choose which language you want to use: "
VIDEO_PLAYNG_MESSAGE = "Video is now playing"
INVALID_INPUT_ERROR_MESSAGE = "Please type a valid value."
INVALID_SKILL_ERROR_MESSAGE = "Error: Please select a valid skill between 0 and 4"
LOGIN_ERROR_MESSAGE = "Incorrect username / password, please try again"
CONTACT_FOUND_MESSAGE = "They are a part of the InCollege system."
CONTACT_NOT_FOUND_MESSAGE = "They are NOT a part of the InCollege system yet."
JOB_SAVED_MESSAGE = "Job has been saved!"
TYPE_JOB_TITLE_MESSAGE = "Enter title of Job: "
TYPE_JOB_DESCRIPTION_MESSAGE = "Enter a brief description of Job: "
TYPE_JOB_EMPLOYER_MESSAGE = "Employer: "
TYPE_JOB_LOCATION_MESSAGE = "Location of Job: "
TYPE_JOB_SALARY_MESSAGE = "Estimated Salary: "
TYPE_JOB_TITLE_MESSAGE = "Job Title: "
TYPE_DATE_STARTED_MESSAGE = "Date Started: "
TYPE_DATE_ENDED_MESSAGE = "Date Ended: "
HELP_CENTER_MESSAGE = "We're here to help!"
GENERAL_OPTION_ABOUT_MESSAGE = "In College: Welcome to In College, the world's largest "\
    "college student network with many users in many countries and territories worldwide"
PRESS_MESSAGE = "In College Pressroom: Stay on top of the latest news, updates, "\
    "and reports!"
EXPERIENCE_ADDED_MESSAGE = "Experience added succesfully!"
EXPERIENCE_REMOVED_MESSAGE ="Experience removed successful!"
TYPE_SCHOOL_NAME_MESSAGE = "School Name: "
TYPE_DEGREE_MESSAGE = "Degree: "
TYPE_YEARS_ATTENDED_MESSAGE = "Years Attended: "
EDUCATION_ADDED_MESSAGE = "Education added succesfully!"
EDUCATION_REMOVED_MESSAGE = "Education removed successful!"
NO_PROFILE_YET_MESSAGE = "You do not have a profile to view yet. "\
    "Please return to dashboard and select 'Edit Profile'"


def screen(method):
    def wrapper(app):
        app.history.append(method.__name__)
        print(f"\n{'=' * TEXT_WIDTH}\n")
        return method(app)

    return wrapper


class App:
    SUCCESS_STORY_FILE_NAME = "./resources/success_story.txt"
    COPYRIGHT_NOTICE_FILE_NAME = "./resources/copyright_notice.txt"
    ABOUT_MESSAGE_FILE_NAME = "./resources/about_message.txt"
    ACCESSIBILITY_MESSAGE_FILE_NAME = "./resources/accessibility_message.txt"
    USER_AGREEMENT_FILE_NAME = "./resources/user_agreement.txt"
    PRIVACY_POLICY_FILE_NAME = "./resources/privacy_policy.txt"
    COOKIE_POLICY_FILE_NAME = "./resources/cookie_policy.txt"
    COPYRIGHT_POLICY_FILE_NAME = "./resources/copyright_policy.txt"
    BRAND_POLICY_FILE_NAME = "./resources/brand_policy.txt"

    success_story = ""
    copyright_notice = ""
    about_message = ""
    accessibility_message = ""
    user_agreement = ""
    privacy_policy = ""
    cookie_policy = ""
    copyright_policy = ""
    brand_policy = ""

    def __init__(self):
        self.history = deque()
        self.current_user = None

    @staticmethod
    def load_success_story():
        with open(App.SUCCESS_STORY_FILE_NAME) as success_story_file:
            App.success_story = success_story_file.read()

    @staticmethod
    def load_copyright_notice():
        with open(App.COPYRIGHT_NOTICE_FILE_NAME) as copyright_notice_file:
            App.copyright_notice = copyright_notice_file.read()

    @staticmethod
    def load_about_message():
        with open(App.ABOUT_MESSAGE_FILE_NAME) as about_message_file:
            App.about_message = about_message_file.read()

    @staticmethod
    def load_accessibility_message():
        with open(App.ACCESSIBILITY_MESSAGE_FILE_NAME) as accessability_message_file:
            App.accessibility_message = accessability_message_file.read()

    @staticmethod
    def load_user_agreement():
        with open(App.USER_AGREEMENT_FILE_NAME) as user_agreement_file:
            App.user_agreement = user_agreement_file.read()

    @staticmethod
    def load_privacy_policy():
        with open(App.PRIVACY_POLICY_FILE_NAME) as privacy_policy_file:
            App.privacy_policy = privacy_policy_file.read()

    @staticmethod
    def load_cookie_policy():
        with open(App.COOKIE_POLICY_FILE_NAME) as cookie_policy_file:
            App.cookie_policy = cookie_policy_file.read()

    @staticmethod
    def load_copyright_policy():
        with open(App.COPYRIGHT_POLICY_FILE_NAME) as copyright_policy_file:
            App.copyright_policy = copyright_policy_file.read()

    @staticmethod
    def load_brand_policy():
        with open(App.BRAND_POLICY_FILE_NAME) as brand_policy_file:
            App.brand_policy = brand_policy_file.read()

    def go_back(self):
        """
        Function to run the previous function name saved in the
        history stack.
        """
        try:
            self.history.pop()
            function_name = self.history.pop()
        except IndexError:
            return None

        back = getattr(self, function_name)
        return back()

    def reload_screen(self):
        """
        Function to reload the last function name saved in the
        history stack.
        """
        if len(self.history) == 0:
            return None

        function_name = self.history.pop()
        current_screen = getattr(self, function_name)
        return current_screen()

    def handle_input(self, prompt, input_type=str):
        """
        :param key: The user's input
        :param prompt: The prompt to pass to handle_input recursively in the event of an error
        :param input_type: The expected input type
        :return: The user's input
        """
        key = input(prompt)
        if input_type != int or key.isnumeric() or key == GO_BACK_KEY:
            return key

        print(INVALID_INPUT_ERROR_MESSAGE)
        return self.handle_input(prompt, input_type)

    def handle_go_back(self, choice):
        if choice == GO_BACK_KEY:
            return self.go_back()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def add_experience_screen(self):
        print("Add Experience", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()
           
        profile = self.current_user.profile

        title = input(TYPE_JOB_TITLE_MESSAGE)
        employer = input(TYPE_JOB_EMPLOYER_MESSAGE)
        date_started = input(TYPE_DATE_STARTED_MESSAGE)
        date_ended = input(TYPE_DATE_ENDED_MESSAGE)
        location = input(TYPE_JOB_LOCATION_MESSAGE)
        description = input(TYPE_JOB_DESCRIPTION_MESSAGE)

        experience = Experience(
            title, 
            employer, 
            date_started, 
            date_ended, 
            location, 
            description
        )

        error_message = profile.add_experience(experience)
        if error_message:
            print(error_message)
        else:
            print(EXPERIENCE_ADDED_MESSAGE)            

        return self.go_back()

    @screen
    def delete_experience_screen(self):
        print("Delete Experience", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        print("Which experience would you like to delete?")           
        for index, experience in enumerate(self.current_user.profile.experience):
            print(f"{index}. {experience.title} at {experience.employer} ", end="")
            print(f"{experience.date_started} - {experience.date_ended}")
        print("b. Go Back")

        experience_index = self.handle_input(SELECT_OPTION_MESSAGE, int)
        if experience_index == GO_BACK_KEY:
            return self.go_back()
        
        experience_index = int(experience_index)
        error_message = self.current_user.profile.delete_experience(experience_index)
        if error_message:
            print(error_message)
        else:
            print(EXPERIENCE_REMOVED_MESSAGE)
        
        return self.reload_screen()

    @screen
    def experience_screen(self):
        print("Experience", end="\n\n")
        print("0. Add experience")
        print("1. Delete experience")
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        elif option == "0":
            return self.add_experience_screen()

        elif option == "1":
            return self.delete_experience_screen()

        return self.reload_screen()

    @screen
    def education_screen(self):
        print("Education", end="\n\n")
        print("0. Add education")
        print("1. Delete education")
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        elif option == "0":
            return self.add_education_screen()

        elif option == "1":
            return self.delete_education_screen()

        return self.reload_screen()

    @screen
    def add_education_screen(self):
        print("Add Education", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        schoolName = input(TYPE_SCHOOL_NAME_MESSAGE)
        degree = input(TYPE_DEGREE_MESSAGE)
        yearsAttended = input(TYPE_YEARS_ATTENDED_MESSAGE)

        education = Education(
            schoolName,
            degree,
            yearsAttended,
        )

        error_message = self.current_user.profile.add_education(education)
        if error_message:
            print(error_message)
        else:
            print(EDUCATION_ADDED_MESSAGE)

        return self.go_back()

    @screen
    def delete_education_screen(self):
        print("Delete Education", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        print("Which education section would you like to delete?")
        for index, education in enumerate(self.current_user.profile.education):
            print(f"{index}. {education.degree} at {education.school_name} ", end="")
            print(education.years_attended)
        print("b. Go back")

        education_index = self.handle_input(SELECT_OPTION_MESSAGE, int)
        if education_index == GO_BACK_KEY:
            return self.go_back()
        
        education_index = int(education_index)
        error_message = self.current_user.profile.delete_education(education_index)
        if error_message:
            print(error_message)
        else:
            print(EDUCATION_REMOVED_MESSAGE)

        return self.reload_screen()

    @screen
    def edit_profile_title_screen(self):
        print("Edit profile title", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()
        
        if self.current_user.profile.title:
            print(f"Current title: {self.current_user.profile.title}")
            print(UPDATE_WARRNING)

        self.current_user.profile.title = input(TYPE_TITLE_MESSAGE)
        User.update_users_file()
        return self.go_back()
    
    @screen
    def edit_profile_major_screen(self):
        print("Edit profile major", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()

        if self.current_user.profile.major:
            print(f"Current major: {self.current_user.profile.major}")
            print(UPDATE_WARRNING)

        major = input(TYPE_MAJOR_MESSAGE)
        self.current_user.profile.major = str.title(major)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_university_screen(self):
        print("Edit profile university", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()
        
        if self.current_user.profile.university:
            print(f"Current university: {self.current_user.profile.university}")
            print(UPDATE_WARRNING)

        university = input(TYPE_NAME_OF_UNIVERSITY)
        self.current_user.profile.university = str.title(university)
        User.update_users_file()
        return self.go_back()
    
    @screen
    def edit_profile_summary_screen(self):
        print("Edit profile summary", end="\n\n")
        if not self.current_user.profile:
            self.current_user.profile = Profile()
        
        if self.current_user.profile.about:
            print(f"Current summary: {self.current_user.profile.about}")
            print(UPDATE_WARRNING)

        self.current_user.profile.about = input(TYPE_SUMMARY_MESSAGE)
        User.update_users_file()
        return self.go_back()

    @screen
    def edit_profile_screen(self):
        print("Edit Profile", end="\n\n")
        print("0. Title")
        print("1. Major")
        print("2. University Name")
        print("3. Summary")
        print("4. Experience")
        print("5. Education")
        print("b. Go Back")
        option = self.handle_input(EDIT_PROFILE_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.edit_profile_title_screen()
        elif option == "1":
            return self.edit_profile_major_screen()
        elif option == "2":
            return self.edit_profile_university_screen()
        elif option == "3":
            return self.edit_profile_summary_screen()
        elif option == "4":
            return self.experience_screen()
        elif option == "5":
            return self.education_screen()

        return self.reload_screen()

    @screen
    def view_profile_screen(self):
        print("Profile", end="\n\n")
        profile = self.current_user.profile
        
        if profile:
            print("\t\t\t\t\t\t\t\t\t\t\t", self.current_user.first_name, self.current_user.last_name)
            print("Title: ", profile.title)
            print("Major: ", profile.major)
            print("University: ", profile.university)
            print("Summary: ", profile.about)
            print("\nEXPERIENCE:\n")
            for experience in profile.experience:
                print("\tJob Title: ", experience.title)
                print("\tEmployer: ", experience.employer)
                print("\tDate Started: ", experience.date_started)
                print("\tDate Ended: ", experience.date_ended)
                print("\tLocation: ", experience.location)
                print("\tDescription:", experience.description)
                print("==========================")

            print("\nEDUCATION:\n")
            for education in profile.education:
                print("\tUniversity: ", education.school_name)
                print("\tDegree: ", education.degree)
                print("\tYears Attended:", education.years_attended)
                print("==========================")
        else:
            print(NO_PROFILE_YET_MESSAGE)

        option = self.handle_input(GO_BACK_MESSAGE)
        if option == "b":
            return self.go_back()

        return self.reload_screen()

    @screen
    def register_user_screen(self):
        print("Create Account", end="\n\n")
        first_name = input(TYPE_FIRST_NAME_MESSAGE)
        last_name = input(TYPE_LAST_NAME_MESSAGE)
        username = input(TYPE_USERNAME_MESSAGE)
        password = input(TYPE_PASSWORD_MESSAGE)
        user = User(username, password, first_name, last_name, LANGUAGES[0])

        error_message = user.save()
        if error_message == None:
            print(USER_CREATED_MESSAGE)

        else:
            print(error_message)

        return self.go_back()

    @screen
    def under_construction_screen(self):
        print(UNDER_CONSTRUCTION_MESSAGE, end="\n\n")
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def new_skills_screen(self):
        print("Learn a New Skill", end="\n\n")
        print(*[f"{index}: {skill}" for index, skill in enumerate(SKILLS)], sep="\n")
        print("b. Go back")
        option = self.handle_input(SELECT_NEW_SKILL_MESSAGE, int)

        if option == GO_BACK_KEY:
            return self.go_back()

        skill = int(option)
        if skill in range(len(SKILLS)):
            return self.under_construction_screen()

        print(f"\n{INVALID_SKILL_ERROR_MESSAGE}")
        return self.reload_screen()

    @screen
    def find_someone_screen(self):
        print("Find Someone You Know", end="\n\n")
        search_first = input(TYPE_FIRST_NAME_MESSAGE)
        search_last = input(TYPE_LAST_NAME_MESSAGE)
        user = User.find_by_name(search_first, search_last)

        if user == None:
            print(CONTACT_NOT_FOUND_MESSAGE)
            return self.go_back()

        print(CONTACT_FOUND_MESSAGE)
        if self.current_user != None:
            return self.go_back()

        # Removes this screen from the history
        self.history.pop()
        return self.join_your_friends_screen()

    @screen
    def join_your_friends_screen(self):
        print("Connect", end="\n\n")
        print("0. Login to an existing account to connect!")
        print("1. Sign up and join your friends!")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.login_screen()
        elif option == "1":
            return self.register_user_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def login_screen(self):
        print("Please enter your login information: ", end="\n\n")
        username = input(TYPE_USERNAME_MESSAGE)
        password = input(TYPE_PASSWORD_MESSAGE)
        user = User.login(username, password)
        if not user:
            print(LOGIN_ERROR_MESSAGE)
            return self.go_back()

        self.current_user = user
        print(LOGIN_SUCCESSFUL_MESSAGE)
        # Removes this screen from the history
        self.history.pop()
        return self.user_dashboard()

    @screen
    def play_video(self):
        print(VIDEO_PLAYNG_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def job_menu_screen(self):
        print("Job Search/Internship", end="\n\n")
        print("0. Post a Job")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.post_job()

        return self.reload_screen()

    @screen
    def post_job(self):
        print("Post a Job", end="\n\n")
        title = input(TYPE_JOB_TITLE_MESSAGE)
        description = input(TYPE_JOB_DESCRIPTION_MESSAGE)
        employer = input(TYPE_JOB_EMPLOYER_MESSAGE)
        location = input(TYPE_JOB_LOCATION_MESSAGE)
        salary = input(TYPE_JOB_SALARY_MESSAGE)

        new_job = Job(
            title,
            description,
            employer,
            location,
            salary,
            self.current_user.first_name,
            self.current_user.last_name,
        )

        error_message = new_job.save()
        if error_message == None:
            print(JOB_SAVED_MESSAGE)
        else:
            print(error_message)

        return self.go_back()

    @screen
    def guest_controls_screen(self):
        print("Guest controls", end="\n\n")
        email_toggle = "ON" if self.current_user.email_notifications else "OFF"
        sms_toggle = "ON" if self.current_user.sms_notifications else "OFF"
        targeted_ads_toggle = "ON" if self.current_user.targeted_ads else "OFF"

        print("Please select option if you would like to toggle feature ON/OFF")
        print("0. Email Notifications: ", email_toggle)
        print("1. SMS Notifications: ", sms_toggle)
        print("2. Targeted Advertisment: ", targeted_ads_toggle)
        print("b. Go Back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            self.current_user.toggle_email_notifications()
        elif option == "1":
            self.current_user.toggle_sms_notifications()
        elif option == "2":
            self.current_user.toggle_targeted_ads()
        else:
            print("Invalid choice. Try again.")

        return self.reload_screen()

    @screen
    def languages_screen(self):
        print("Languages screen", end="\n\n")
        print("You are currently using", self.current_user.app_language)
        for index, language in enumerate(LANGUAGES):
            print(f"{index}: {language}")
        print("b. Go Back")
        option = self.handle_input(SELECT_LANGUAGE_MESSAGE, int)

        if option == GO_BACK_KEY:
            return self.go_back()

        language_index = int(option)
        if language_index >= 0 and language_index < len(LANGUAGES):
            self.current_user.app_language = LANGUAGES[language_index]
            User.update_users_file()
        else:
            print("Invalid choice. Try again.")

        return self.reload_screen()

    @screen
    def copyright_notice_screen(self):
        print("Copyright notice", end="\n\n")
        print(textwrap.fill(App.copyright_notice, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def about_screen(self):
        print("About", end="\n\n")
        print(textwrap.fill(App.about_message, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def accessibility_screen(self):
        print("Accessibility", end="\n\n")
        print(textwrap.fill(App.accessibility_message, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def user_agreement_screen(self):
        print("User agreenment", end="\n\n")
        print(textwrap.fill(App.user_agreement, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def privacy_policy_screen(self):
        print("Privacy policy", end="\n\n")
        print(textwrap.fill(App.privacy_policy, TEXT_WIDTH))

        if self.current_user != None:
            print("0. Guest Controls")
            print("b. Go back")
            choice = self.handle_input(SELECT_OPTION_MESSAGE)

            if choice == "0":
                return self.guest_controls_screen()

        else:
            choice = self.handle_input(GO_BACK_MESSAGE)

        return self.handle_go_back(choice)

    @screen
    def cookie_policy_screen(self):
        print("Cookie policy", end="\n\n")
        print(textwrap.fill(App.cookie_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def copyright_policy_screen(self):
        print("Copyright policy", end="\n\n")
        print(textwrap.fill(App.copyright_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def brand_policy_screen(self):
        print("Brand policy", end="\n\n")
        print(textwrap.fill(App.brand_policy, TEXT_WIDTH))
        choice = self.handle_input(GO_BACK_MESSAGE)
        return self.handle_go_back(choice)

    @screen
    def important_links_screen(self):
        print("Important links", end="\n\n")
        print("0. Copyright Notice")
        print("1. About")
        print("2. Accessibility")
        print("3. User Agreement")
        print("4. Privacy Policy")
        print("5. Cookie Policy")
        print("6. Copyright Policy")
        print("7. Brand Policy")
        if self.current_user != None:
            print("8. Language")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.copyright_notice_screen()
        elif option == "1":
            return self.about_screen()
        elif option == "2":
            return self.accessibility_screen()
        elif option == "3":
            return self.user_agreement_screen()
        elif option == "4":
            return self.privacy_policy_screen()
        elif option == "5":
            return self.cookie_policy_screen()
        elif option == "6":
            return self.copyright_policy_screen()
        elif option == "7":
            return self.brand_policy_screen()
        elif option == "8" and self.current_user != None:
            return self.languages_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def useful_links_screen(self):
        print("Useful links", end="\n\n")
        print("0. General")
        print("1. Browse InCollege")
        print("2. Business Solutions")
        print("3. Directories")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.general_option_screen()
        elif option == "1":
            return self.under_construction_screen()
        elif option == "2":
            return self.under_construction_screen()
        elif option == "3":
            return self.under_construction_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def general_option_screen(self):
        print("General option", end="\n\n")
        print("0. Sign Up")
        print("1. Help Center")
        print("2. About")
        print("3. Press")
        print("4. Blog")
        print("5. Careers")
        print("6. Developers")
        print("b. Go back")
        option = self.handle_input(SELECT_OPTION_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()
        elif option == "0":
            return self.register_user_screen()
        elif option == "1":
            return self.help_center_screen()
        elif option == "2":
            return self.general_option_about_screen()
        elif option == "3":
            return self.press_screen()
        elif option == "4":
            return self.under_construction_screen()
        elif option == "5":
            return self.under_construction_screen()
        elif option == "6":
            return self.under_construction_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def help_center_screen(self):
        print("Help center", end="\n\n")
        print(HELP_CENTER_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def general_option_about_screen(self):
        print("About", end="\n\n")
        print(GENERAL_OPTION_ABOUT_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def press_screen(self):
        print("Press", end="\n\n")
        print(PRESS_MESSAGE)
        option = self.handle_input(GO_BACK_MESSAGE)

        if option == GO_BACK_KEY:
            return self.go_back()

        return self.reload_screen()

    @screen
    def main_menu(self):
        print(textwrap.fill(App.success_story, TEXT_WIDTH))
        print("\nWelcome to InCollege!", end="\n\n")
        print("0. Login")
        print("1. Create account")
        print("2. Video: Why InCollege is the best option for you")
        print("3. Connect with Someone You Know")
        print("4. Useful Links")
        print("5. InCollege Important Links")
        print("b. Exit")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            return self.go_back()
        elif choice == "0":
            return self.login_screen()
        elif choice == "1":
            return self.register_user_screen()
        elif choice == "2":
            return self.play_video()
        elif choice == "3":
            return self.find_someone_screen()
        elif choice == "4":
            return self.useful_links_screen()
        elif choice == "5":
            return self.important_links_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()

    @screen
    def user_dashboard(self):
        print("Welcome to InCollege!", end="\n\n")
        print("0. Job Search/Internship")
        print("1. Find Someone You Know")
        print("2. Learn a New Skill")
        print("3. Useful Links")
        print("4. InCollege Important Links")
        print("5. Edit Profile")
        print("6. View Profile")
        print("b. Sign Out")
        choice = self.handle_input(SELECT_OPTION_MESSAGE, int)

        if choice == GO_BACK_KEY:
            self.current_user = None
            return self.go_back()
        elif choice == "0":
            return self.job_menu_screen()
        elif choice == "1":
            return self.find_someone_screen()
        elif choice == "2":
            return self.new_skills_screen()
        elif choice == "3":
            return self.useful_links_screen()
        elif choice == "4":
            return self.important_links_screen()
        elif choice == "5":
            return self.edit_profile_screen()
        elif choice == "6":
            return self.view_profile_screen()

        print("Invalid choice. Try again.")
        return self.reload_screen()


if __name__ == "__main__":
    # Loads the registered users to memory
    User.load_users_file()
    # Loads the saved jobs to memory
    Job.load_jobs_file()
    # Loads the success story
    App.load_success_story()
    # Loads the copyright notice
    App.load_copyright_notice()
    # Loads the about message
    App.load_about_message()
    # Loads the accessibility message
    App.load_accessibility_message()
    # Loads the user agreement
    App.load_user_agreement()
    # Loads the privacy policy
    App.load_privacy_policy()
    # Loads the cookie policy
    App.load_cookie_policy()
    # Loads the copyright policy
    App.load_copyright_policy()
    # Loads the brand policy
    App.load_brand_policy()
    # Starts the app
    app = App()
    app.main_menu()
