#!/usr/bin/env python3

# API documentation: https://docs.gitlab.com/ee/api/labels.html
#

import logging
import sys
from urllib.parse import quote, urlencode
from os import getenv, listdir
import requests
import argparse

# Import the config module
from tools.utils.utils import Config
utils = Config()

def get_labels(project_name, with_counts=False, include_ancestor_groups=True, search=""):
    """Get labels of the project, can also serach for a specific label with search filter

    Parameters:
    -----------
    project_name : str
        The name of the project
    with_counts : boolean
        Whether or not to include issue and merge request counts (default : false)
    include_ancestor_groups : boolean
        Include ancestor groups (default : true)
    search : str
        Feywords to filter labels by (default : None)

    Returns:
    --------
    obj
        Response to the request
    """
    headers = {
        'PRIVATE-TOKEN': utils.JOB_TOKEN
    }
    payload = {
        'with_counts': with_counts,
        'include_ancestors_groups': include_ancestor_groups,
        'search': search
    }
    base_label_url = f"{utils.GITLAB_API_URL}/projects/{quote(project_name, safe='')}" + "/labels"
    url = f"{base_label_url}?{urlencode(payload)}"
    logging.info(f"Getting the list of issues from the project {project_name} filtered by {search}")
    return (requests.get(url, headers=headers))

def create_label(project_name, label_name, label_color=utils.LABEL_COLOR):
    """Create a new label for a job

    Parameters:
    -----------
    project_name : str
        The name of the project
    label_name : str
        The name of the label to create
    label_color : str
        6-digit hex notation with leading '#'
        or one of the CSS color names (default: fuchsia)

    Returns:
    --------
    obj
        Response to the request
    """
    headers = {
        'PRIVATE-TOKEN': utils.JOB_TOKEN
    }
    payload = {
        "name": label_name,
        "color": label_color,
        "description": f"Issues related to {label_name}"
    }
    url = f"{utils.GITLAB_API_URL}/projects/{quote(project_name, safe='')}/labels"
    logging.info(f"Creating a label {label_name} for the project {project_name}")
    return (requests.post(url, headers=headers, data=payload))

def delete_label(project_name, label_name):
    """Delete a label for the project

    Parameters:
    -----------
    proejct_name : str
        The name of the project
    label_name : str
        The name of the label to delete

    Returns:
    --------
    obj:
        Response to the request
    """
    headers = {
        'PRIVATE-TOKEN': utils.JOB_TOKEN
    }
    url = f"{utils.GITLAB_API_URL}/projects/{quote(project_name, safe='')}/labels/{label_name}"
    logging.info(f"Deleting a label {label_name} for the project {project_name}")
    return (requests.delete(url, headers=headers))

def argparse_setup():
    """Setup argparse

    Return
    ------
    obj
        Python object with arguments parsed
    """
    parser = argparse.ArgumentParser()
    return parser.parse_args()

if __name__ == "__main__":
    """Main function if used as a program
    Looping through all jobs to check if their scoped
    label exist or if we need to create it

    Returns:
    --------
    boolean
        0 if nothing is wrong, 1 otherwise
    """
    # Setup argparse
    args = argparse_setup()

    # Setup logging
    logging.basicConfig(
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(utils.LOGFILE_NAME),
            logging.StreamHandler()
        ]
    )

    jobs = listdir(utils.JOBS_DIR)
    for job in jobs:
        job_label = utils.JOBS_SCOPE_LABEL + job
        label = get_labels(utils.PROJECT_NAME, search=job_label)
        if "Unauthorized" not in label.text:
            if label.json():
                logging.info(f"Label {job} exist")
            else:
                logging.info(f"Label {job} does not exist, creating one now")
                create_label(utils.PROJECT_NAME, job_label)
        else:
            logging.error("Not Authorized, verify the API_TOKEN environment variable in the gitlab project")
            sys.exit(1)
