#!/usr/bin/env python3

# This script is used to build the documentation that hub.go2scale.com will be using for every job added to the hub

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

from pathlib import Path
from os import listdir
from yaml import full_load
from jinja2 import Environment, FileSystemLoader
import requests

# Job variables
jobs_dir = "jobs"
mkdocs_dir = "docs"
mkdocs_placeholder_file = "placeholder.md"
job_changelog_dir = "versions"
job_description_file = "README.md"
job_license_file = "LICENSE"
job_metadata_file = "job.yml"

gitlab_api_url = "https://gitlab.com/api/v4/"

# Templates variables
builder_dir = "builder"
template_dir = "templates"
template_index = "index.md.j2"
template_doc = "job_documentation.md.j2"
template_placeholder = "placeholder.md.j2"
index_file = "index.md"
index = {
  "static_tests": [],
  "build": [],
  "dynamic_tests": [],
  "review": [],
  "deployment": []
}

def get_conf(job_path, job_name):
  # Load yaml file
  with open(job_path + "/" + job_metadata_file) as file:
    return full_load(file)

def get_description(job_path, job_name):
  # Concatenate description to final file
  with open(job_path + "/" + job_description_file) as file:
    return file.read()

def get_changelogs(job_path, job_name):
  changelogs = []

  latest_version = listdir(job_path + "/" + job_changelog_dir)[-1][0:-3]
  ### TODO add the url of the tag in here
  latest_url = "<TAG_URL>"
  version_url = "<TAG_URL>"
  ###

  latest = {
    "url": latest_url,
    "version": latest_version
  }

  for version in listdir(job_path + "/" + job_changelog_dir)[::-1]:
    with open(job_path + "/" + job_changelog_dir + "/" + version) as file:
      changelogs.append({
        "version": version[0:-3],
        "url": version_url,
        "changelog": file.read()
      })
  return (latest, changelogs)

def get_license(job_path, job_name):
  with open(job_path + "/" + job_license_file) as file:
    return file.readlines()

def get_user(job_path, job, code_owner):
  url = gitlab_api_url + "users?username=" + code_owner

  response = requests.request("GET", url)

  if response.status_code == 200:
    return response.json()[0]
  return None

def create_job_doc(job):
  job_path = jobs_dir + "/" + job

  # Getting conf for indexing  
  conf = get_conf(job_path, job)
  code_owner = conf.get("code-owner")
  index[conf["default_stage"]].append(conf)

  mkdocs_file_path = mkdocs_dir + "/" + jobs_dir + "/" + conf["default_stage"] + "/" + job + ".md"

  # Get variables for jinja
  description = get_description(job_path, job)
  latest, changelogs = get_changelogs(job_path, job)
  license = get_license(job_path, job)
  user = get_user(job_path, job, conf["code-owner"])

  ### TO REMOVE
  from pprint import pprint
  pprint(changelogs)
  ###

  # Write final file
  with open(mkdocs_file_path, 'w+') as file:
    env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
    template = env.get_template(template_doc)
    file.write(template.render(
      readme = description,
      license = license,
      latest = latest,
      changelogs = changelogs,
      gitlab_image = user["avatar_url"],
      code_owner_name = user["name"],
      code_owner = code_owner,
      code_owner_url = user["web_url"]
    ))

def add_placeholder():
  # Verify that there is a .md file for every stage, or mkdocs will break
  for stage in index.keys():
    if len(listdir(mkdocs_dir + "/" + jobs_dir + "/" + stage)) == 1:
      # There is only the .pages file, so mkdocs will break
      with open(mkdocs_dir + "/" + jobs_dir + "/" + stage + "/" + mkdocs_placeholder_file, "w+") as file:
        env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
        template = env.get_template(template_placeholder)
        file.write(template.render())
  
if __name__ == "__main__":
  # Iterate over every directories in jobs directory to create their job.md for the documentation
  jobs = listdir(jobs_dir)

  for job in jobs:
    create_job_doc(job)

  # Verify that there is a .md file for every stage, or mkdocs will break
  add_placeholder()

  # Using jinja2 with a template to create the index
  env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
  template = env.get_template(template_index)
  index_content = template.render(index=index)

  with open(mkdocs_dir + "/" + jobs_dir + "/" + index_file, "w+") as file:
    file.write(index_content)
