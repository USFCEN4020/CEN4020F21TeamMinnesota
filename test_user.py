import builtins
import io
import pickle

from os import path
from user import CONNECT_TO_FRIEND_ERROR_MESSAGE, CONNECT_TO_SELF_ERROR_MESSAGE, CONNECTION_NOT_FOUND_ERROR_MESSAGE, CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE, CONNECTION_REQUEST_PENDING_ERROR_MESSAGE, MAX_ALLOWED_ACCOUNTS_ERROR_MESSAGE, MAX_USERS, RESEND_CONNECT_ERROR_MESSAGE, USERNAME_IN_USE_ERROR_MESSAGE,\
    PASSWORD_DIGIT_ERROR_MESSAGE, PASSWORD_CAPITAL_LETTER_ERROR_MESSAGE, PASSWORD_LENGTH_ERROR_MESSAGE, \
    INVALID_USERNAME_ERROR_MESSAGE, User
from profile import Profile

def test__init__():
    user = User("Testing", "Testing@12", "John", "Connor", "English")
    assert user.username == "Testing"
    assert user.password == "Testing@12"
    assert user.first_name == "John"
    assert user.last_name == "Connor"
    assert user.email_notifications
    assert user.sms_notifications
    assert user.targeted_ads
    assert user.app_language == "English"
    assert len(user.friends) == 0
    assert len(user.sent_friend_requests) == 0
    assert len(user.received_friend_requests) == 0

def test_load_users_file(monkeypatch):    
    user1 = User("Testing", User.hash_password("Testing@12"), "John", "Connor", "English")
    user2 = User("Software", User.hash_password("Software$89"), "John", "Doe", "Spanish")

    users = {
        "Testing": user1,
        "Software": user2
    }

    # Creates in-memory bytes file and dumps the users on it
    users_file = io.BytesIO()
    pickle.dump(users, users_file)
    users_file.seek(0)

    def mock_open(path, mode):
        assert path == User.USERS_FILE_NAME
        assert mode == "rb"
        return users_file
    
    # Replaces open buildt-in function by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    # Replaces python os.path isfile function by a lambda function that returns False
    monkeypatch.setattr(path, "isfile", lambda *arg: False)
    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    User.load_users_file()
    assert len(User.users) == len(users)
    
    assert user1.username in User.users
    assert user1.username == User.users[user1.username].username
    assert user1.password == User.users[user1.username].password
    assert user1.first_name == User.users[user1.username].first_name
    assert user1.last_name == User.users[user1.username].last_name
    assert user1.email_notifications == User.users[user1.username].email_notifications
    assert user1.sms_notifications == User.users[user1.username].sms_notifications
    assert user1.targeted_ads == User.users[user1.username].targeted_ads
    assert user1.app_language == User.users[user1.username].app_language
    assert user1.profile == None

    assert user2.username in User.users
    assert user2.username == User.users[user2.username].username
    assert user2.password == User.users[user2.username].password
    assert user2.first_name == User.users[user2.username].first_name
    assert user2.last_name == User.users[user2.username].last_name
    assert user2.email_notifications == User.users[user2.username].email_notifications
    assert user2.sms_notifications == User.users[user2.username].sms_notifications
    assert user2.targeted_ads == User.users[user2.username].targeted_ads
    assert user2.app_language == User.users[user2.username].app_language
    assert user2.profile == None

def test_update_users_file(monkeypatch):
    # Creates in-memory bytes file
    users_file = io.BytesIO()
    close = users_file.close
    # Prevent file from being closed
    users_file.close = lambda: None

    def mock_open(path, mode):
        assert path == User.USERS_FILE_NAME
        assert mode == "wb"
        return users_file
    
    # Replaces open buildt-in function with mock_open
    monkeypatch.setattr(builtins, "open", mock_open)

    user1 = User("Testing", User.hash_password("Testing@12"), "John", "Connor", "English")
    user2 = User("Software", User.hash_password("Software$89"), "John", "Doe", "English")

    User.users = {
        "Testing": user1,
        "Software": user2
    }

    User.update_users_file()

    users_file.seek(0)
    users = pickle.load(users_file)
    # Closes the file
    users_file.close = close
    users_file.close()

    assert len(users) == len(User.users)
    
    assert user1.username in User.users
    assert user1.username == User.users[user1.username].username
    assert user1.password == User.users[user1.username].password
    assert user1.first_name == User.users[user1.username].first_name
    assert user1.last_name == User.users[user1.username].last_name
    assert user1.email_notifications == User.users[user1.username].email_notifications
    assert user1.sms_notifications == User.users[user1.username].sms_notifications
    assert user1.targeted_ads == User.users[user1.username].targeted_ads
    assert user1.app_language == User.users[user1.username].app_language

    assert user2.username in User.users
    assert user2.username == User.users[user2.username].username
    assert user2.password == User.users[user2.username].password
    assert user2.first_name == User.users[user2.username].first_name
    assert user2.last_name == User.users[user2.username].last_name
    assert user2.email_notifications == User.users[user2.username].email_notifications
    assert user2.sms_notifications == User.users[user2.username].sms_notifications
    assert user2.targeted_ads == User.users[user2.username].targeted_ads
    assert user2.app_language == User.users[user2.username].app_language
    
def test_hash_password():
    password = User.hash_password("Testing@12")
    assert password == "ee87468f676f3a81e95f77cff2abd9d1"

def test_login():
    user1 = User("Testing", User.hash_password("Testing@12"), "John", "Connor", "English")
    user2 = User("Software", User.hash_password("Software$89"), "John", "Doe", "English")

    User.users = {
        "Testing": user1,
        "Software": user2
    }

    # Test login successful
    result = User.login("Testing", "Testing@12")
    assert result == user1

    result = User.login("Software", "Software$89")
    assert result == user2

    # Test login unsuccessful
    result = User.login("Testing", "Tampa@12")
    assert result == None

    result = User.login("Tampa", "Tampa@12")
    assert result == None

    result = User.login("Soft", "Software$89")
    assert result == None

def test_save(monkeypatch):
    monkeypatch.setattr(User, "update_users_file", lambda: None)
    User.users = {}

    user1 = User("Test", "Testing@12", "John", "Connor", "English")
    user2 = User("", "Testing@12", "John", "Doe", "English")
    user3 = User("Test", "Testing@12", "Peter", "Parker", "English")
    user4 = User("Software", "software$89", "Tony", "Stark", "English")
    user5 = User("Test1", "Testing@", "John", "Parker", "English")
    user6 = User("Test2", "Test2", "John", "Stark", "English")
    user7 = User("Test3", "Testing@12345", "Tony", "Connor", "English")

    # Test save successful
    error_message = user1.save()
    assert error_message == None

    # Test save unsuccessful
    error_message = user2.save()
    assert error_message == INVALID_USERNAME_ERROR_MESSAGE

    error_message = user3.save()
    assert error_message == USERNAME_IN_USE_ERROR_MESSAGE

    error_message = user4.save()
    assert error_message  == PASSWORD_CAPITAL_LETTER_ERROR_MESSAGE

    error_message = user5.save()
    assert error_message == PASSWORD_DIGIT_ERROR_MESSAGE

    error_message = user6.save() 
    assert error_message == PASSWORD_LENGTH_ERROR_MESSAGE

    error_message = user7.save()
    assert error_message == PASSWORD_LENGTH_ERROR_MESSAGE

    # Test max number of users reached
    for i in range(9):
        user = User(f"Test_{i}", "Testing@12", "John", f"Connor_{i}", "English")
        error_message = user.save()
        assert error_message == None

    user = User("Test_9", "Testing@12", "John", "Connor", "English")
    error_message = user.save()
    assert error_message == MAX_ALLOWED_ACCOUNTS_ERROR_MESSAGE
    assert len(User.users) == MAX_USERS

def test_toggle_email_notifications(monkeypatch):
    user = User("Testing", "Testing@12", "John", "Connor", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test turn off email notifications
    user.toggle_email_notifications()
    assert user.email_notifications == False

    # Test turn on email notifications
    user.toggle_email_notifications()
    assert user.email_notifications == True

def test_toggle_sms_notifications(monkeypatch):
    user = User("Testing", "Testing@12", "John", "Connor", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test turn off sms notifications
    user.toggle_sms_notifications()
    assert user.sms_notifications == False

    # Test turn on sms notifications
    user.toggle_sms_notifications()
    assert user.sms_notifications == True

def test_toggle_targeted_ads(monkeypatch):
    user = User("Testing", "Testing@12", "John", "Connor", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test turn off targeted ads
    user.toggle_targeted_ads()
    assert user.targeted_ads == False

    # Test turn on targeted ads
    user.toggle_targeted_ads()
    assert user.targeted_ads == True

def test_find_by_name():
    user1 = User("Testing", "Testing@12", "John", "Connor", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")

    User.users = {
        "Testing": user1,
        "Software": user2
    }

    # Test find user successful
    user = User.find_by_name(user2.first_name, user2.last_name)
    assert user == user2

    # Test find user unsuccessful
    user = User.find_by_name("Tony", "Stark")
    assert user == None

def test_find_users_by_last_name():
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")
    user3 = User("Engineering", "Software$89", "John", "Brown", "English")

    User.users = {
        "Testing": user1,
        "Software": user2,
        "Engineering": user3
    }

    # Test find users by last name successful
    result = User.find_users_by_last_name("Doe")
    assert result == [user1, user2]

    # Test find users by last name empty
    result = User.find_users_by_last_name("Connor")
    assert result == []

def test_find_users_by_university():
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user1.profile = Profile()
    user1.profile.university = "USF"

    user2 = User("Software", "Software$89", "John", "Doe", "English")
    user2.profile = Profile()
    user2.profile.university = "USF"

    user3 = User("Engineering", "Software$89", "John", "Brown", "English")
    user3.profile = Profile()
    user3.profile.university = "UCF"

    User.users = {
        "Testing": user1,
        "Software": user2,
        "Engineering": user3
    }

    # Test find users by last name successful
    result = User.find_users_by_university("USF")
    assert result == [user1, user2]

    # Test find users by last name empty
    result = User.find_users_by_university("UF")
    assert result == []

def test_find_users_by_major():
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user1.profile = Profile()
    user1.profile.major = "Computer Science"

    user2 = User("Software", "Software$89", "John", "Doe", "English")
    user2.profile = Profile()
    user2.profile.major = "Computer Science"

    user3 = User("Engineering", "Software$89", "John", "Brown", "English")
    user3.profile = Profile()
    user3.profile.major = "Computer Engineering"

    User.users = {
        "Testing": user1,
        "Software": user2,
        "Engineering": user3
    }

    # Test find users by last name successful
    result = User.find_users_by_major("Computer Science")
    assert result == [user1, user2]

    # Test find users by last name empty
    result = User.find_users_by_major("Cybersecurity")
    assert result == []

def test_request_connection(monkeypatch):
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test connect to self error
    error_message = user1.request_connection(user1)
    assert error_message == CONNECT_TO_SELF_ERROR_MESSAGE
    assert len(user1.sent_friend_requests) == 0

    # Test resend connect error
    user1.sent_friend_requests = [user2.username]
    error_message = user1.request_connection(user2)
    assert error_message == RESEND_CONNECT_ERROR_MESSAGE
    assert len(user1.sent_friend_requests) == 1

    # Test request pending error
    user1.sent_friend_requests = []
    user1.received_friend_requests = [user2.username]
    error_message = user1.request_connection(user2)
    assert error_message == CONNECTION_REQUEST_PENDING_ERROR_MESSAGE
    assert len(user1.sent_friend_requests) == 0

    # Test connect to friend error
    user1.received_friend_requests = []
    user1.friends = [user2.username]
    error_message = user1.request_connection(user2)
    assert error_message == CONNECT_TO_FRIEND_ERROR_MESSAGE
    assert len(user1.sent_friend_requests) == 0

    # Test send request successful
    user1.friends = []
    error_message = user1.request_connection(user2)
    assert error_message == None
    assert len(user1.friends) == 0
    assert len(user1.sent_friend_requests) == 1
    assert len(user1.received_friend_requests) == 0
    assert user2.username in user1.sent_friend_requests
    assert len(user2.friends) == 0
    assert len(user2.sent_friend_requests) == 0
    assert len(user2.received_friend_requests) == 1
    assert user1.username in user2.received_friend_requests

def test_accept_connection(monkeypatch):
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test accept connection error
    error_message = user1.accept_connection(user2)
    assert error_message == CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
    assert len(user1.friends) == 0
    assert len(user2.friends) == 0

    # Test accept connection successfull
    user1.received_friend_requests = [user2.username]
    user2.sent_friend_requests = [user1.username]
    error_message = user1.accept_connection(user2)
    assert len(user1.friends) == 1
    assert len(user1.sent_friend_requests) == 0
    assert len(user1.received_friend_requests) == 0
    assert user2.username in user1.friends
    assert len(user2.friends) == 1
    assert len(user2.sent_friend_requests) == 0
    assert len(user2.received_friend_requests) == 0
    assert user1.username in user2.friends


def test_reject_connection(monkeypatch):
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test reject connection error
    error_message = user1.reject_connection(user2)
    assert error_message == CONNECTION_REQUEST_NOT_FOUND_ERROR_MESSAGE
    assert len(user1.friends) == 0
    assert len(user2.friends) == 0

    # Test reject connection successfull
    user1.received_friend_requests = [user2.username]
    user2.sent_friend_requests = [user1.username]
    error_message = user1.reject_connection(user2)
    assert len(user1.friends) == 0
    assert len(user1.sent_friend_requests) == 0
    assert len(user1.received_friend_requests) == 0
    assert len(user2.friends) == 0
    assert len(user2.sent_friend_requests) == 0
    assert len(user2.received_friend_requests) == 0

def test_disconnect(monkeypatch):
    user1 = User("Testing", "Testing@12", "Peter", "Doe", "English")
    user2 = User("Software", "Software$89", "John", "Doe", "English")

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    # Test disconnection connection error
    error_message = user1.disconnect(user2)
    assert error_message == CONNECTION_NOT_FOUND_ERROR_MESSAGE
    assert len(user1.friends) == 0
    assert len(user2.friends) == 0

    # Test disconnection successfull
    user1.friends = [user2.username]
    user2.friends = [user1.username]
    error_message = user1.disconnect(user2)
    assert len(user1.friends) == 0
    assert len(user1.sent_friend_requests) == 0
    assert len(user1.received_friend_requests) == 0
    assert len(user2.friends) == 0
    assert len(user2.sent_friend_requests) == 0
    assert len(user2.received_friend_requests) == 0
    