import builtins
import io
import pickle

from os import path
from job import MAX_ALLOWED_JOBS_ERROR_MESSAGE, MAX_JOBS, Job

def test__init__():
    job = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Connor")
    assert job.title == "SWE"
    assert job.description == "Just code!"
    assert job.employer == "USF"
    assert job.location == "Tampa, FL"
    assert job.salary == "80000"
    assert job.author_first_name == "John"
    assert job.author_last_name == "Connor"

def test_load_jobs_file(monkeypatch):
    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Connor")
    job2 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Doe")

    jobs = [job1, job2]

    # Creates in-memory bytes file and dumps the jobs on it
    jobs_file = io.BytesIO()
    pickle.dump(jobs, jobs_file)
    jobs_file.seek(0)

    def mock_open(path, mode):
        assert path == Job.JOBS_FILE_NAME
        assert mode == "rb"
        return jobs_file
    
    # Replaces open buildt-in function by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    # Replaces python os.path isfile function by a lambda function that returns False
    monkeypatch.setattr(path, "isfile", lambda *arg: False)
    # Replaces Job update_jobs_file function by a lambda function that returns None
    monkeypatch.setattr(Job, "update_jobs_file", lambda: None)

    Job.load_jobs_file()
    assert len(Job.jobs) == len(jobs)
    
    assert job1.title == Job.jobs[0].title
    assert job1.description == Job.jobs[0].description
    assert job1.employer == Job.jobs[0].employer
    assert job1.location == Job.jobs[0].location
    assert job1.salary == Job.jobs[0].salary
    assert job1.author_first_name == Job.jobs[0].author_first_name
    assert job1.author_last_name == Job.jobs[0].author_last_name
    
    assert job2.title == Job.jobs[1].title
    assert job2.description == Job.jobs[1].description
    assert job2.employer == Job.jobs[1].employer
    assert job2.location == Job.jobs[1].location
    assert job2.salary == Job.jobs[1].salary
    assert job2.author_first_name == Job.jobs[1].author_first_name
    assert job2.author_last_name == Job.jobs[1].author_last_name

def test_update_jobs_file(monkeypatch):
    # Creates in-memory bytes file
    jobs_file = io.BytesIO()
    close = jobs_file.close
    # Prevent file from being closed
    jobs_file.close = lambda: None

    def mock_open(path, mode):
        assert path == Job.JOBS_FILE_NAME
        assert mode == "wb"
        return jobs_file
    
    # Replaces open buildt-in function with mock_open
    monkeypatch.setattr(builtins, "open", mock_open)

    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Connor")
    job2 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Doe")

    Job.jobs = [job1, job2]

    Job.update_jobs_file()

    jobs_file.seek(0)
    jobs = pickle.load(jobs_file)
    # Closes the file
    jobs_file.close = close
    jobs_file.close()

    assert len(jobs) == len(Job.jobs)
    
    assert job1.title == Job.jobs[0].title
    assert job1.description == Job.jobs[0].description
    assert job1.employer == Job.jobs[0].employer
    assert job1.location == Job.jobs[0].location
    assert job1.salary == Job.jobs[0].salary
    assert job1.author_first_name == Job.jobs[0].author_first_name
    assert job1.author_last_name == Job.jobs[0].author_last_name
    
    assert job2.title == Job.jobs[1].title
    assert job2.description == Job.jobs[1].description
    assert job2.employer == Job.jobs[1].employer
    assert job2.location == Job.jobs[1].location
    assert job2.salary == Job.jobs[1].salary
    assert job2.author_first_name == Job.jobs[1].author_first_name
    assert job2.author_last_name == Job.jobs[1].author_last_name

def test_save(monkeypatch):
    monkeypatch.setattr(Job, "update_jobs_file", lambda: None)
    Job.jobs = []

    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000", "John", "Connor")
    
    # Test save successful
    error_message = job1.save()
    assert error_message == None

    error_message = job1.save()
    assert error_message == None
    
    error_message = job1.save()
    assert error_message == None

    error_message = job1.save()
    assert error_message == None
    
    error_message = job1.save()
    assert error_message == None

    # Test save unsuccessful
    error_message = job1.save()
    assert error_message == MAX_ALLOWED_JOBS_ERROR_MESSAGE
    assert len(Job.jobs) == MAX_JOBS