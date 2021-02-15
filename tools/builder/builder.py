#!/usr/bin/env python3

# This script is used to build the documentation that
# r2devops.io will be using for every job added to the hub

# Directory skeleton for a job:
# ── jobs
#     └── <job_name>
#         ├── <job_name>.yml
#         ├── LICENSE
#         ├── job.yml
#         ├── README.md
#         └── versions
#             ├── 0.1.0.md
#             └──...

import logging
import re
import sys
from datetime import datetime
from distutils.version import LooseVersion
from os import listdir, makedirs
from shutil import copyfile
from urllib.parse import quote, urlencode
import requests
from yaml import full_load, YAMLError
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Job variables
JOBS_DIR = "jobs"
MKDOCS_DIR = "docs"

MKDOCS_PLACEHOLDER_FILE = "placeholder.md"
JOB_CHANGELOG_DIR = "versions"

JOB_DESCRIPTION_FILE = "README.md"
JOB_METADATA_FILE = "job.yml"
JOBS_EXTENSION = ".yml"
MARKDOWN_EXTENSION = ".md"

# Path to images used for the built job documentation
MKDOCS_DIR_JOBS_IMAGES = "images/jobs"
# Directory name to use for the jobs screenshot
SCREENSHOTS_DIR = "screenshots"
ISSUES_LIMIT = 5

# Requests variable
GITLAB_BASE_URL = "https://gitlab.com/"
GITLAB_API_URL = "https://gitlab.com/api/v4/"
R2DEVOPS_URL = "https://jobs.r2devops.io/"
PROJECT_NAME = "r2devops/hub"
JOBS_SCOPE_LABEL = "Jobs::"

# Templates variables
BUILDER_DIR = "tools/builder"
TEMPLATE_DIR = "templates"
TEMPLATE_INDEX = "index.md.j2"
TEMPLATE_DOC = "job_documentation.md.j2"
TEMPLATE_PLACEHOLDER = "placeholder.md.j2"
TEMPLATE_LICENSE_DIR = "licenses"
INDEX_FILE = "index.md"

# List of available labels for jobs
labels_list = ["GitLab","Build","Container","Docker","PHP", "Testing","Utilities","Yarn", "Dependency scan", "Security","Python","API", "Documentation","Quality","SAST","Linter","Helm","DAST","Kubernetes","NPM"]
set_labels_list = set(labels_list)

index = {
    "static_tests": {"name":"Static_tests","icon":"🔎","content":[], "description":"Static testing of repository files"},
    "build": {"name":"Build","icon":"🧱","content":[], "description":"Building and packaging of software"},
    "dynamic_tests": {"name":"Dynamic_tests","icon":"🔥","content":[], "description":"Dynamic testing of a running version of the software"},
    "provision": {"name":"Provision","icon":"🛠","content":[], "description":"Preparation of the software infrastructure"},
    "review": {"name":"Review","icon":"👌","content":[], "description":"Deployment of the software in an isolated review environment"},
    "release": {"name":"Release","icon":"🏷","content":[], "description":"Releasing and tagging of the software"},
    "deploy": {"name":"Deploy","icon":"🚀","content":[], "description":"Deployment of the software on environments"},
    "others": {"name":"Others","icon":"🦄","content":[], "description":"All other magic jobs not included in previous stages"}
}

def get_conf(job_path):
    """Parse the YAML config of the job

    Args:
        job_path (string): Path to job.yml

    Returns:
        (dict): Object of parsed YAML
    """
    try:
        with open(job_path + "/" + JOB_METADATA_FILE) as conf_file:
            return full_load(conf_file)
    except YAMLError as error:
        logging.error("Failed to parse job config '%s/%s", job_path,
                      JOB_METADATA_FILE )
        logging.error(error)
        sys.exit(1)
    except OSError as error:
        logging.error("Failed to open and read job config '%s/%s",
                      job_path, JOB_METADATA_FILE )
        logging.error(error)
        sys.exit(1)

def get_description(job_path):
    """Fetch the README file from job

    Args:
        job_path (string): Path the job folder

    Returns:
        (string): Full README file
    """
    try:
        with open(job_path + "/" + JOB_DESCRIPTION_FILE) as readme_file:
            return readme_file.read()
    except OSError as error:
        logging.error("Failed to open and read file README %s", job_path)
        logging.error(error)
        sys.exit(1)

def get_changelogs(job_path, job_name):
    """Fetch the changelogs file from job

    Args:
        job_path (string): Path the job folder
        job_name (string): Name of the job

    Returns:
        latest (dict): data about latest version
        changelogs (list): list of data about each versions
    """
    versions = listdir(job_path + "/" + JOB_CHANGELOG_DIR)
    versions = [version[:-3] for version in versions]
    versions = sorted(versions, key=LooseVersion, reverse=True)
    latest = {
      "version": versions[0],
      "url": R2DEVOPS_URL + job_name + JOBS_EXTENSION
    }
    changelogs = []
    try:
        for version in versions:
            with open(job_path + "/" + JOB_CHANGELOG_DIR + "/" + version + MARKDOWN_EXTENSION) as changelog_file:
                changelogs.append({
                    "version": version,
                    "url": R2DEVOPS_URL + version + "/" + job_name + JOBS_EXTENSION,
                    "changelog": changelog_file.readlines()
                })
    except OSError as error:
        logging.error("Failed to open and read versions files of %s", job_name)
        logging.error(error)
        sys.exit(1)

    return (latest, changelogs)

def get_license(license_name, copyright_holder):
    """Return the license file

    Args:
        licence_name (string): name of the licence
        copyright_holder (string): gitlab name of the job maitainer

    Returns:
        license_content (string): content of the license
    """
    try:
        env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR + "/" + TEMPLATE_LICENSE_DIR))
        template = env.get_template(license_name + MARKDOWN_EXTENSION + ".j2")
        license_content = template.render(
            year = datetime.now().year,
            copyright_holder = copyright_holder
        ).split('\n')
        license_content = [ line + '\n' for line in license_content]
    except TemplateNotFound as error:
        logging.error("Failed to fetch the template for license %s and copyright holder: %s", license_name, copyright_holder)
        logging.error(error)
        sys.exit(1)

    return license_content

def get_screenshots(job_path, job_name):
    """Create the job directory for the job documentation
       Gets the jobs screenshots and copy them to the documentation directory

    Parameters
    ----------
    job_path : str
        The job path
    job_name : str
        The job name (ex: gitleaks)

    Returns
    -------
    str
        Path to the documentation directory
    list
        List of all screenshots name for the job
    """

    # Create screenshots folder in docs for the job
    makedirs(MKDOCS_DIR+"/"+MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+SCREENSHOTS_DIR,0o777,True)

    # Get all screenshots of the job
    regex = re.compile('(.png|.jpg|.jpeg)$')
    screenshot_list = listdir(job_path + "/" + SCREENSHOTS_DIR)
    screenshot_list = list(filter(regex.search, screenshot_list))

    # Copy all screenshot of the job into screenshots folder for the doc
    for screenshot in screenshot_list:
        copyfile(job_path + "/" + SCREENSHOTS_DIR+"/"+screenshot, MKDOCS_DIR+ "/"+ MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+SCREENSHOTS_DIR+"/"+screenshot)

    return ("/" + MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+SCREENSHOTS_DIR, screenshot_list)

def get_user(code_owner):
    """Fetch the job maintainer Gitlab user

    Args:
        code_owner (string): gitlab name of the job maitainer

    Returns:
        (dict): user data
    """
    url = GITLAB_API_URL + "users?username=" + code_owner

    response = requests.request("GET", url)

    try:
        if response.status_code == 200:
            return response.json()[0]

        raise Exception('Expected 200 status code, but got {}'.format(response.status_code))
    except IndexError as error:
        logging.error("Unexpected error when retrieving user %s", code_owner)
        logging.error(error)
        sys.exit(1)
    except Exception as error:
        logging.error("User %s was not found", code_owner)
        logging.error(error)
        sys.exit(1)

    return None

def get_job_raw_content(job_name):
    """Return the raw content of a job

    Parameters
    ----------
    job_name : str
        The job name (ex: gitleaks)

    Returns
    -------
    yaml
        Raw content of the job
    """
    try:
        with open("{}/{job}/{job}{}".format(JOBS_DIR, JOBS_EXTENSION,
                                            job=job_name), 'r') as job:
            return job.readlines()
    except FileNotFoundError :
        logging.error("File %s/%s/%s.%s not found", JOBS_DIR,
                                                    job_name,
                                                    job_name,
                                                    JOBS_EXTENSION)
        sys.exit(1)

# https://docs.gitlab.com/ee/api/issues.html#list-project-issues (for the structure of the response)
def get_linked_issues(job_name, opened=True):
    """Get a list of linked issues for a job

    Parameters:
    -----------
    job_name : str
        The name of the job
    opened : boolean
        If we get only opened issues or all of them (default: True)

    Returns:
    --------
    list
        A list of issues linked to the job with their name and url
    str
        Url to list the issues related to the job
    str
        Url to create a new issue for the job
    """
    linked_issues = []
    base_url = f"{GITLAB_API_URL}/projects/{quote(PROJECT_NAME, safe='')}/issues"
    url = f"{base_url}?labels={JOBS_SCOPE_LABEL}{job_name}"
    if opened:
        url += "&state=opened"
    r = requests.get(url)

    for issue in r.json():
        linked_issues.append({
            "name": issue['title'],
            "url": issue['web_url'],
            "iid": issue['iid']
        })
    issues_base_url = f"{GITLAB_BASE_URL}/{PROJECT_NAME}"
    linked_issues_payload = {
        "label_name": f"{JOBS_SCOPE_LABEL}{job_name}"
    }
    linked_issues_url = f"{issues_base_url}/issues?{urlencode(linked_issues_payload)}"
    create_issue_payload = f"issue[title]=[job][{job_name}]"
    create_issue_url = f"{issues_base_url}/issues/new?{quote(create_issue_payload, safe='=')}%20-%20"
    return (linked_issues, linked_issues_url, create_issue_url)


def check_job_labels(job, job_labels):
    """Check and logging if job labels are not in the knonw label set_labels_list

    Parameters:
    -----------
    job : str
        The name of the job
    job_labels : list
        List of job labels

    Returns:
    --------
    """
    # If job has no label
    if job_labels is None:
        logging.info(' 🚫 🏷  Missing label(s) for job Job label: "%s"',
             job)
    # Check if job lable are weel knonw
    else:
        difference_labels = [label for label in job_labels if label not in set_labels_list]
        if difference_labels != []:
            logging.info(' ⚠️  🏷  Label(s) unknown: "%s"',difference_labels)


def create_job_doc(job):
    job_path = JOBS_DIR + "/" + job

    # Getting conf for indexing
    conf = get_conf(job_path)
    code_owner = conf.get("maintainer")
    license_name = conf.get("license")
    stage = conf.get("default_stage")

    if not code_owner or not license_name or not stage:
        logging.error("Job %s is missing fields (code_owner, license_name, stage) in '%s'", job, JOB_METADATA_FILE)
        sys.exit(1)

    index[stage]["content"].append(conf)

    # If job name starts with a dot, we must remove the dot for the file name,
    # else mkdocs will ignore it
    job_file = job
    if job.startswith('.'):
        job_file = job_file[1:]

    mkdocs_file_path = '{}/{}/{}/{}{}'.format(MKDOCS_DIR,
                                              JOBS_DIR,
                                              stage,
                                              job_file,
                                              MARKDOWN_EXTENSION)

    # Get variables for jinja
    description = get_description(job_path)
    latest, changelogs = get_changelogs(job_path, job)
    screenshot_path, screenshots_files = get_screenshots(job_path, job)
    license_content = get_license(license_name, code_owner)
    user = get_user(code_owner)
    job_raw_content = get_job_raw_content(job)
    job_icon = conf.get("icon")
    job_labels = conf.get("labels")
    linked_issues, linked_issues_url, create_issue_url = get_linked_issues(job)

    # Check job labels_list
    check_job_labels(job,job_labels)

    # Write final file
    logging.info('Build of documentation file for job "%s" in stage "%s"',
                 job,
                 stage)
    try:
        with open(mkdocs_file_path, 'w+') as doc_file:
            env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR))
            template = env.get_template(TEMPLATE_DOC)
            doc_file.write(template.render(
                job_name = job,
                job_icon = job_icon,
                readme = description,
                license_name = license_name,
                license = license_content,
                latest = latest,
                changelogs = changelogs,
                gitlab_image = user["avatar_url"],
                code_owner_name = user["name"],
                code_owner = code_owner,
                code_owner_url = user["web_url"],
                screenshot_path = screenshot_path,
                screenshots_files = screenshots_files,
                job_raw_content = ''.join(job_raw_content),
                job_labels = job_labels,
                linked_issues = linked_issues,
                linked_issues_limit = ISSUES_LIMIT,
                linked_issues_url = linked_issues_url,
                create_issue_url = create_issue_url
        ))
    except Exception as error:
        logging.error("Failed to create final file for job %s", job)
        logging.error(error)
        sys.exit(1)

def add_placeholder():
    # Verify that there is a .md file for every stage, or mkdocs will break
    for stage_key, _ in index.items():
        placeholder_path = MKDOCS_DIR + "/" + JOBS_DIR + "/" + stage_key
        if len(listdir(placeholder_path)) == 1:
            # There is only the .pages file, so mkdocs will break
            with open(placeholder_path + "/" + MKDOCS_PLACEHOLDER_FILE, "w+") as file_handle:
                env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR))
                template = env.get_template(TEMPLATE_PLACEHOLDER)
                file_handle.write(template.render())


def main():
    """
    Main function
    """

    # logging
    logging.basicConfig(level=logging.INFO)

    # Iterate over every directories in jobs directory to create their job.md for the documentation
    jobs = listdir(JOBS_DIR)
    for job in jobs:
        create_job_doc(job)

    # Verify that there is a .md file for every stage, or mkdocs will break
    add_placeholder()

    # Using jinja2 with a template to create the index
    env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_INDEX)
    index_content = template.render(index=index)

    with open(MKDOCS_DIR + "/" + JOBS_DIR + "/" + INDEX_FILE, "w+") as index_file:
        index_file.write(index_content)

if __name__ == "__main__":
    main()
