from education import Education


def test_education_section(monkeypatch, capfd):
    schoolName = "Test School Name"
    degree = "Test Degree"
    '''
    yearStart = 2000
    yearEnd = 2004
    '''
    yearsAttended = "2000-2004"
    education = Education(schoolName, degree, yearsAttended)

    assert education.schoolName == schoolName
    assert education.degree == degree
    assert education.yearsAttended == yearsAttended