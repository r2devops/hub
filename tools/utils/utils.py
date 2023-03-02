#!/usr/bin/env python3

import os
import logging
import sys
import yaml
from os import getenv, listdir

class Config():
    def __init__(self):
        """Constructor of the config object
        Returns
        -------
        nothing
        """
        # Job variables
        self.JOBS_DIR = "jobs"
        self.TOOLS_DIR = "tools"
        self.JOB_TEMPLATE_DIR = "job_template"
        self.JOB_DIR = "r2_jobname"
        self.JOB_DESCRIPTION_FILE = "README.md"
        self.JOBS_EXTENSION = ".yml"
        # Directory name to use for the jobs screenshot
        self.SCREENSHOTS_DIR = "screenshots"
        self.ISSUES_LIMIT = 5

        # Logging
        self.LOGFILE_NAME = os.getenv("JOB_LOGFILE")
        self.EXIT_SUCCESS = 0
        self.EXIT_FAILURE = 1

        # Requests variable & API Variables
        self.GITLAB_BASE_URL = "https://gitlab.com/"
        self.GITLAB_API_URL = "https://gitlab.com/api/v4/"
        self.R2DEVOPS_URL = "https://jobs.r2devops.io/"
        self.PROJECT_NAME = "r2devops/hub"
        self.JOBS_SCOPE_LABEL = "Jobs::"
        self.LABEL_COLOR = "fuchsia"
        self.JOB_TOKEN = getenv("API_TOKEN")

        # Check in Constructor
        if not self.LOGFILE_NAME:
            self.LOGFILE_NAME = "default_logfile.log"

    def __str__(self):
        """ Print function, return an string representation of the config object
        Returns
        -------
        str
            All keys and values of the config
        """
        return ''.join("%s: %s \n" % item for item in vars(self).items())



if __name__ == "__main__":
    """Main function, print all the config
    Returns
    -------
    str
        All keys and values of the config
    """

    config = Config()
    print(config)
