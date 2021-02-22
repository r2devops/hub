#!/usr/bin/env python3

import os
import logging
import sys
import yaml
from os import getenv, listdir

class Config:
    # Job variables
    JOBS_DIR = "jobs"
    TOOLS_DIR = "tools"
    JOB_TEMPLATE_DIR = "job_template"
    JOB_DIR = "job_name"
    JOB_YAML = "job.yml"
    JOB_DESCRIPTION_FILE = "README.md"
    JOB_METADATA_FILE = "job.yml"
    JOBS_EXTENSION = ".yml"
    JOB_CHANGELOG_DIR = "versions"
    # Directory name to use for the jobs screenshot
    SCREENSHOTS_DIR = "screenshots"
    ISSUES_LIMIT = 5

    # Logging
    LOGFILE_NAME = os.getenv("JOB_LOGFILE")
    EXIT_SUCCESS = 0
    EXIT_FAILURE = 1

    # Mkdocs
    MKDOCS_DIR = "docs"
    MKDOCS_PLACEHOLDER_FILE = "placeholder.md"
    MARKDOWN_EXTENSION = ".md"
    # Path to images used for the built job documentation
    MKDOCS_DIR_JOBS_IMAGES = "images/jobs"

    # Requests variable & API Variables
    GITLAB_BASE_URL = "https://gitlab.com/"
    GITLAB_API_URL = "https://gitlab.com/api/v4/"
    R2DEVOPS_URL = "https://jobs.r2devops.io/"
    PROJECT_NAME = "r2devops/hub"
    JOBS_SCOPE_LABEL = "Jobs::"
    LABEL_COLOR = "fuchsia"
    JOB_TOKEN = getenv("API_TOKEN")

    # Templates variables
    BUILDER_DIR = "tools/builder"
    TEMPLATE_DIR = "templates"
    TEMPLATE_INDEX = "index.md.j2"
    TEMPLATE_DOC = "job_documentation.md.j2"
    TEMPLATE_PLACEHOLDER = "placeholder.md.j2"
    TEMPLATE_LICENSE_DIR = "licenses"
    INDEX_FILE = "index.md"

    # List of stages
    INDEX = {
        "static_tests": {"name":"Static_tests","icon":"🔎","content":[], "description":"Static testing of repository files"},
        "build": {"name":"Build","icon":"🧱","content":[], "description":"Building and packaging of software"},
        "dynamic_tests": {"name":"Dynamic_tests","icon":"🔥","content":[], "description":"Dynamic testing of a running version of the software"},
        "provision": {"name":"Provision","icon":"🛠","content":[], "description":"Preparation of the software infrastructure"},
        "review": {"name":"Review","icon":"👌","content":[], "description":"Deployment of the software in an isolated review environment"},
        "release": {"name":"Release","icon":"🏷","content":[], "description":"Releasing and tagging of the software"},
        "deploy": {"name":"Deploy","icon":"🚀","content":[], "description":"Deployment of the software on environments"},
        "others": {"name":"Others","icon":"🦄","content":[], "description":"All other magic jobs not included in previous stages"}
    }




if __name__ == "__main__":
    """Main function, iterating over job structures to compare to the tempale one

    Returns
    -------
    0
        In case nothing was mismatched
    Number
        Number of jobs that doesn't match the template
    """
    # Setup logging
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOGFILE_NAME),
            logging.StreamHandler()
        ]
    )
