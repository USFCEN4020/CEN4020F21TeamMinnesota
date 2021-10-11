from profile import MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE, EXPERIENCE_INDEX_OUT_OF_RANGE, Profile, \
    EDUCATION_INDEX_OUT_OF_RANGE
from experience import Experience
from education import Education
from user import User

def test__init__():
    profile = Profile()
    assert profile.title == ""
    assert profile.major == ""
    assert profile.university == ""
    assert profile.about == ""
    assert profile.experience == []
    assert profile.education == []

def test_add_experience(monkeypatch):
    profile = Profile()

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    experience = Experience("SWE", "USF", "2020", "2021", "Tampa", "LOL")
    assert len(profile.experience) == 0

    # Add experience successful
    error_message = profile.add_experience(experience)
    assert error_message == None
    assert len(profile.experience) == 1

    error_message = profile.add_experience(experience)
    assert error_message == None
    assert len(profile.experience) == 2

    error_message = profile.add_experience(experience)
    assert error_message == None
    assert len(profile.experience) == 3

    # Add experience unsuccessful
    error_message = profile.add_experience(experience)
    assert error_message == MAX_ALLOWED_EXPERIENCES_ERROR_MESSAGE
    assert len(profile.experience) == 3

def test_delete_experience(monkeypatch):
    profile = Profile()
    
    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    experience = Experience("SWE", "USF", "2020", "2021", "Tampa", "LOL")
    profile.experience = [experience]
    assert len(profile.experience) == 1

    # Delete experience successful
    error_message = profile.delete_experience(0)
    assert error_message == None
    assert len(profile.experience) == 0

    # Delete experience unsuccessful
    error_message = profile.delete_experience(0)
    assert error_message == EXPERIENCE_INDEX_OUT_OF_RANGE
    assert len(profile.experience) == 0

    # Delete experience unsuccessful
    error_message = profile.delete_experience(-1)
    assert error_message == EXPERIENCE_INDEX_OUT_OF_RANGE
    assert len(profile.experience) == 0

def test_add_education(monkeypatch):
    profile = Profile()

    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    education = Education("USF", "BSc", "2020-2021")
    assert len(profile.education) == 0

    # Add experience successful
    error_message = profile.add_education(education)
    assert error_message == None
    assert len(profile.education) == 1


def test_delete_education(monkeypatch):
    profile = Profile()
    
    # Replaces User update_users_file function by a lambda function that returns None
    monkeypatch.setattr(User, "update_users_file", lambda: None)

    education = Education("USF", "BSc", "2020-2021")
    profile.education = [education]
    assert len(profile.education) == 1

    # Delete education successful
    error_message = profile.delete_education(0)
    assert error_message == None
    assert len(profile.education) == 0

    # Delete education unsuccessful
    error_message = profile.delete_education(0)
    assert error_message == EDUCATION_INDEX_OUT_OF_RANGE
    assert len(profile.education) == 0

    # Delete education unsuccessful
    error_message = profile.delete_education(-1)
    assert error_message == EDUCATION_INDEX_OUT_OF_RANGE
    assert len(profile.education) == 0