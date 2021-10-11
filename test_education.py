from education import Education

def test__init__():
    schoolName = "Test School Name"
    degree = "Test Degree"
    years_attended = "2000-2004"
    education = Education(schoolName, degree, years_attended)

    assert education.school_name == schoolName
    assert education.degree == degree
    assert education.years_attended == years_attended