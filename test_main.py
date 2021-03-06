import builtins
import io

from collections import deque
from job import JOB_NOT_FOUND_ERROR_MESSAGE, MAX_ALLOWED_JOBS_ERROR_MESSAGE, Job
from main import CONNECTION_ACEPTED_MESSAGE, CONNECTION_REJECTED_MESSAGE, CONNECTION_REQUESTED_MESSAGE, CONTACT_FOUND_MESSAGE,\
    CONTACT_NOT_FOUND_MESSAGE, DISCONNECTED_MESSAGE, DO_NOT_FORGET_PROFILE_MESSAGE, EDIT_PROFILE_MESSAGE, EDUCATION_ADDED_MESSAGE,\
    EDUCATION_REMOVED_MESSAGE, EXPERIENCE_ADDED_MESSAGE, EXPERIENCE_REMOVED_MESSAGE, GENERAL_OPTION_ABOUT_MESSAGE, HELP_CENTER_MESSAGE,\
    JOB_DELETED_MESSAGE, JOB_SAVED_MESSAGE, LANGUAGES, LAST_APPLICATION_SEVEN_DAYS_AGO_MESSAGE, LOGIN_ERROR_MESSAGE,\
    LOGIN_SUCCESSFUL_MESSAGE, NO_PROFILE_YET_MESSAGE, PENDING_FRIEND_REQUEST_MESSAGE, PRESS_MESSAGE, SELECT_LANGUAGE_MESSAGE,\
    SELECT_SUSCRIPTION_TYPE, TYPE_DATE_ENDED_MESSAGE, TYPE_DATE_STARTED_MESSAGE, TYPE_DEGREE_MESSAGE, TYPE_FIRST_NAME_MESSAGE, \
    TYPE_JOB_DESCRIPTION_MESSAGE, TYPE_JOB_EMPLOYER_MESSAGE, TYPE_JOB_LOCATION_MESSAGE, TYPE_JOB_SALARY_MESSAGE, TYPE_JOB_TITLE_MESSAGE,\
    TYPE_LAST_NAME_MESSAGE, TYPE_MAJOR_MESSAGE, TYPE_NAME_OF_UNIVERSITY, TYPE_SCHOOL_NAME_MESSAGE, TYPE_SUMMARY_MESSAGE,\
    TYPE_TITLE_MESSAGE, TYPE_YEARS_ATTENDED_MESSAGE, UNREAD_MESSAGES_MESSAGE, UPDATE_WARRNING, VIDEO_PLAYNG_MESSAGE, GO_BACK_KEY,\
    GO_BACK_MESSAGE, INVALID_INPUT_ERROR_MESSAGE, SELECT_NEW_SKILL_MESSAGE, SELECT_OPTION_MESSAGE, SKILLS, TYPE_PASSWORD_MESSAGE,\
    TYPE_USERNAME_MESSAGE, UNDER_CONSTRUCTION_MESSAGE, USER_CREATED_MESSAGE, screen, App
from message import Message
from user import CONNECT_TO_SELF_ERROR_MESSAGE, CONNECTION_NOT_FOUND_ERROR_MESSAGE, CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE,\
    PASSWORD_LENGTH_ERROR_MESSAGE, STANDARD_TIER_NAME, User
from profile import Profile, EXPERIENCE_INDEX_OUT_OF_RANGE, EDUCATION_INDEX_OUT_OF_RANGE

def test_screen():
    return_true = lambda app: app
    return_true.__name__ = "return_true"
    wrapper = screen(return_true)

    app = App()
    result = wrapper(app)
    assert result == app
    assert app.history[-1] == (return_true.__name__, ())
    assert len(app.history) == 1

def test__init__():
    app = App()
    assert type(app.history) == deque
    assert len(app.history) == 0
    assert app.current_user == None

def test_load_sucess_story(monkeypatch):
    story = "Success story"
    # Create in-memory string file
    story_file = io.StringIO(story)

    def mock_open(file_name):
        assert file_name == App.SUCCESS_STORY_FILE_NAME
        return story_file
    
    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_success_story()
    assert App.success_story == story

def test_load_copyright_notice(monkeypatch):
    copyright_notice = "Copyright notice"
    # Create in-memory string file
    copyright_notice_file = io.StringIO(copyright_notice)

    def mock_open(file_name):
        assert file_name == App.COPYRIGHT_NOTICE_FILE_NAME
        return copyright_notice_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_copyright_notice()
    assert App.copyright_notice == copyright_notice

def test_load_about_message(monkeypatch):
    about_message = "About message"
    # Create in-memory string file
    about_message_file = io.StringIO(about_message)

    def mock_open(file_name):
        assert file_name == App.ABOUT_MESSAGE_FILE_NAME
        return about_message_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_about_message()
    assert App.about_message == about_message

def test_load_accessibility_message(monkeypatch):
    accessibility_message = "Accessibility message"
    # Create in-memory string file
    accessibility_message_file = io.StringIO(accessibility_message)

    def mock_open(file_name):
        assert file_name == App.ACCESSIBILITY_MESSAGE_FILE_NAME
        return accessibility_message_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_accessibility_message()
    assert App.accessibility_message == accessibility_message

def test_load_user_agreement(monkeypatch):
    user_agreement = "user agreement"
    # Create in-memory string file
    user_agreement_file = io.StringIO(user_agreement)

    def mock_open(file_name):
        assert file_name == App.USER_AGREEMENT_FILE_NAME
        return user_agreement_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_user_agreement()
    assert App.user_agreement == user_agreement

def test_load_privacy_policy(monkeypatch):
    privacy_policy = "Privacy policy"
    # Create in-memory string file
    privacy_policy_file = io.StringIO(privacy_policy)

    def mock_open(file_name):
        assert file_name == App.PRIVACY_POLICY_FILE_NAME
        return privacy_policy_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_privacy_policy()
    assert App.privacy_policy == privacy_policy

def test_load_cookie_policy(monkeypatch):
    cookie_policy = "Cookie policy"
    # Create in-memory string file
    cookie_policy_file = io.StringIO(cookie_policy)

    def mock_open(file_name):
        assert file_name == App.COOKIE_POLICY_FILE_NAME
        return cookie_policy_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_cookie_policy()
    assert App.cookie_policy == cookie_policy

def test_load_copyright_policy(monkeypatch):
    copyright_policy = "Copyright policy"
    # Create in-memory string file
    copyright_policy_file = io.StringIO(copyright_policy)

    def mock_open(file_name):
        assert file_name == App.COPYRIGHT_POLICY_FILE_NAME
        return copyright_policy_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_copyright_policy()
    assert App.copyright_policy == copyright_policy

def test_load_brand_policy(monkeypatch):
    brand_policy = "Brand policy"
    # Create in-memory string file
    brand_policy_file = io.StringIO(brand_policy)

    def mock_open(file_name):
        assert file_name == App.BRAND_POLICY_FILE_NAME
        return brand_policy_file

    # Replaces open built-in method by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    App.load_brand_policy()
    assert App.brand_policy == brand_policy

def test_go_back():
    app = App()

    # Test with valid history
    app.return_true = lambda: True
    app.return_true.__name__ = "return_true"
    app.history.extend([(app.return_true.__name__, ()), None])

    result = app.go_back()
    assert result == True
    assert len(app.history) == 0

    # Test with single history
    app.history.extend([(app.return_true.__name__, ())])

    result = app.go_back()
    assert result == None
    assert len(app.history) == 0

    # Test with empty history
    result = app.go_back()
    assert result == None
    assert len(app.history) == 0

def test_reload_screen():
    app = App()

    # Test with valid history
    app.return_true = lambda: True
    app.return_true.__name__ = "return_true"

    app.return_false = lambda: False
    app.return_false.__name__ = "return_false"

    app.history.extend([(app.return_false.__name__, (1)), (app.return_true.__name__, ())])

    result = app.reload_screen()
    assert result == True
    assert len(app.history) == 1
    assert app.history[-1] == (app.return_false.__name__, (1))

    # Test with empty history
    app.history.clear()
    result = app.reload_screen()
    assert result == None

def test_handle_input(monkeypatch, capfd):
    app = App()
    test_prompt = "Type something: "
    
    # Test valid input

    def mock_input(*args):
        nonlocal test_prompt, input_counter, input_value
        input_counter += 1

        prompt = args[0]
        assert test_prompt == prompt
        return input_value

    # Replaces input buildt-in input with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)

    input_counter = 0
    input_value = "1"
    result = app.handle_input(test_prompt, int)
    assert result == input_value
    assert input_counter == 1

    input_counter = 0
    result = app.handle_input(test_prompt, str)
    assert result == input_value
    assert input_counter == 1

    input_value = GO_BACK_KEY
    input_counter = 0
    result = app.handle_input(test_prompt, int)
    assert result == input_value
    assert input_counter == 1

    # Test invalid input

    def wrong_input(*args):
        nonlocal input_counter

        input_counter += 1
        if input_counter == 1:
            return "h"
        else:
            # Reads standard output
            out, _ = capfd.readouterr()
            assert INVALID_INPUT_ERROR_MESSAGE in out
            prompt = args[0]
            assert prompt == test_prompt
            return "1"

    # Replaces python builtin input function with wrong_input function
    monkeypatch.setattr(builtins, "input", wrong_input)

    input_counter = 0
    result = app.handle_input(test_prompt, int)
    assert result == "1"
    assert input_counter == 2

def test_handle_go_back(monkeypatch):
    app = App()

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    
    # Test go back
    result = app.handle_go_back(GO_BACK_KEY)
    assert result == "go_back"

    # Test reload
    result = app.handle_go_back("h")
    assert result == "reload"

def test_add_experience_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_counter        
        input_counter += 1
        
        prompt = args[0]
        if prompt == TYPE_JOB_TITLE_MESSAGE:
            return "SWE"
        
        if prompt == TYPE_JOB_EMPLOYER_MESSAGE:
            return "USF"
        
        if prompt == TYPE_DATE_STARTED_MESSAGE:
            return "2020"
        
        if prompt == TYPE_DATE_ENDED_MESSAGE:
            return "2021"
        
        if prompt == TYPE_JOB_LOCATION_MESSAGE:
            return "Tampa"
        
        if prompt == TYPE_JOB_DESCRIPTION_MESSAGE:
            return "LOL"
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Successful test

    # Replaces Profile add_experience by a lambda function that returns None
    monkeypatch.setattr(Profile, "add_experience", lambda *args: None)

    input_counter = 0
    result = app.add_experience_screen()
    assert input_counter == 6
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert EXPERIENCE_ADDED_MESSAGE in out

    # Unsuccessful test

    # Replaces Profile add_experience by a lambda function that returns MAX_ALLOWED_JOBS_ERROR_MESSAGE
    monkeypatch.setattr(Profile, "add_experience", lambda *args: MAX_ALLOWED_JOBS_ERROR_MESSAGE)

    input_counter = 0
    result = app.add_experience_screen()
    assert input_counter == 6
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert MAX_ALLOWED_JOBS_ERROR_MESSAGE in out

def test_delete_experience_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value
        prompt = args[1]
        assert SELECT_OPTION_MESSAGE == prompt
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.delete_experience_screen()
    assert result == "go_back"

    # Test valid option
    
    # Replaces Profile delete_experience by a lambda function that returns None
    monkeypatch.setattr(Profile, "delete_experience", lambda *args: None)

    input_value = "1"
    result = app.delete_experience_screen()
    assert result == "reload"
    out, _ = capfd.readouterr()
    assert EXPERIENCE_REMOVED_MESSAGE in out

    # Test invalid

    # Replaces Profile delete_experience by a lambda function that returns EXPERIENCE_INDEX_OUT_OF_RANGE
    monkeypatch.setattr(Profile, "delete_experience", lambda *args: EXPERIENCE_INDEX_OUT_OF_RANGE)

    input_value = "-1"
    result = app.delete_experience_screen()
    assert result == "reload"
    out, _ = capfd.readouterr()
    assert EXPERIENCE_INDEX_OUT_OF_RANGE in out

def test_experience_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value
        
        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App add_experience_screen by a lambda function that returns "add"
    monkeypatch.setattr(App, "add_experience_screen", lambda *arg: "add")
    # Replaces App delete_experience_screen by a lambda function that returns "delete"
    monkeypatch.setattr(App, "delete_experience_screen", lambda *arg: "delete")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.experience_screen()
    assert result == "go_back"

    # Test add experience
    input_value = "0"
    result = app.experience_screen()
    assert result == "add"

    # Test remove experience
    input_value = "1"
    result = app.experience_screen()
    assert result == "delete"

    # Test reload
    input_value = "-1"
    result = app.experience_screen()
    assert result == "reload"

def test_education_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value
        
        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App add_education_screen by a lambda function that returns "add"
    monkeypatch.setattr(App, "add_education_screen", lambda *arg: "add")
    # Replaces App delete_education_screen by a lambda function that returns "delete"
    monkeypatch.setattr(App, "delete_education_screen", lambda *arg: "delete")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.education_screen()
    assert result == "go_back"

    # Test add experience
    input_value = "0"
    result = app.education_screen()
    assert result == "add"

    # Test remove experience
    input_value = "1"
    result = app.education_screen()
    assert result == "delete"

    # Test reload
    input_value = "-1"
    result = app.education_screen()
    assert result == "reload"

def test_add_education_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_counter        
        input_counter += 1
        
        prompt = args[0]
        if prompt == TYPE_SCHOOL_NAME_MESSAGE:
            return "USF"
        
        if prompt == TYPE_DEGREE_MESSAGE:
            return "BSc"
        
        if prompt == TYPE_YEARS_ATTENDED_MESSAGE:
            return "2020-2021"
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Successful test

    # Replaces Profile add_education by a lambda function that returns None
    monkeypatch.setattr(Profile, "add_education", lambda *args: None)

    input_counter = 0
    result = app.add_education_screen()
    assert input_counter == 3
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert EDUCATION_ADDED_MESSAGE in out

    # Unsuccessful test

    # Replaces Profile add_education by a lambda function that returns Error
    monkeypatch.setattr(Profile, "add_education", lambda *args: "Error")

    input_counter = 0
    result = app.add_education_screen()
    assert input_counter == 3
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert "Error" in out

def test_delete_education_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value
        prompt = args[1]
        assert SELECT_OPTION_MESSAGE == prompt
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.delete_education_screen()
    assert result == "go_back"

    # Test valid option
    
    # Replaces Profile delete_education by a lambda function that returns None
    monkeypatch.setattr(Profile, "delete_education", lambda *args: None)

    input_value = "1"
    result = app.delete_education_screen()
    assert result == "reload"
    out, _ = capfd.readouterr()
    assert EDUCATION_REMOVED_MESSAGE in out

    # Test invalid

    # Replaces Profile delete_education by a lambda function that returns EDUCATION_INDEX_OUT_OF_RANGE
    monkeypatch.setattr(Profile, "delete_education", lambda *args: EDUCATION_INDEX_OUT_OF_RANGE)

    input_value = "-1"
    result = app.delete_education_screen()
    assert result == "reload"
    out, _ = capfd.readouterr()
    assert EDUCATION_INDEX_OUT_OF_RANGE in out

def test_edit_profile_title_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value

        prompt = args[0]
        if prompt == TYPE_TITLE_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User update_users_file function with a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda *args: None)

    # Test without update warning
    input_value = "hello"
    app.edit_profile_title_screen()
    assert app.current_user.profile.title == input_value
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING not in out

    # Test with update warning
    input_value = "world"
    app.edit_profile_title_screen()
    assert app.current_user.profile.title == input_value
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING in out

def test_edit_profile_major_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value

        prompt = args[0]
        if prompt == TYPE_MAJOR_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User update_users_file function with a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda *args: None)

    # Test without update warning
    input_value = "hello"
    app.edit_profile_major_screen()
    assert app.current_user.profile.major == str.title(input_value)
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING not in out

    # Test with update warning
    input_value = "world"
    app.edit_profile_major_screen()
    assert app.current_user.profile.major == str.title(input_value)
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING in out

def test_edit_profile_university_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value

        prompt = args[0]
        if prompt == TYPE_NAME_OF_UNIVERSITY:
            return input_value
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User update_users_file function with a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda *args: None)

    # Test without update warning
    input_value = "hello"
    app.edit_profile_university_screen()
    assert app.current_user.profile.university == str.title(input_value)
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING not in out

    # Test with update warning
    input_value = "world"
    app.edit_profile_university_screen()
    assert app.current_user.profile.university == str.title(input_value)
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING in out

def test_edit_profile_summary_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value

        prompt = args[0]
        if prompt == TYPE_SUMMARY_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User update_users_file function with a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda *args: None)

    # Test without update warning
    input_value = "hello"
    app.edit_profile_summary_screen()
    assert app.current_user.profile.about == input_value
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING not in out

    # Test with update warning
    input_value = "world"
    app.edit_profile_summary_screen()
    assert app.current_user.profile.about == input_value
    out, _ = capfd.readouterr()
    assert UPDATE_WARRNING in out

def test_edit_profile_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value
        
        prompt = args[1]
        assert prompt == EDIT_PROFILE_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App edit_profile_title_screen function by a lambda function that returns profile_title
    monkeypatch.setattr(App, "edit_profile_title_screen", lambda *args: "profile_title")
    # Replaces App edit_profile_major_screen function by a lambda function that returns profile_major
    monkeypatch.setattr(App, "edit_profile_major_screen", lambda *args: "profile_major")
    # Replaces App edit_profile_university_screen function by a lambda function that returns profile_university
    monkeypatch.setattr(App, "edit_profile_university_screen", lambda *args: "profile_university")
    # Replaces App edit_profile_summary_screen function by a lambda function that returns profile_summary
    monkeypatch.setattr(App, "edit_profile_summary_screen", lambda *args: "profile_summary")
    # Replaces App experience_screen function by a lambda function that returns experience
    monkeypatch.setattr(App, "experience_screen", lambda *args: "experience")
    # Replaces App education_screen function by a lambda function that returns education
    monkeypatch.setattr(App, "education_screen", lambda *args: "education")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.edit_profile_screen()
    assert result == "go_back"

    # Test profile title
    input_value = "0"
    result = app.edit_profile_screen()
    assert result == "profile_title"

    # Test profile major  
    input_value = "1"
    result = app.edit_profile_screen()
    assert result == "profile_major"

    # Test profile university
    input_value = "2"
    result = app.edit_profile_screen()
    assert result == "profile_university"

    # Test profile summary
    input_value = "3"    
    result = app.edit_profile_screen()
    assert result == "profile_summary"

    # Test experience
    input_value = "4"    
    result = app.edit_profile_screen()
    assert result == "experience"

    # Test education
    input_value = "5"    
    result = app.edit_profile_screen()
    assert result == "education"

    # Test reload
    input_value = "-1"
    result = app.edit_profile_screen()
    assert result == "reload"

def test_show_profile_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test profile available
    input_value = GO_BACK_KEY
    user.profile = Profile()
    result = app.show_profile_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert NO_PROFILE_YET_MESSAGE not in out

    # Test no profile and no logged in go back
    input_value = GO_BACK_KEY
    user.profile = None
    result = app.show_profile_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert NO_PROFILE_YET_MESSAGE not in out

    # Test no profile and logged in go back
    app.current_user = user
    input_value = GO_BACK_KEY
    user.profile = None
    result = app.show_profile_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert NO_PROFILE_YET_MESSAGE in out

    # Test no profile reload
    input_value = "h"
    result = app.show_profile_screen(user)
    assert result == "reload"
    out, _ = capfd.readouterr()
    assert NO_PROFILE_YET_MESSAGE in out

def test_register_user_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_counter
        input_counter += 1

        prompt = args[0]
        if prompt == SELECT_SUSCRIPTION_TYPE:
            return "0"

        if prompt == TYPE_USERNAME_MESSAGE:
            return "hello"

        if prompt == TYPE_PASSWORD_MESSAGE:
            return "12345678"

        if prompt == TYPE_FIRST_NAME_MESSAGE:
            return "John"

        if prompt == TYPE_LAST_NAME_MESSAGE:
            return "Connor"
    
    def broadcast_notification(*args):
        nonlocal broadcast_notification_execution

        assert len(args) == 1
        broadcast_notification_execution += 1

    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User broadcast_new_user_notification method by broadcast_notification function
    monkeypatch.setattr(User, "broadcast_new_user_notification", broadcast_notification)
    
    # Test valid input
    
    # Replaces User save function with a lambda function that returns None
    monkeypatch.setattr(User, "save", lambda *args: None)
    input_counter = 0
    broadcast_notification_execution = 0
    result = app.register_user_screen()
    assert result == "go_back"
    assert input_counter == 5
    assert broadcast_notification_execution == 1
    out, _ = capfd.readouterr()
    assert USER_CREATED_MESSAGE in out

    # Test wrong input

    # Replaces User save function with a lambda function that returns a message
    monkeypatch.setattr(User, "save", lambda *args: PASSWORD_LENGTH_ERROR_MESSAGE)
    input_counter = 0
    broadcast_notification_execution = 0
    result = app.register_user_screen()
    assert result == "go_back"
    assert input_counter == 5
    assert broadcast_notification_execution == 0
    out, _ = capfd.readouterr()
    assert PASSWORD_LENGTH_ERROR_MESSAGE in out

def test_under_construction_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert UNDER_CONSTRUCTION_MESSAGE in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    
    # Test go back
    input_value = GO_BACK_KEY
    result = app.under_construction_screen()
    assert result == "go_back"

    # Test reload
    input_value = "h"
    result = app.under_construction_screen()
    assert result == "reload"

def test_new_skills_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        for skill in SKILLS:
            assert skill in out

        prompt = args[1]
        assert SELECT_NEW_SKILL_MESSAGE == prompt
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    # Replaces App under_construction_screen function with a lambda function that returns under_construction
    monkeypatch.setattr(App, "under_construction_screen", lambda *args: "under_construction")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.new_skills_screen()
    assert result == "go_back"

    # Test under construction
    input_value = "1"
    result = app.new_skills_screen()
    assert result == "under_construction"

    # Test reload
    input_value = "-1"
    result = app.new_skills_screen()
    assert result == "reload"

def test_find_someone_screen(monkeypatch, capfd):
    app = App()

    input_counter = 0
    def mock_input(*args):
        nonlocal input_counter        
        input_counter += 1
        
        prompt = args[0]
        if prompt == TYPE_FIRST_NAME_MESSAGE:
            return "Jhon"
        
        if prompt == TYPE_LAST_NAME_MESSAGE:
            return "Connor"
    
    # Replaces input buildt-in function by mock_input
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces the App join_your_friends_screen method by a lambda function that returns
    # join_your_friends
    monkeypatch.setattr(App, "join_your_friends_screen", lambda *args: "join_your_friends")
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test user found

    # Replaces find_by_name User method by a lambda function that returns a user
    user = User("Testing", User.hash_password("Testing@12"), "Jhonn", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    monkeypatch.setattr(User, "find_by_name", lambda *args: user)

    # Test join your friends
    input_counter = 0
    assert app.current_user == None
    result = app.find_someone_screen()
    assert result == "join_your_friends"
    out, _ = capfd.readouterr()
    assert CONTACT_FOUND_MESSAGE in out
    assert input_counter == 2
    assert len(app.history) == 0

    # Test go back
    input_counter = 0
    app.current_user = user
    result = app.find_someone_screen()
    assert result == "go_back"
    assert input_counter == 2

    # Test user not found

    # Replaces find_by_name User method by a lambda function that returns None
    monkeypatch.setattr(User, "find_by_name", lambda *args: None)

    input_counter = 0
    result = app.find_someone_screen()
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONTACT_NOT_FOUND_MESSAGE in out
    assert input_counter == 2

def test_join_your_friends_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value
        
        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App login_screen method by a lambda function that returns log_in
    monkeypatch.setattr(App, "login_screen", lambda *args: "login")
    # Replaces App register_user_screen method by a lambda function that returns register_user
    monkeypatch.setattr(App, "register_user_screen", lambda *args: "register_user")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.join_your_friends_screen()
    assert result == "go_back"   

    # Test login
    input_value = "0"
    result = app.join_your_friends_screen()
    assert result == "login"

    # Test register user
    input_value = "1"
    result = app.join_your_friends_screen()
    assert result == "register_user"

    # Test reload
    input_value = "h"
    result = app.join_your_friends_screen()
    assert result == "reload"

def test_login_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "Jhonn", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)

    def mock_input(*args):
        nonlocal input_counter
        input_counter += 1

        prompt = args[0]
        if prompt == TYPE_USERNAME_MESSAGE:
            return "hello"

        if prompt == TYPE_PASSWORD_MESSAGE:
            return "12345678"

    # Replaces input buildt-in function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App user_dashboard function with a lambda function that returns user_dashboard
    monkeypatch.setattr(App, "user_dashboard", lambda *args: "user_dashboard")

    User.users = {
        "Testing": user,
    }

    # Test login suscefful
    monkeypatch.setattr(User, "login", lambda *args: User.users["Testing"])    
    assert app.current_user == None
    input_counter = 0
    result = app.login_screen()
    assert input_counter == 2
    assert result == "user_dashboard"
    out, _ = capfd.readouterr()
    assert app.current_user == User.users["Testing"]
    assert LOGIN_SUCCESSFUL_MESSAGE in out
    assert len(app.history) == 0

    # Test login unsuccessful
    monkeypatch.setattr(User, "login", lambda *args: None)
    app.current_user = None
    input_counter = 0
    result = app.login_screen()
    assert input_counter == 2
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert app.current_user == None
    assert LOGIN_ERROR_MESSAGE in out

def test_play_video(monkeypatch, capfd):
    app = App()    

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert VIDEO_PLAYNG_MESSAGE in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.play_video()
    assert result == "go_back"

    # Test reload
    input_value = "-1"
    result = app.play_video()
    assert result == "reload"

def test_job_menu_screen(monkeypatch):
    app = App()
    user = User("Testing", "Testing@12", "Jhonn", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user 

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App list_all_jobs_screen method by a lambda function that returns list_all_jobs_screen
    monkeypatch.setattr(App, "list_all_jobs_screen", lambda *args: "list_all_jobs_screen")
    # Replaces App post_job method by a lambda function that returns post_job
    monkeypatch.setattr(App, "post_job", lambda *args: "post_job")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.job_menu_screen()
    assert result == "go_back"

    # Test list all jobs
    input_value = "0"
    result = app.job_menu_screen()
    assert result == "list_all_jobs_screen"

    # Test post job
    input_value = "1"
    result = app.job_menu_screen()
    assert result == "post_job"

    # Test reload
    input_value = "-1"
    result = app.job_menu_screen()
    assert result == "reload"

def test_post_job(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "Jhonn", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(prompt):
        nonlocal input_counter
        input_counter += 1

        if prompt == TYPE_JOB_TITLE_MESSAGE:
            return "Software Engineer"
        
        if prompt == TYPE_JOB_DESCRIPTION_MESSAGE:
            return "Just code!"
        
        if prompt == TYPE_JOB_EMPLOYER_MESSAGE:
            return "USF"
        
        if prompt == TYPE_JOB_LOCATION_MESSAGE:
            return "Tampa, FL"
        
        if prompt == TYPE_JOB_SALARY_MESSAGE:
            return "80000"
    
    def broadcast_notification(*args):
        nonlocal broadcast_notification_execution

        assert len(args) == 2
        broadcast_notification_execution += 1
    
    # Replaces input buildt-in function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User broadcast_new_job_notification method by broadcast_notification function
    monkeypatch.setattr(User, "broadcast_new_job_notification", broadcast_notification)

    # Test save successful

    # Replaces Job save method by a lambda function that returns None
    monkeypatch.setattr(Job, "save", lambda *args: None)
    input_counter = 0
    broadcast_notification_execution = 0
    result = app.post_job()
    assert input_counter == 5
    assert result == "go_back"
    assert broadcast_notification_execution == 1
    out, _ = capfd.readouterr()
    assert JOB_SAVED_MESSAGE in out 

    # Test save unsuccessful

    # Replaces Job save method by a lambda function that returns MAX_ALLOWED_JOBS_ERROR_MESSAGE
    monkeypatch.setattr(Job, "save", lambda *args: MAX_ALLOWED_JOBS_ERROR_MESSAGE)
    input_counter = 0
    broadcast_notification_execution = 0
    result = app.post_job()
    assert input_counter == 5
    assert broadcast_notification_execution == 0
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert MAX_ALLOWED_JOBS_ERROR_MESSAGE in out

def test_delete_job_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "Jhonn", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user
    job = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")

    def broadcast_notification(*args):
        nonlocal broadcast_notification_execution

        assert len(args) == 2
        broadcast_notification_execution += 1

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces user broadcast_job_applied_deleted_notification method by broadcast_notification function
    monkeypatch.setattr(User, "broadcast_job_applied_deleted_notification", broadcast_notification)

    # Test deleted successfully

    # Replaces Job delete method by a lambda function that returns None
    monkeypatch.setattr(Job, "delete", lambda *args: None)
    broadcast_notification_execution = 0
    result =  app.delete_job_screen(job)
    assert result == "go_back"
    assert broadcast_notification_execution == 1
    out, _ = capfd.readouterr()
    assert JOB_DELETED_MESSAGE in out

    # Test error
    
    # Replaces Job delete method by a lambda function that returns None
    monkeypatch.setattr(Job, "delete", lambda *args: JOB_NOT_FOUND_ERROR_MESSAGE)
    broadcast_notification_execution = 0
    result =  app.delete_job_screen(job)
    assert result == "go_back"
    assert broadcast_notification_execution == 0
    out, _ = capfd.readouterr()
    assert JOB_NOT_FOUND_ERROR_MESSAGE in out


def test_guest_controls_screen(monkeypatch):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user
    executed = ""
    
    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    def mock_toggle_email_notifications(*args):
        nonlocal executed
        executed = "email_notifications"

    def mock_toggle_sms_notifications(*args):
        nonlocal executed
        executed = "sms_notifications"
    
    def mock_toggle_targeted_ads(*args):
        nonlocal executed
        executed = "targeted_ads"
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces User toggle_email_notifications method by mock_toggle_email_notifications
    monkeypatch.setattr(User, "toggle_email_notifications", mock_toggle_email_notifications)
    # Replaces User toggle_sms_notifications method by mock_toggle_sms_notifications
    monkeypatch.setattr(User, "toggle_sms_notifications", mock_toggle_sms_notifications)
    # Replaces user toggle_targeted_ads method by mock_toggle_targeted_ads
    monkeypatch.setattr(User, "toggle_targeted_ads", mock_toggle_targeted_ads)
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.guest_controls_screen()
    assert result == "go_back"
    assert executed == ""

    # Test toggle email notifications
    input_value = "0"      
    result = app.guest_controls_screen()
    assert result == "reload"
    assert executed == "email_notifications"

    # Test toggle SMS notifications
    input_value = "1"
    result = app.guest_controls_screen()
    assert result == "reload"
    assert executed == "sms_notifications"

    # Test toggle targeted adds
    input_value = "2"
    result = app.guest_controls_screen()
    assert result == "reload"
    assert executed == "targeted_ads"

    # Test reload
    input_value = "-1"    
    result = app.guest_controls_screen()
    assert result == "reload"
    
def test_languages_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        for language in LANGUAGES:
            assert language in out

        prompt = args[1]
        assert SELECT_LANGUAGE_MESSAGE == prompt
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    # Replaces User update_users_file function with a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda *args: None)

    # Test go back
    input_value = GO_BACK_KEY
    result = app.languages_screen()
    assert result == "go_back"

    # Test update language
    for index, language in enumerate(LANGUAGES):
        input_value = str(index)
        result = app.languages_screen()
        assert result == "reload"
        assert app.current_user.app_language == language

    # Test reload
    input_value = "-1"
    result = app.languages_screen()
    assert result == "reload"

def test_copyright_notice_screen(monkeypatch, capfd):
    app = App()
    App.copyright_notice = "Copyright notice"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.copyright_notice in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App copyright_notice method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.copyright_notice_screen()
    assert result == "handle_go_back"

def test_about_screen(monkeypatch, capfd):
    app = App()
    App.about_message = "About message"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.about_message in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App about_message method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.about_screen()
    assert result == "handle_go_back"

def test_accessibility_screen(monkeypatch, capfd):
    app = App()
    App.accessibility_message = "Accessibility message"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.accessibility_message in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App accessibility_message method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.accessibility_screen()
    assert result == "handle_go_back"

def test_user_agreement_screen(monkeypatch, capfd):
    app = App()
    App.user_agreement = "User agreement"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.user_agreement in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App user_agreement method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.user_agreement_screen()
    assert result == "handle_go_back"

def test_privacy_policy_screen(monkeypatch, capfd):
    app = App()
    App.privacy_policy = "Privacy policy"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.privacy_policy in out
        prompt = args[1]
        assert prompt in [GO_BACK_MESSAGE, SELECT_OPTION_MESSAGE]
        return input_value

    # Replaces App privacy_policy method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App guest_controls_screen method by a lambda function that returns guest_controls
    monkeypatch.setattr(App, "guest_controls_screen", lambda *args: "guest_controls")
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test guest controls
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user
    input_value = "0"
    result = app.privacy_policy_screen()
    assert result == "guest_controls"

    # Test go back
    input_value = GO_BACK_KEY
    result = app.privacy_policy_screen()
    assert result == "handle_go_back"
    
    # Test user not logged in
    app.current_user = None
    input_value = "h"
    result = app.privacy_policy_screen()
    assert result == "handle_go_back"

def test_cookie_policy_screen(monkeypatch, capfd):
    app = App()
    App.cookie_policy = "Cookie policy"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.cookie_policy in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App cookie_policy method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.cookie_policy_screen()
    assert result == "handle_go_back"

def test_copyright_policy_screen(monkeypatch, capfd):
    app = App()
    App.copyright_policy = "Copyright policy"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.copyright_policy in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App copyright_policy method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.copyright_policy_screen()
    assert result == "handle_go_back"

def test_brand_policy_screen(monkeypatch, capfd):
    app = App()
    App.brand_policy = "Brand policy"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.brand_policy in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App brand_policy method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App handle_go_back method by a lambda function that returns handle_go_back
    monkeypatch.setattr(App, "handle_go_back", lambda *args: "handle_go_back")
    
    # Test handle go back
    input_value = "h"
    result = app.brand_policy_screen()
    assert result == "handle_go_back"

def test_important_links_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App copyright_notice_screen method by a lambda function that returns copyright_notice
    monkeypatch.setattr(App, "copyright_notice_screen", lambda *args: "copyright_notice")
    # Replaces App about_screen method by a lambda function that returns about
    monkeypatch.setattr(App, "about_screen", lambda *args: "about")
    # Replaces App accessibility_screen method by a lambda function that returns accessibility
    monkeypatch.setattr(App, "accessibility_screen", lambda *args: "accessibility")
    # Replaces App user_agreement_screen method by a lambda function that returns user_agreement
    monkeypatch.setattr(App, "user_agreement_screen", lambda *args: "user_agreement")
    # Replaces App privacy_policy_screen method by a lambda function that returns privacy_policy
    monkeypatch.setattr(App, "privacy_policy_screen", lambda *args: "privacy_policy")
    # Replaces App cookie_policy_screen method by a lambda function that returns cookie_policy
    monkeypatch.setattr(App, "cookie_policy_screen", lambda *args: "cookie_policy")
    # Replaces App copyright_policy_screen method by a lambda function that returns copyright_policy
    monkeypatch.setattr(App, "copyright_policy_screen", lambda *args: "copyright_policy")
    # Replaces App brand_policy_screen method by a lambda function that returns brand_policy
    monkeypatch.setattr(App, "brand_policy_screen", lambda *args: "brand_policy")
    # Replaces App languages_screen method by a lambda function that returns languages
    monkeypatch.setattr(App, "languages_screen", lambda *args: "languages")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.important_links_screen()
    assert result == "go_back"

    # Test copyright notice
    input_value = "0"
    result = app.important_links_screen()
    assert result == "copyright_notice"

    # Test about
    input_value = "1"
    result = app.important_links_screen()
    assert result == "about"

    # Test accessibility
    input_value = "2"
    result = app.important_links_screen()
    assert result == "accessibility"

    # Test user agreement
    input_value = "3"
    result = app.important_links_screen()
    assert result == "user_agreement"

    # Test privacy policy
    input_value = "4"
    result = app.important_links_screen()
    assert result == "privacy_policy"

    # Test cookie policy
    input_value = "5"
    result = app.important_links_screen()
    assert result == "cookie_policy"

    # Test copyright policy
    input_value = "6"
    result = app.important_links_screen()
    assert result == "copyright_policy"

    # Test brand policy
    input_value = "7"
    result = app.important_links_screen()
    assert result == "brand_policy"

    # Test languages withouth login
    input_value = "8"    
    result = app.important_links_screen()
    assert result == "reload"

    # Test languages
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0], STANDARD_TIER_NAME)
    app.current_user = user
    input_value = "8"    
    result = app.important_links_screen()
    assert result == "languages"

    # Test reload
    input_value = "-1"    
    result = app.main_menu()
    assert result == "reload"

def test_useful_links_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App under_construction_screen function with a lambda function that returns under_construction
    monkeypatch.setattr(App, "under_construction_screen", lambda *args: "under_construction")
    # Replaces App under_construction_screen function with a lambda function that returns under_construction
    monkeypatch.setattr(App, "general_option_screen", lambda *args: "general_option")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.useful_links_screen()
    assert result == "go_back"

    # Test general options
    input_value = "0"
    result = app.useful_links_screen()
    assert result == "general_option"

    # Test under construction
    input_value = "1"
    result = app.useful_links_screen()
    assert result == "under_construction"

    # Test under construction
    input_value = "2"
    result = app.useful_links_screen()
    assert result == "under_construction"

    # Test under construction
    input_value = "3"
    result = app.useful_links_screen()
    assert result == "under_construction"

    # Test reload
    input_value = "-1"    
    result = app.useful_links_screen()
    assert result == "reload"

def test_general_option_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)

    # Replaces App screen functions with a lambda function that returns a string representation of the function
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    monkeypatch.setattr(App, "under_construction_screen", lambda *args: "under_construction")
    monkeypatch.setattr(App, "register_user_screen", lambda *args: "register_user")
    monkeypatch.setattr(App, "help_center_screen", lambda *args: "help_center")
    monkeypatch.setattr(App, "general_option_about_screen", lambda *args: "about")
    monkeypatch.setattr(App, "press_screen", lambda *args: "press")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.general_option_screen()
    assert result == "go_back"

    # Test register user
    input_value = "0"
    result = app.general_option_screen()
    assert result == "register_user"

    # Test help center
    input_value = "1"
    result = app.general_option_screen()
    assert result == "help_center"

    # Test about
    input_value = "2"
    result = app.general_option_screen()
    assert result == "about"

    # Test press
    input_value = "3"
    result = app.general_option_screen()
    assert result == "press"

    # Test under construction
    input_value = "4"
    result = app.general_option_screen()
    assert result == "under_construction"

    # Test under construction
    input_value = "5"
    result = app.general_option_screen()
    assert result == "under_construction"

    # Test under construction
    input_value = "6"
    result = app.general_option_screen()
    assert result == "under_construction"

    # Test reload
    input_value = "-1"    
    result = app.general_option_screen()
    assert result == "reload"

def test_help_center_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert HELP_CENTER_MESSAGE in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.help_center_screen()
    assert result == "go_back"

    # Test reload
    input_value = "h"    
    result = app.help_center_screen()
    assert result == "reload"

def test_general_option_about_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert GENERAL_OPTION_ABOUT_MESSAGE in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.general_option_about_screen()
    assert result == "go_back"

    # Test reload
    input_value = "h"    
    result = app.general_option_about_screen()
    assert result == "reload"

def test_press_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert PRESS_MESSAGE in out
        prompt = args[1]
        assert prompt == GO_BACK_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.press_screen()
    assert result == "go_back"

    # Test reload
    input_value = "h"    
    result = app.press_screen()
    assert result == "reload"

def test_main_menu(monkeypatch, capfd):
    app = App()
    App.success_story = "Success story!"

    def mock_input(*args):
        nonlocal input_value

        # Reads standard output
        out, _ = capfd.readouterr()
        assert App.success_story in out
        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App login_screen method by a lambda function that returns login
    monkeypatch.setattr(App, "login_screen", lambda *args: "login")
    # Replaces App register_user_screen method by a lambda function that returns register_user
    monkeypatch.setattr(App, "register_user_screen", lambda *args: "register_user")
    # Replaces App play_video method by a lambda function that returns play_video
    monkeypatch.setattr(App, "play_video", lambda *args: "play_video")
    # Replaces App find_someone_screen method by a lambda function that returns find_someone_screen
    monkeypatch.setattr(App, "find_someone_screen", lambda *args: "find_someone_screen")
    # Replaces App useful_links_screen method by a lambda function that returns useful_links
    monkeypatch.setattr(App, "useful_links_screen", lambda *args: "useful_links")
    # Replaces App important_links_screen method by a lambda function that returns important_links
    monkeypatch.setattr(App, "important_links_screen", lambda *args: "important_links")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")
    # Replaces App useful_links_screen method by a lambda function that returns useful_links
    monkeypatch.setattr(App, "useful_links_screen", lambda *args: "useful_links")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.main_menu()
    assert result == "go_back"

    # Test login
    input_value = "0"      
    result = app.main_menu()
    assert result == "login"

    # Test register user
    input_value = "1"
    result = app.main_menu()
    assert result == "register_user"

    # Test play video
    input_value = "2"
    result = app.main_menu()
    assert result == "play_video"

    # Test find someone
    input_value = "3"    
    result = app.main_menu()
    assert result == "find_someone_screen"

    # Test useful links
    input_value = "4"
    result = app.main_menu()
    assert result == "useful_links"

    # Test important links
    input_value = "5"    
    result = app.main_menu()
    assert result == "important_links"

    # Test reload
    input_value = "6"    
    result = app.main_menu()
    assert result == "reload"

def test_search_students_screen(monkeypatch):
    app = App()
    App.success_story = "Success story!"

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App search_students_by_last_name_screen method by a lambda function that returns last_name
    monkeypatch.setattr(App, "search_students_by_last_name_screen", lambda *args: "last_name")
    # Replaces App search_students_by_university_screen method by a lambda function that returns university
    monkeypatch.setattr(App, "search_students_by_university_screen", lambda *args: "university")
    # Replaces App search_students_by_major_screen method by a lambda function that returns major
    monkeypatch.setattr(App, "search_students_by_major_screen", lambda *args: "major")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.search_students_screen()
    assert result == "go_back"

    # Test search students by last name
    input_value = "0"      
    result = app.search_students_screen()
    assert result == "last_name"

    # Test search students by university
    input_value = "1"
    result = app.search_students_screen()
    assert result == "university"

    # Test search students by major
    input_value = "2"
    result = app.search_students_screen()
    assert result == "major"

    # Test reload
    input_value = "-1"    
    result = app.search_students_screen()
    assert result == "reload"

def test_search_students_by_last_name_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        prompt = args[0]
        if prompt == TYPE_LAST_NAME_MESSAGE:
            return ""
        
        assert False
    
    # Replaces input buildt-in input with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces User find_users_by_last_name by a lambda function that returns []
    monkeypatch.setattr(User, "find_users_by_last_name", lambda *args: [])
    # Replaces User search_students_result_screen by a lambda function that returns results
    monkeypatch.setattr(App, "search_students_result_screen", lambda *args: "results")

    result = app.search_students_by_last_name_screen()
    assert result == "results"
    assert len(app.history) == 0

def test_search_students_by_university_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        prompt = args[0]
        if prompt == TYPE_NAME_OF_UNIVERSITY:
            return ""
        
        assert False
    
    # Replaces input buildt-in input with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces User find_users_by_university by a lambda function that returns []
    monkeypatch.setattr(User, "find_users_by_university", lambda *args: [])
    # Replaces User search_students_result_screen by a lambda function that returns results
    monkeypatch.setattr(App, "search_students_result_screen", lambda *args: "results")

    result = app.search_students_by_university_screen()
    assert result == "results"
    assert len(app.history) == 0

def test_search_students_by_major_screen(monkeypatch):
    app = App()

    def mock_input(*args):
        prompt = args[0]
        if prompt == TYPE_MAJOR_MESSAGE:
            return ""
        
        assert False
    
    # Replaces input buildt-in input with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces User find_users_by_major by a lambda function that returns []
    monkeypatch.setattr(User, "find_users_by_major", lambda *args: [])
    # Replaces User search_students_result_screen by a lambda function that returns results
    monkeypatch.setattr(App, "search_students_result_screen", lambda *args: "results")

    result = app.search_students_by_major_screen()
    assert result == "results"
    assert len(app.history) == 0

def test_search_students_result_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        if prompt == SELECT_OPTION_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App show_student_options method by a lambda function that returns show_student
    monkeypatch.setattr(App, "show_student_options", lambda *args: "show_student")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    user1 = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    user2 = User("Software", "", "John", "Doe", "English", STANDARD_TIER_NAME)
    users_list = [user1, user2]

    # Test go back no results
    input_value = GO_BACK_KEY
    result = app.search_students_result_screen([])
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name not in out
    assert user2.first_name not in out

    # Test go back with results
    input_value = GO_BACK_KEY
    result = app.search_students_result_screen(users_list)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name in out
    assert user2.first_name in out
    
    # Test show user successfull
    for i in range(len(users_list)):
        input_value = str(i)
        result = app.search_students_result_screen(users_list)
        assert result == "show_student"
    
    # Test reload
    input_value = "-1"
    result = app.search_students_result_screen(users_list)
    assert result == "reload"

def test_show_student_options(monkeypatch):
    app = App()
    user1 = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user1

    user2 = User("Software", "", "John", "Doe", "English", STANDARD_TIER_NAME)

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        if prompt == SELECT_OPTION_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App accept_connection_screen method by a lambda function that returns accept
    monkeypatch.setattr(App, "accept_connection_screen", lambda *args: "accept")
    # Replaces App reject_connection_screen method by a lambda function that returns reject
    monkeypatch.setattr(App, "reject_connection_screen", lambda *args: "reject")
    # Replaces App view_profile_screen method by a lambda function that returns view
    monkeypatch.setattr(App, "show_profile_screen", lambda *args: "view")
    # Replaces App disconnect_screen method by a lambda function that returns disconnect
    monkeypatch.setattr(App, "disconnect_screen", lambda *args: "disconnect")
    # Replaces App request_connection_screen method by a lambda function that returns request
    monkeypatch.setattr(App, "request_connection_screen", lambda *args: "request")
    # Relplaces App send_message_input_screen method by a lambda function that returns "send_message"
    monkeypatch.setattr(App, "send_message_input_screen", lambda *args: "send_message")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.show_student_options(user2)
    assert result == "go_back"

    # Test received connection request
    user1.received_friend_requests = [user2.username]

    input_value = "0"
    result = app.show_student_options(user2)
    assert result == "accept"

    input_value = "1"
    result = app.show_student_options(user2)
    assert result == "reject"

    input_value = "2"
    result = app.show_student_options(user2)
    assert result == "send_message"

    input_value = "3"
    result = app.show_student_options(user2)
    assert result == "reload"

    # Test is friend without profile
    user1.received_friend_requests = []
    user1.friends = [user2.username]

    input_value = "0"
    result = app.show_student_options(user2)
    assert result == "disconnect"

    input_value = "1"
    result = app.show_student_options(user2)
    assert result == "send_message"

    input_value = "2"
    result = app.show_student_options(user2)
    assert result == "reload"

    # Test is friend with profile
    user2.profile = Profile()

    input_value = "0"
    result = app.show_student_options(user2)
    assert result == "view"

    input_value = "1"
    result = app.show_student_options(user2)
    assert result == "disconnect"

    input_value = "2"
    result = app.show_student_options(user2)
    assert result == "send_message"

    input_value = "3"
    result = app.show_student_options(user2)
    assert result == "reload"

    # Test is self with profile
    user1.profile = Profile()

    input_value = "0"
    result = app.show_student_options(user1)
    assert result == "view"

    input_value = "1"
    result = app.show_student_options(user1)
    assert result == "reload"

    # Test request connection
    user1.friends = []

    input_value = "0"
    result = app.show_student_options(user2)
    assert result == "send_message"
    
    input_value = "1"
    result = app.show_student_options(user2)
    assert result == "request"

    input_value = "2"
    result = app.show_student_options(user2)
    assert result == "reload"

def test_request_connection_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test successful

    # Replaces User request_connection method by a lambda function that returns None
    monkeypatch.setattr(User, "request_connection", lambda *args: None)
    
    result = app.request_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_REQUESTED_MESSAGE in out

    # Test unsuccessfull

    # Replaces User request_connection method by a lambda function that returns CONNECT_TO_SELF_ERROR_MESSAGE
    monkeypatch.setattr(User, "request_connection", lambda *args: CONNECT_TO_SELF_ERROR_MESSAGE)
    
    result = app.request_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECT_TO_SELF_ERROR_MESSAGE in out

def test_accept_connection_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test successful

    # Replaces User accept_connection method by a lambda function that returns None
    monkeypatch.setattr(User, "accept_connection", lambda *args: None)
    
    result = app.accept_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_ACEPTED_MESSAGE in out

    # Test unsuccessfull

    # Replaces User accept_connection method by a lambda function that returns CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
    monkeypatch.setattr(User, "accept_connection", lambda *args: CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE)
    
    result = app.accept_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE in out

def test_reject_connection_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test successful

    # Replaces User reject_connection method by a lambda function that returns None
    monkeypatch.setattr(User, "reject_connection", lambda *args: None)
    
    result = app.reject_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_REJECTED_MESSAGE in out

    # Test unsuccessfull

    # Replaces User reject_connection method by a lambda function that returns CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
    monkeypatch.setattr(User, "reject_connection", lambda *args: CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE)
    
    result = app.reject_connection_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE in out

def test_disconnect_screen(monkeypatch, capfd):
    app = App()
    user = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user

    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test successful

    # Replaces User disconnect method by a lambda function that returns None
    monkeypatch.setattr(User, "disconnect", lambda *args: None)
    
    result = app.disconnect_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert DISCONNECTED_MESSAGE in out

    # Test unsuccessfull

    # Replaces User disconnect method by a lambda function that returns CONNECTION_NOT_FOUND_ERROR_MESSAGE
    monkeypatch.setattr(User, "disconnect", lambda *args: CONNECTION_NOT_FOUND_ERROR_MESSAGE)
    
    result = app.disconnect_screen(user)
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert CONNECTION_NOT_FOUND_ERROR_MESSAGE in out

def test_my_network_screen(monkeypatch, capfd):
    app = App() 
    user1 = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    user2 = User("Software", "", "John", "Doe", "English", STANDARD_TIER_NAME)

    User.users = {
        "Testing": user1,
        "Software": user2,
    }
    app.current_user = user1

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        if prompt == SELECT_OPTION_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App show_student_options method by a lambda function that returns show_student
    monkeypatch.setattr(App, "show_student_options", lambda *args: "show_student")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back no results
    input_value = GO_BACK_KEY
    result = app.my_network_screen()
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name not in out
    assert user2.first_name not in out

    # Test go back with results
    user1.friends = [user2.username]

    input_value = GO_BACK_KEY
    result = app.my_network_screen()
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name not in out
    assert user2.first_name in out
    
    # Test show user successfull
    for i in range(1):
        input_value = str(i)
        result = app.my_network_screen()
        assert result == "show_student"
    
    # Test reload
    input_value = "1"
    result = app.my_network_screen()
    assert result == "reload"

def test_pending_friend_requests_screen(monkeypatch, capfd):
    app = App() 
    user1 = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    user2 = User("Software", "", "John", "Doe", "English", STANDARD_TIER_NAME)

    User.users = {
        "Testing": user1,
        "Software": user2,
    }
    app.current_user = user1

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        if prompt == SELECT_OPTION_MESSAGE:
            return input_value
        
        assert False
    
    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App show_student_options method by a lambda function that returns show_student
    monkeypatch.setattr(App, "show_student_options", lambda *args: "show_student")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back no results
    input_value = GO_BACK_KEY
    result = app.pending_friend_requests_screen()
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name not in out
    assert user2.first_name not in out

    # Test go back with results
    user1.received_friend_requests = [user2.username]

    input_value = GO_BACK_KEY
    result = app.pending_friend_requests_screen()
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert user1.first_name not in out
    assert user2.first_name in out
    
    # Test show user successfull
    for i in range(1):
        input_value = str(i)
        result = app.pending_friend_requests_screen()
        assert result == "show_student"
    
    # Test reload
    input_value = "1"
    result = app.pending_friend_requests_screen()
    assert result == "reload"

def test_user_dashboard(monkeypatch, capfd):
    app = App()
    user = User("Testing", "", "Peter", "Doe", "English", STANDARD_TIER_NAME)
    app.current_user = user

    def mock_input(*args):
        nonlocal input_value
        
        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value
    
    def pop_notification(user):
        return user.notifications.pop()

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces User pop_notification method by pop_notification
    monkeypatch.setattr(User, "pop_notification", pop_notification)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App job_menu_screen function by a lambda function that returns job_menu
    monkeypatch.setattr(App, "job_menu_screen", lambda *args: "job_menu")
    # Replaces App search_students_screen function by a lambda function that returns search_students
    monkeypatch.setattr(App, "search_students_screen", lambda *args: "search_students")
    # Replaces App new_skills_screen function by a lambda function that returns new_skills
    monkeypatch.setattr(App, "new_skills_screen", lambda *args: "new_skills")
    # Replaces App useful_links_screen method by a lambda function that returns useful_links
    monkeypatch.setattr(App, "useful_links_screen", lambda *args: "useful_links")
    # Replaces App important_links_screen method by a lambda function that returns important_links
    monkeypatch.setattr(App, "important_links_screen", lambda *args: "important_links")
    # Replaces App edit_profile_screen method by a lambda function that returns edit_profile
    monkeypatch.setattr(App, "edit_profile_screen", lambda *args: "edit_profile")
    # Replaces App show_profile_screen method by a lambda function that returns show_profile
    monkeypatch.setattr(App, "show_profile_screen", lambda *args: "show_profile")
    # Replaces App my_network_screen method by a lambda function that returns my_network
    monkeypatch.setattr(App, "my_network_screen", lambda *args: "my_network")
    # Replaces App pending_friend_requests_screen method by a lambda function that returns friend_requests
    monkeypatch.setattr(App, "pending_friend_requests_screen", lambda *args: "friend_requests")
    # Replaces App inbox_screen method by a lambda function that returns inbox
    monkeypatch.setattr(App, "inbox_screen", lambda *args: "inbox")
    # Replaces App send_message method by a lambda function that returns send_message
    monkeypatch.setattr(App, "send_message_screen", lambda *args: "send_message")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test job menu
    input_value = "0"
    result = app.user_dashboard()
    assert result == "job_menu"
    out, _ = capfd.readouterr()
    assert LAST_APPLICATION_SEVEN_DAYS_AGO_MESSAGE in out
    assert "Notification 1" not in out

    user.notifications = ["Notification 1", "Notification 2"]
    result = app.user_dashboard()
    assert result == "job_menu"
    out, _ = capfd.readouterr()
    assert "Notification 1" in out
    assert "Notification 2" in out

    # Test search students    
    input_value = "1"
    result = app.user_dashboard()
    assert result == "search_students"

    # Test new skills
    input_value = "2"
    result = app.user_dashboard()
    assert result == "new_skills"

    # Test useful links
    input_value = "3"    
    result = app.user_dashboard()
    assert result == "useful_links"

    # Test important links
    input_value = "4"    
    result = app.user_dashboard()
    assert result == "important_links"

    # Test edit profile
    input_value = "5"
    result = app.user_dashboard()
    assert result == "edit_profile"

    # Test show profile
    input_value = "6"
    result = app.user_dashboard()
    assert result == "show_profile"
    out, _ = capfd.readouterr()
    assert DO_NOT_FORGET_PROFILE_MESSAGE in out

    user.profile = Profile()
    result = app.user_dashboard()
    assert result == "show_profile"
    out, _ = capfd.readouterr()
    assert DO_NOT_FORGET_PROFILE_MESSAGE not in out

    # Test my network
    input_value = "7"
    result = app.user_dashboard()
    assert result == "my_network"

    # Test friend requests
    input_value = "8"
    result = app.user_dashboard()
    assert result == "friend_requests"
    out, _ = capfd.readouterr()
    assert PENDING_FRIEND_REQUEST_MESSAGE not in out

    user.received_friend_requests = ["user2"]
    result = app.user_dashboard()
    assert result == "friend_requests"
    out, _ = capfd.readouterr()
    assert PENDING_FRIEND_REQUEST_MESSAGE in out

    # Test inbox
    input_value = "9"
    result = app.user_dashboard()
    assert result == "inbox"   

    # Test send  message
    input_value = "10"
    result = app.user_dashboard()
    assert result == "send_message"
    out, _ = capfd.readouterr()
    assert UNREAD_MESSAGES_MESSAGE not in out

    user.inbox = {0: Message("user2", "Message", None)}
    result = app.user_dashboard()
    assert result == "send_message"
    out, _ = capfd.readouterr()
    assert UNREAD_MESSAGES_MESSAGE in out   

    # Test reload
    input_value = "11"
    result = app.user_dashboard()
    assert result == "reload"

    # Test go back
    input_value = GO_BACK_KEY
    result = app.user_dashboard()
    assert result == "go_back"
    assert app.current_user == None
