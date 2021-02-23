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
        self.JOB_DIR = "job_name"
        self.JOB_YAML = "job.yml"
        self.JOB_DESCRIPTION_FILE = "README.md"
        self.JOB_METADATA_FILE = "job.yml"
        self.JOBS_EXTENSION = ".yml"
        self.JOB_CHANGELOG_DIR = "versions"
        # Directory name to use for the jobs screenshot
        self.SCREENSHOTS_DIR = "screenshots"
        self.ISSUES_LIMIT = 5

        # Logging
        self.LOGFILE_NAME = os.getenv("JOB_LOGFILE")
        self.EXIT_SUCCESS = 0
        self.EXIT_FAILURE = 1

        # Mkdocs
        self.MKDOCS_DIR = "docs"
        self.MKDOCS_PLACEHOLDER_FILE = "placeholder.md"
        self.MARKDOWN_EXTENSION = ".md"
        # Path to images used for the built job documentation
        self.MKDOCS_DIR_JOBS_IMAGES = "images/jobs"

        # Requests variable & API Variables
        self.GITLAB_BASE_URL = "https://gitlab.com/"
        self.GITLAB_API_URL = "https://gitlab.com/api/v4/"
        self.R2DEVOPS_URL = "https://jobs.r2devops.io/"
        self.PROJECT_NAME = "r2devops/hub"
        self.JOBS_SCOPE_LABEL = "Jobs::"
        self.LABEL_COLOR = "fuchsia"
        self.JOB_TOKEN = getenv("API_TOKEN")

        # Templates variables
        self.BUILDER_DIR = "tools/builder"
        self.TEMPLATE_DIR = "templates"
        self.TEMPLATE_INDEX = "index.md.j2"
        self.TEMPLATE_DOC = "job_documentation.md.j2"
        self.TEMPLATE_PLACEHOLDER = "placeholder.md.j2"
        self.TEMPLATE_LICENSE_DIR = "licenses"
        self.INDEX_FILE = "index.md"

        # List of stages
        self.INDEX = {
            "static_tests": {"name":"Static_tests","icon":"🔎","content":[], "description":"Static testing of repository files"},
            "build": {"name":"Build","icon":"🧱","content":[], "description":"Building and packaging of software"},
            "dynamic_tests": {"name":"Dynamic_tests","icon":"🔥","content":[], "description":"Dynamic testing of a running version of the software"},
            "provision": {"name":"Provision","icon":"🛠","content":[], "description":"Preparation of the software infrastructure"},
            "review": {"name":"Review","icon":"👌","content":[], "description":"Deployment of the software in an isolated review environment"},
            "release": {"name":"Release","icon":"🏷","content":[], "description":"Releasing and tagging of the software"},
            "deploy": {"name":"Deploy","icon":"🚀","content":[], "description":"Deployment of the software on environments"},
            "others": {"name":"Others","icon":"🦄","content":[], "description":"All other magic jobs not included in previous stages"}
        }


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