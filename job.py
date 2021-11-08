import pickle

from os import path

MAX_JOBS = 10

MAX_ALLOWED_JOBS_ERROR_MESSAGE = "Max number of job postings has been reached. (10)"
FATAL_DUPLICATED_JOB_ID = "Fatal: other job has been found with the new job id."
JOB_NOT_FOUND_ERROR_MESSAGE = "Job not found."
JOB_AUTHOR_ERROR_MESSAGE = "Only job authors can delete its jobs."
ALREADY_APPLIED_TO_THIS_JOB = "Already applied to this job."


class Job:
    JOBS_FILE_NAME = "jobs.pickle"
    jobs = {}
    NEXT_JOB_ID_FILE_NAME = "next_job_id.pickle"
    next_job_id = 0

    # Constructs an actual Job Post using these parameters from the job screen.
    def __init__(self, title, description, employer, location, salary):
        self.id = None
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.author_username = None
        self.applications = {}

    # Loads the JOBS_FILE_NAME file, if it doesn't exist it creates a new one.
    @staticmethod
    def load_jobs_file():
        if not path.isfile(Job.JOBS_FILE_NAME):
            Job.update_jobs_file()

        with open(Job.JOBS_FILE_NAME, "rb") as jobs_file:
            Job.jobs = pickle.load(jobs_file)

    # Creates a the jobs file and dumps Job.jobs list.
    @staticmethod
    def update_jobs_file():
        with open(Job.JOBS_FILE_NAME, "wb") as jobs_file:
            pickle.dump(Job.jobs, jobs_file)

    # Loads the NEXT_JOB_ID_FILE_NAME file, if it doesn't exists it creates a new one.
    @staticmethod
    def load_next_job_id_file():
        if not path.isfile(Job.NEXT_JOB_ID_FILE_NAME):
            Job.update_next_job_id_file()

        with open(Job.NEXT_JOB_ID_FILE_NAME, "rb") as next_job_id_file:
            Job.next_job_id = pickle.load(next_job_id_file)

    # Creates the next_job_id file and dumps Jobs.next_job_id .
    @staticmethod
    def update_next_job_id_file():
        with open(Job.NEXT_JOB_ID_FILE_NAME, "wb") as next_job_id_file:
            pickle.dump(Job.next_job_id, next_job_id_file)

    # Deletes the job posting
    @staticmethod
    def delete(job_id, current_username):
        if job_id not in Job.jobs:
            return JOB_NOT_FOUND_ERROR_MESSAGE

        job = Job.jobs[job_id]
        if current_username != job.author_username:
            return JOB_AUTHOR_ERROR_MESSAGE

        del Job.jobs[job_id]
        Job.update_jobs_file()

    # Saves the job posting.
    def save(self, current_username):
        """
        save method retuns a user intended message when the job information
        does not meet the requirements.
        """
        if len(Job.jobs) >= MAX_JOBS:
            return MAX_ALLOWED_JOBS_ERROR_MESSAGE

        if self.id in self.jobs:
            return FATAL_DUPLICATED_JOB_ID

        self.id = Job.next_job_id
        self.author_username = current_username
        Job.jobs[Job.next_job_id] = self
        Job.update_jobs_file()

        Job.next_job_id += 1
        Job.update_next_job_id_file()

    def add_application(self, application):
        if application.username in self.applications:
            return ALREADY_APPLIED_TO_THIS_JOB

        self.applications[application.username] = application
        Job.update_jobs_file()
