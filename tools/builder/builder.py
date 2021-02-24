#!/usr/bin/env python3

# This script is used to build the documentation that
# r2devops.io will be using for every job added to the hub

# Directory skeleton for a job:
# ── jobs
#     └── <job_name>
#         ├── <job_name>.yml
#         ├── job.yml
#         ├── README.md
#         ├── screenshots
#             ├── <screen_name>
#             └──...
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
import argparse

# Import the config module
from tools.utils.utils import Config
utils = Config()


def get_conf(job_path):
    """Parse the YAML config of the job

    Args:
        job_path (string): Path to job.yml

    Returns:
        (dict): Object of parsed YAML
    """
    logging.info("Parsing conf file")
    try:
        with open(job_path + "/" + utils.JOB_METADATA_FILE) as conf_file:
            return full_load(conf_file)
    except YAMLError as error:
        logging.error("Failed to parse job config '%s/%s", job_path,
                      utils.JOB_METADATA_FILE )
        logging.error(error)
        sys.exit(1)
    except OSError as error:
        logging.error("Failed to open and read job config '%s/%s",
                      job_path, utils.JOB_METADATA_FILE )
        logging.error(error)
        sys.exit(1)

def get_description(job_path):
    """Fetch the README file from job

    Args:
        job_path (string): Path the job folder

    Returns:
        (string): Full README file
    """
    logging.info("Parsing readme for job %s", job_path)
    try:
        with open(job_path + "/" + utils.JOB_DESCRIPTION_FILE) as readme_file:
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
    versions = listdir(job_path + "/" + utils.JOB_CHANGELOG_DIR)
    versions = [version[:-3] for version in versions]
    versions = sorted(versions, key=LooseVersion, reverse=True)
    latest = {
      "version": versions[0],
      "url": utils.R2DEVOPS_URL + job_name + utils.JOBS_EXTENSION
    }
    changelogs = []
    logging.info("Parsing changelogs for job %s", job_name)
    try:
        for version in versions:
            with open(job_path + "/" + utils.JOB_CHANGELOG_DIR + "/" + version + utils.MARKDOWN_EXTENSION) as changelog_file:
                changelogs.append({
                    "version": version,
                    "url": utils.R2DEVOPS_URL + version + "/" + job_name + utils.JOBS_EXTENSION,
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
    logging.info("Getting licence %s", license_name)
    try:
        env = Environment(loader=FileSystemLoader(utils.BUILDER_DIR + "/" + utils.TEMPLATE_DIR + "/" + utils.TEMPLATE_LICENSE_DIR))
        template = env.get_template(license_name + utils.MARKDOWN_EXTENSION + ".j2")
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

    logging.info("Getting screenshots for job %s", job_name)
    # Create screenshots folder in docs for the job
    makedirs(utils.MKDOCS_DIR+"/"+utils.MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+utils.SCREENSHOTS_DIR,0o777,True)

    # Get all screenshots of the job
    regex = re.compile('(.png|.jpg|.jpeg)$')
    screenshot_list = listdir(job_path + "/" + utils.SCREENSHOTS_DIR)
    screenshot_list = list(filter(regex.search, screenshot_list))

    # Copy all screenshot of the job into screenshots folder for the doc
    for screenshot in screenshot_list:
        copyfile(job_path + "/" + utils.SCREENSHOTS_DIR+"/"+screenshot, utils.MKDOCS_DIR+ "/"+ utils.MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+utils.SCREENSHOTS_DIR+"/"+screenshot)

    return ("/" + utils.MKDOCS_DIR_JOBS_IMAGES+"/"+job_name+"/"+utils.SCREENSHOTS_DIR, screenshot_list)

def get_user(code_owner):
    """Fetch the job maintainer Gitlab user

    Args:
        code_owner (string): gitlab name of the job maitainer

    Returns:
        (dict): user data
    """
    url = utils.GITLAB_API_URL + "users?username=" + code_owner

    response = requests.request("GET", url)

    logging.info("Getting user link for %s", code_owner)
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
    logging.info("Parsing content of the job %s", job_name)
    try:
        with open("{}/{job}/{job}{}".format(utils.JOBS_DIR, utils.JOBS_EXTENSION,
                                            job=job_name), 'r') as job:
            return job.readlines()
    except FileNotFoundError :
        logging.error("File %s/%s/%s.%s not found", utils.JOBS_DIR,
                                                    job_name,
                                                    job_name,
                                                    utils.JOBS_EXTENSION)
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
    logging.info(f"Getting list of linked issues for job %s", job_name)
    linked_issues = []
    base_url = f"{utils.GITLAB_API_URL}/projects/{quote(utils.PROJECT_NAME, safe='')}/issues"
    url = f"{base_url}?labels={utils.JOBS_SCOPE_LABEL}{job_name}"
    if opened:
        url += "&state=opened"
    r = requests.get(url)

    for issue in r.json():
        linked_issues.append({
            "name": issue['title'],
            "url": issue['web_url'],
            "iid": issue['iid']
        })
    issues_base_url = f"{utils.GITLAB_BASE_URL}/{utils.PROJECT_NAME}"
    linked_issues_payload = {
        "label_name": f"{utils.JOBS_SCOPE_LABEL}{job_name}"
    }
    linked_issues_url = f"{issues_base_url}/issues?{urlencode(linked_issues_payload)}"
    create_issue_payload = f"issue[title]=[job][{job_name}]"
    create_issue_url = f"{issues_base_url}/issues/new?{quote(create_issue_payload, safe='=')}%20-%20"
    return (linked_issues, linked_issues_url, create_issue_url)

def create_job_doc(job):
    """Create the Markdown documentation file for a job

    Parameters:
    -----------
    job : str
        The name of the job

    Returns:
    --------
    nothing
    """
    job_path = utils.JOBS_DIR + "/" + job

    # Getting conf for indexing
    conf = get_conf(job_path)
    code_owner = conf.get("maintainer")
    license_name = conf.get("license")
    stage = conf.get("default_stage")

    if not code_owner or not license_name or not stage:
        logging.error("Job %s is missing fields (code_owner, license_name, stage) in '%s'", job, utils.JOB_METADATA_FILE)
        sys.exit(1)

    utils.INDEX[stage]["content"].append(conf)

    # If job name starts with a dot, we must remove the dot for the file name,
    # else mkdocs will ignore it
    job_file = job
    if job.startswith('.'):
        job_file = job_file[1:]

    mkdocs_file_path = '{}/{}/{}/{}{}'.format(utils.MKDOCS_DIR,
                                              utils.JOBS_DIR,
                                              stage,
                                              job_file,
                                              utils.MARKDOWN_EXTENSION)

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

    # Write final file
    logging.info('Build of documentation file for job "%s" in stage "%s"',
                 job,
                 stage)

    try:
        with open(mkdocs_file_path, 'w+') as doc_file:
            env = Environment(loader=FileSystemLoader(utils.BUILDER_DIR + "/" + utils.TEMPLATE_DIR))
            template = env.get_template(utils.TEMPLATE_DOC)
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
                linked_issues_limit = utils.ISSUES_LIMIT,
                linked_issues_url = linked_issues_url,
                create_issue_url = create_issue_url
        ))
    except Exception as error:
        logging.error("Failed to create final file for job %s", job)
        logging.error(error)
        sys.exit(1)


def create_pages_placeholder(placeholder_path,stage_key):
    """ Create jobs folder destination folder in docs for the job and .pages fil

    Parameters:
    -----------
    placeholder_path : str
        Path to the stage documentation
    stage_key : boolean
        Name of the stage

    Returns:
    --------
    """
    # Create jobs folder destination folder in docs for the job
    makedirs(placeholder_path,0o777,True)
    # Create the .pages files mandatory to serve documentaiton and display stages
    f = open(placeholder_path + "/.pages", "w+")
    f.write("title: '"+ stage_key +"'")
    f.close()


def add_placeholder():
    """Add a placeholder file for every stage, in case a stage have no job

    Parameters:
    -----------
    nothing

    Return:
    -------
    nothing
    """
    for stage_key, _ in utils.INDEX.items():
        placeholder_path = utils.MKDOCS_DIR + "/" + utils.JOBS_DIR + "/" + stage_key
        if len(listdir(placeholder_path)) == 1:
            # There is only the .pages file, so mkdocs will break
            logging.info("Creating a placeholder file for the stage %s", stage_key)
            with open(placeholder_path + "/" + utils.MKDOCS_PLACEHOLDER_FILE, "w+") as file_handle:
                env = Environment(loader=FileSystemLoader(utils.BUILDER_DIR + "/" + utils.TEMPLATE_DIR))
                template = env.get_template(utils.TEMPLATE_PLACEHOLDER)
                file_handle.write(template.render())

def create_arrange_pages():
    """ Create arrange .pages for mkdocs to sort the list of stage in job page

    Parameters:
    -----------

    Returns:
    --------
    """
    stages = sorted(utils.INDEX.items(), key=lambda x: x[1]['order'])
    try:
        with open(utils.ARRANGE_PAGES_FILE_PATH, 'w+') as doc_file:
            env = Environment(loader=FileSystemLoader(utils.BUILDER_DIR + "/" + utils.TEMPLATE_DIR))
            template = env.get_template(utils.TEMPLATE_ARRANGE_PAGES)
            doc_file.write(template.render(
                title = utils.TITLE_ARRANGE_PAGES,
                stages = stages
        ))
    except Exception as error:
        logging.error("Failed to create arrange pages file for job %s", doc_file_path)
        logging.error(error)
        sys.exit(1)

def argparse_setup():
    """Setup argparse

    Return
    ------
    obj
        Python object with arguments parsed
    """
    parser = argparse.ArgumentParser()
    return parser.parse_args()

def main():
    """
    Main function, multiple-purpose:
    - Setup logging
    - Iterate over jobs to create their documentation
    - Add placeholders in stages that don't have a job
    - Create jobs index
    """

    # Setup argparse
    args = argparse_setup()
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(utils.LOGFILE_NAME),
            logging.StreamHandler()
        ]
    )

    # Iterate over every directories in jobs directory to create their job.md for the documentation
    jobs = listdir(utils.JOBS_DIR)
    for job in jobs:
        create_job_doc(job)

    # Verify that there is a .md file for every stage, or mkdocs will break
    add_placeholder()

    create_arrange_pages()

    # Using jinja2 with a template to create the index
    logging.info("Creating index of jobs")
    env = Environment(loader=FileSystemLoader(utils.BUILDER_DIR + "/" + utils.TEMPLATE_DIR))
    template = env.get_template(utils.TEMPLATE_INDEX)
    index_content = template.render(index=utils.INDEX)




    with open(utils.MKDOCS_DIR + "/" + utils.JOBS_DIR + "/" + utils.INDEX_FILE, "w+") as index_file:
        index_file.write(index_content)

if __name__ == "__main__":
    main()
