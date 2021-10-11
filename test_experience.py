from experience import Experience

def test__init__():
    experience = Experience("Testing", "TestEmployer", "Jan1", "Dec31", "Tampa", "Internship")
    assert experience.title == "Testing"
    assert experience.employer == "TestEmployer"
    assert experience.date_started == "Jan1"
    assert experience.date_ended == "Dec31"
    assert experience.location == "Tampa"
    assert experience.description == "Internship"
