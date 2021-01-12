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

from os import getenv, listdir
from yaml import full_load
from jinja2 import Environment, FileSystemLoader
import requests
from urllib.parse import quote, urlencode
from datetime import datetime
from distutils.version import LooseVersion

# Job variables
JOBS_DIR = "jobs"
MKDOCS_DIR = "docs"
MKDOCS_PLACEHOLDER_FILE = "placeholder.md"
JOB_CHANGELOG_DIR = "versions"
JOB_DESCRIPTION_FILE = "README.md"
JOB_METADATA_FILE = "job.yml"
ISSUES_LIMIT = 5

# Requests variable
GITLAB_BASE_URL = "https://gitlab.com/"
GITLAB_API_URL = "https://gitlab.com/api/v4/"
R2DEVOPS_URL = "https://jobs.r2devops.io/"
JOB_TOKEN = getenv("API_TOKEN")
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


def get_user(code_owner):
    url = GITLAB_API_URL + "users?username=" + code_owner

    response = requests.request("GET", url)

    if response.status_code == 200:
        return response.json()[0]
    return None

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
    list
        A list of issues linked to the job with their name and url
    str
        Url to list the issues related to the job
    str
        Url to create a new issue for the job
    """
    linked_issues = []
    headers = {
        'PRIVATE-TOKEN': JOB_TOKEN
    }
    base_url = f"{GITLAB_API_URL}/projects/{quote(PROJECT_NAME, safe='')}/issues"
    url = f"{base_url}?labels={JOBS_SCOPE_LABEL}{job_name}"
    if opened:
        url += "&state=opened"
    r = requests.get(url, headers=headers)

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
    create_issue_payload = {
        "new": f"issue[title]=[job][{job_name}]"
    }
    create_issue_url = f"{issues_base_url}/issues?{urlencode(create_issue_payload)}%20-%20"
    return (linked_issues, linked_issues_url, create_issue_url)

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
    license_content = get_license(license_name, code_owner)
    user = get_user(code_owner)
    linked_issues, linked_issues_url, create_issue_url = get_linked_issues(job)

    # Write final file
    with open(mkdocs_file_path, 'w+') as doc_file:
        env = Environment(loader=FileSystemLoader(BUILDER_DIR + "/" + TEMPLATE_DIR))
        template = env.get_template(TEMPLATE_DOC)
        doc_file.write(template.render(
            job_name = job,
            readme = description,
            license_name = license_name,
            license = license_content,
            latest = latest,
            changelogs = changelogs,
            gitlab_image = user["avatar_url"],
            code_owner_name = user["name"],
            code_owner = code_owner,
            code_owner_url = user["web_url"],
            linked_issues = linked_issues,
            linked_issues_limit = ISSUES_LIMIT,
            linked_issues_url = linked_issues_url,
            create_issue_url = create_issue_url
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
