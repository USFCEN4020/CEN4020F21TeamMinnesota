import builtins
import io

from collections import deque
from job import MAX_ALLOWED_JOBS_ERROR_MESSAGE, Job
from main import CONTACT_FOUND_MESSAGE, CONTACT_NOT_FOUND_MESSAGE, GENERAL_OPTION_ABOUT_MESSAGE, HELP_CENTER_MESSAGE, JOB_SAVED_MESSAGE, LANGUAGES, \
    LOGIN_ERROR_MESSAGE, LOGIN_SUCCESSFUL_MESSAGE, PRESS_MESSAGE, SELECT_LANGUAGE_MESSAGE, TYPE_FIRST_NAME_MESSAGE, \
    TYPE_JOB_DESCRIPTION_MESSAGE, TYPE_JOB_EMPLOYER_MESSAGE, TYPE_JOB_LOCATION_MESSAGE, \
    TYPE_JOB_SALARY_MESSAGE, TYPE_JOB_TITLE_MESSAGE, TYPE_LAST_NAME_MESSAGE, VIDEO_PLAYNG_MESSAGE,\
    GO_BACK_KEY, GO_BACK_MESSAGE, INVALID_INPUT_ERROR_MESSAGE, SELECT_NEW_SKILL_MESSAGE, \
    SELECT_OPTION_MESSAGE, SKILLS, TYPE_PASSWORD_MESSAGE, TYPE_USERNAME_MESSAGE, \
    UNDER_CONSTRUCTION_MESSAGE, USER_CREATED_MESSAGE, screen, App
from user import PASSWORD_LENGTH_ERROR_MESSAGE, User

def test_screen():
    return_true = lambda app: app
    return_true.__name__ = "return_true"
    wrapper = screen(return_true)

    app = App()
    result = wrapper(app)
    assert result == app
    assert app.history[-1] == return_true.__name__
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
    app.history.extend([app.return_true.__name__, None])

    result = app.go_back()
    assert result == True
    assert len(app.history) == 0

    # Test with single history
    app.history.extend([app.return_true.__name__])

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

    app.history.extend([app.return_false.__name__, app.return_true.__name__])

    result = app.reload_screen()
    assert result == True
    assert len(app.history) == 1
    assert app.history[-1] == app.return_false.__name__

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

def test_register_user_screen(monkeypatch, capfd):
    app = App()

    def mock_input(*args):
        nonlocal input_counter
        input_counter += 1

        prompt = args[0]
        if prompt == TYPE_USERNAME_MESSAGE:
            return "hello"

        if prompt == TYPE_PASSWORD_MESSAGE:
            return "12345678"

        if prompt == TYPE_FIRST_NAME_MESSAGE:
            return "John"

        if prompt == TYPE_LAST_NAME_MESSAGE:
            return "Connor"

    # Replaces python builtin input function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    
    # Test valid input
    
    # Replaces User save function with a lambda function that returns None
    monkeypatch.setattr(User, "save", lambda *args: None)
    input_counter = 0
    app.register_user_screen()
    assert input_counter == 4
    # Reads standard output
    out, _ = capfd.readouterr()
    assert USER_CREATED_MESSAGE in out

    # Test wrong input

    # Replaces User save function with a lambda function that returns a message
    monkeypatch.setattr(User, "save", lambda *args: PASSWORD_LENGTH_ERROR_MESSAGE)
    input_counter = 0
    app.register_user_screen()
    assert input_counter == 4
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
    user = User("Testing", User.hash_password("Testing@12"), "Jhonn", "Connor", LANGUAGES[0])
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
        "Testing": User.hash_password("Testing@12"),
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

    def mock_input(*args):
        nonlocal input_value

        prompt = args[1]
        assert prompt == SELECT_OPTION_MESSAGE
        return input_value

    # Replaces App handle_input method by mock_input
    monkeypatch.setattr(App, "handle_input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")
    # Replaces App post_job method by a lambda function that returns post_job
    monkeypatch.setattr(App, "post_job", lambda *args: "post_job")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.job_menu_screen()
    assert result == "go_back"

    # Test post job
    input_value = "0"
    result = app.job_menu_screen()
    assert result == "post_job"

    # Test reload
    input_value = "-1"
    result = app.job_menu_screen()
    assert result == "reload"

def test_post_job(monkeypatch, capfd):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0])
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
    
    # Replaces input buildt-in function with mock_input function
    monkeypatch.setattr(builtins, "input", mock_input)
    # Replaces App go_back method by a lambda function that returns go_back
    monkeypatch.setattr(App, "go_back", lambda *args: "go_back")

    # Test save successful

    # Replaces Job save method by a lambda function that returns None
    monkeypatch.setattr(Job, "save", lambda *args: None)
    input_counter = 0
    result = app.post_job()
    assert input_counter == 5
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert JOB_SAVED_MESSAGE in out 

    # Test save unsuccessful

    # Replaces Job save method by a lambda function that returns MAX_ALLOWED_JOBS_ERROR_MESSAGE
    monkeypatch.setattr(Job, "save", lambda *args: MAX_ALLOWED_JOBS_ERROR_MESSAGE)
    input_counter = 0
    result = app.post_job()
    assert input_counter == 5
    assert result == "go_back"
    out, _ = capfd.readouterr()
    assert MAX_ALLOWED_JOBS_ERROR_MESSAGE in out

def test_guest_controls_screen(monkeypatch):
    app = App()
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0])
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
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0])
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
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0])
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
    user = User("Testing", "Testing@12", "John", "Connor", LANGUAGES[0])
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
    input_value = "-1"    
    result = app.main_menu()
    assert result == "reload"

def test_user_dashboard(monkeypatch):
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
    # Replaces App job_menu_screen function by a lambda function that returns job_menu
    monkeypatch.setattr(App, "job_menu_screen", lambda *args: "job_menu")
    # Replaces App find_someone_screen function by a lambda function that returns find_someone
    monkeypatch.setattr(App, "find_someone_screen", lambda *args: "find_someone")
    # Replaces App new_skills_screen function by a lambda function that returns new_skills
    monkeypatch.setattr(App, "new_skills_screen", lambda *args: "new_skills")
    # Replaces App useful_links_screen method by a lambda function that returns useful_links
    monkeypatch.setattr(App, "useful_links_screen", lambda *args: "useful_links")
    # Replaces App important_links_screen method by a lambda function that returns important_links
    monkeypatch.setattr(App, "important_links_screen", lambda *args: "important_links")
    # Replaces App reload_screen method by a lambda function that returns reload
    monkeypatch.setattr(App, "reload_screen", lambda *args: "reload")

    # Test go back
    input_value = GO_BACK_KEY
    result = app.user_dashboard()
    assert result == "go_back"

    # Test job menu
    input_value = "0"
    result = app.user_dashboard()
    assert result == "job_menu"

    # Test find someone    
    input_value = "1"
    result = app.user_dashboard()
    assert result == "find_someone"

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

    # Test reload
    input_value = "-1"
    result = app.user_dashboard()
    assert result == "reload"