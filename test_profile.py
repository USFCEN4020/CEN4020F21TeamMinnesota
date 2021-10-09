import io
import pickle

from os import path
from profile import MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE, MAX_EXPRIENCE, Profile
import profile
from user import User

def test__init__():
    profile = Profile()
    assert profile.title == ""
    assert profile.major == ""
    assert profile.university == ""
    assert profile.about == ""
    assert profile.exprience == []
    assert profile.education == None

def test_save(monkeypatch):    
    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "save", lambda: None)
    experiences = ["internship1", "internship2"]
    #profile1 = Profile("4th Year Comp Sci Student", "Computer Science", "USF", "Testing Summ", experiences)
    profile1 = Profile()
    profile1.title = "4th Year Comp Sci Student"
    profile1.major = "Computer Science"
    profile1.university = "USF"
    profile1.about = "Testing Summ"
    profile1.exprience = experiences

    error_message = profile1.save(2)
    assert error_message == None

    experiences.append("internship3")
    experiences.append("internship4")
    error_message = profile1.save(4)
    assert error_message == MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE

    
