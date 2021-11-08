import builtins
import io
import pickle

from os import path
from job import FATAL_DUPLICATED_JOB_ID, JOB_AUTHOR_ERROR_MESSAGE, JOB_NOT_FOUND_ERROR_MESSAGE, MAX_ALLOWED_JOBS_ERROR_MESSAGE, MAX_JOBS, Job

def test__init__():
    job = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    assert job.id == None
    assert job.title == "SWE"
    assert job.description == "Just code!"
    assert job.employer == "USF"
    assert job.location == "Tampa, FL"
    assert job.salary == "80000"
    assert job.author_username == None

def test_load_jobs_file(monkeypatch):
    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    job1.id = 0

    job2 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    job2.id = 1

    jobs = {job1.id: job1, job2.id: job2}

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

    assert job1.id == Job.jobs[job1.id].id
    assert job1.title == Job.jobs[job1.id].title
    assert job1.description == Job.jobs[job1.id].description
    assert job1.employer == Job.jobs[job1.id].employer
    assert job1.location == Job.jobs[job1.id].location
    assert job1.salary == Job.jobs[job1.id].salary
    assert job1.author_username == Job.jobs[job1.id].author_username

    assert job2.id == Job.jobs[job2.id].id
    assert job2.title == Job.jobs[job2.id].title
    assert job2.description == Job.jobs[job2.id].description
    assert job2.employer == Job.jobs[job2.id].employer
    assert job2.location == Job.jobs[job2.id].location
    assert job2.salary == Job.jobs[job2.id].salary
    assert job2.author_username == Job.jobs[job2.id].author_username

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

    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    job1.id = 0

    job2 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    job2.id = 1

    Job.jobs = {job1.id: job1, job2.id: job2}

    Job.update_jobs_file()

    jobs_file.seek(0)
    jobs = pickle.load(jobs_file)
    # Closes the file
    jobs_file.close = close
    jobs_file.close()

    assert len(jobs) == len(Job.jobs)

    assert job1.id == Job.jobs[job1.id].id
    assert job1.title == Job.jobs[job1.id].title
    assert job1.description == Job.jobs[job1.id].description
    assert job1.employer == Job.jobs[job1.id].employer
    assert job1.location == Job.jobs[job1.id].location
    assert job1.salary == Job.jobs[job1.id].salary
    assert job1.author_username == Job.jobs[job1.id].author_username

    assert job2.id == Job.jobs[job2.id].id
    assert job2.title == Job.jobs[job2.id].title
    assert job2.description == Job.jobs[job2.id].description
    assert job2.employer == Job.jobs[job2.id].employer
    assert job2.location == Job.jobs[job2.id].location
    assert job2.salary == Job.jobs[job2.id].salary
    assert job2.author_username == Job.jobs[job2.id].author_username

def test_load_next_job_id_file(monkeypatch):
    next_job_id = 10

    # Creates in-memory bytes file and dumps the next_job_id on it
    next_job_id_file = io.BytesIO()
    pickle.dump(next_job_id, next_job_id_file)
    next_job_id_file.seek(0)

    def mock_open(path, mode):
        assert path == Job.NEXT_JOB_ID_FILE_NAME
        assert mode == "rb"
        return next_job_id_file
    
    # Replaces open buildt-in function by mock_open
    monkeypatch.setattr(builtins, "open", mock_open)
    # Replaces python os.path isfile function by a lambda function that returns False
    monkeypatch.setattr(path, "isfile", lambda *arg: False)
    # Replaces Job update_next_job_id_file function by a lambda function that returns None
    monkeypatch.setattr(Job, "update_next_job_id_file", lambda: None)

    Job.load_next_job_id_file()
    Job.next_job_id == next_job_id

def test_update_next_job_id_file(monkeypatch):
    # Creates in-memory bytes file
    next_job_id_file = io.BytesIO()
    close = next_job_id_file.close
    # Prevent file from being closed
    next_job_id_file.close = lambda: None

    def mock_open(path, mode):
        assert path == Job.NEXT_JOB_ID_FILE_NAME
        assert mode == "wb"
        return next_job_id_file
    
    # Replaces open buildt-in function with mock_open
    monkeypatch.setattr(builtins, "open", mock_open)

    Job.next_job_id = 10
    Job.update_next_job_id_file()

    next_job_id_file.seek(0)
    next_job_id = pickle.load(next_job_id_file)
    # Closes the file
    next_job_id_file.close = close
    next_job_id_file.close()

    assert next_job_id == 10

def test_delete(monkeypatch):
    job = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    job.id = 0
    job.author_username = "jhondoe"

    Job.jobs = {job.id: job}

    # Replaces Job update_jobs_file function by a lambda function that returns None
    monkeypatch.setattr(Job, "update_jobs_file", lambda: None)

    # Test job author error
    assert len(Job.jobs) == 1
    error_message = Job.delete(0, "jhon")
    assert error_message == JOB_AUTHOR_ERROR_MESSAGE
    assert len(Job.jobs) == 1

    # Test successful
    assert len(Job.jobs) == 1
    error_message = Job.delete(0, "jhondoe")
    assert error_message == None
    assert len(Job.jobs) == 0

    # Test job not found error
    error_message = Job.delete(0, "jhondoe")
    assert error_message == JOB_NOT_FOUND_ERROR_MESSAGE
    assert len(Job.jobs) == 0

def test_save(monkeypatch):      
    Job.next_job_id = 0
    Job.jobs = {}

    # Replaces Job update_jobs_file function by a lambda function that returns None
    monkeypatch.setattr(Job, "update_jobs_file", lambda: None)
    # Replaces Job update_next_job_id_file function by a lambda function that returns None
    monkeypatch.setattr(Job, "update_next_job_id_file", lambda: None)
    
    # Test save successful
    for i in range(10):
        job = Job(f"SWE_{i}", "Just code!", "USF", "Tampa, FL", "80000")
        error_message = job.save("jhondoe")
        assert error_message == None

    # Test error max allowed jobs
    job1 = Job("SWE", "Just code!", "USF", "Tampa, FL", "80000")
    error_message = job1.save("jhondoe")
    assert error_message == MAX_ALLOWED_JOBS_ERROR_MESSAGE
    assert len(Job.jobs) == MAX_JOBS

    # Test error duplicated job id
    del Job.jobs[Job.next_job_id - 1]
    job1.id = Job.next_job_id - 2
    error_message = job1.save("jhondoe")
    assert error_message == FATAL_DUPLICATED_JOB_ID
    assert len(Job.jobs) == MAX_JOBS - 1