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

from os import listdir, makedirs
from yaml import full_load
from jinja2 import Environment, FileSystemLoader
import requests
from datetime import datetime
from distutils.version import LooseVersion
from shutil import copyfile
import re


# Job variables
JOBS_DIR = "jobs"
MKDOCS_DIR = "docs"

MKDOCS_PLACEHOLDER_FILE = "placeholder.md"
JOB_CHANGELOG_DIR = "versions"

JOB_DESCRIPTION_FILE = "README.md"
JOB_METADATA_FILE = "job.yml"

# Path to images used for the built job documentation
MKDOCS_DIR_JOBS_IMAGES = "images/jobs"
# Directory name to use for the jobs screenshot
SCREENSHOTS_DIR = "screenshots"

GITLAB_API_URL = "https://gitlab.com/api/v4/"
R2DEVOPS_URL = "https://jobs.r2devops.io/"

# Templates variables
BUILDER_DIR = "tools/builder"
TEMPLATE_DIR = "templates"
TEMPLATE_INDEX = "index.md.j2"
TEMPLATE_DOC = "job_documentation.md.j2"
TEMPLATE_PLACEHOLDER = "placeholder.md.j2"
TEMPLATE_LICENSE_DIR = "licenses"
INDEX_FILE = "index.md"

index = {
    "static_tests": [],
    "build": [],
    "dynamic_tests": [],
    "review": [],
    "deployment": []
}

def get_conf(job_path):
    # Load yaml file
    with open(job_path + "/" + JOB_METADATA_FILE) as conf_file:
        return full_load(conf_file)

def get_description(job_path):
    # Concatenate description to final file
    with open(job_path + "/" + JOB_DESCRIPTION_FILE) as readme_file:
        return readme_file.read()

def get_changelogs(job_path, job_name):
    versions = listdir(job_path + "/" + JOB_CHANGELOG_DIR)
    versions = [version[:-3] for version in versions]
    versions = sorted(versions, key=LooseVersion, reverse=True)
    latest = {
      "version": versions[0],
      "url": R2DEVOPS_URL + job_name + ".yml"
    }
    changelogs = []
    for version in versions:
        with open(job_path + "/" + JOB_CHANGELOG_DIR + "/" + version + ".md") as changelog_file:
            changelogs.append({
                "version": version,
                "url": R2DEVOPS_URL + version + "/" + job_name + ".yml",
                "changelog": changelog_file.readlines()
            })
    return (latest, changelogs)

def get_license(license_name, copyright_holder):
    env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR + "/" + TEMPLATE_LICENSE_DIR))
    template = env.get_template(license_name + ".md.j2")
    license_content = template.render(
        year = datetime.now().year,
        copyright_holder = copyright_holder
    ).split('\n')
    license_content = [ line + '\n' for line in license_content]
    return license_content

def get_screenshots(job_path, job_name):
    """Create the job directory for the job documentation
       Gets the jobs screenshots and copy them to the documentation directory

    Parameters
    ----------
    job_path : str
        The job path
    job_name : str
        The job name (ex: Gitleaks)

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
    url = GITLAB_API_URL + "users?username=" + code_owner

    response = requests.request("GET", url)

    if response.status_code == 200:
        return response.json()[0]
    return None

def create_job_doc(job):
    job_path = JOBS_DIR + "/" + job

    # Getting conf for indexing
    conf = get_conf(job_path)
    code_owner = conf.get("maintainer")
    license_name = conf.get("license")
    index[conf["default_stage"]].append(conf)

    mkdocs_file_path = MKDOCS_DIR + "/" + JOBS_DIR + "/" + conf["default_stage"] + "/" + job + ".md"

    # Get variables for jinja
    description = get_description(job_path)
    latest, changelogs = get_changelogs(job_path, job)
    screenshot_path, screenshots_files = get_screenshots(job_path, job)
    license_content = get_license(license_name, code_owner)
    user = get_user(code_owner)

    # Write final file
    with open(mkdocs_file_path, 'w+') as doc_file:
        env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR))
        template = env.get_template(TEMPLATE_DOC)
        doc_file.write(template.render(
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
            screenshots_files = screenshots_files
    ))

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

if __name__ == "__main__":
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
