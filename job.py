import pickle

from os import path

MAX_JOBS = 5

MAX_ALLOWED_JOBS_ERROR_MESSAGE = "Max number of job postings has been reached. (5)"

class Job:
    JOBS_FILE_NAME = "jobs.pickle"
    jobs = []

    # Constructs an actual Job Post using these parameters from the job screen.
    def __init__(self, title, description, employer, location, salary, author_first_name, author_last_name):
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name

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
        with open(Job.JOBS_FILE_NAME, 'wb') as jobs_file:
            pickle.dump(Job.jobs, jobs_file)

    # Saves the job posting.
    def save(self):
        """
        save method retuns a user intended message when the job information
        does not meet the requirements.
        """
        if len(Job.jobs) >= MAX_JOBS:
            return MAX_ALLOWED_JOBS_ERROR_MESSAGE

        self.jobs.append(self)
        Job.update_jobs_file()