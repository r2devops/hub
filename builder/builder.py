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

# Index variables
builder_dir = "builder"
template_dir = "templates"
template_index = "index.md.j2"
template_changelog = "changelog.md.j2"
template_license = "license.md.j2"
template_placeholder = "placeholder.md.j2"
template_code_owner = "code_owner.md.j2"
index_file = "index.md"
index = {"static_tests": [], "build": [], "dynamic_tests": [], "review": [], "deployment": []}

def get_conf(job_path, job_name):
  # Load yaml file
  with open(job_path + "/" + job_metadata_file) as file:
    return full_load(file)

def add_description(job_path, job_name, mkdocs_job_content):
  # Concatenate description to final file
  with open(job_path + "/" + job_description_file) as file:
    mkdocs_job_content += file.read()
  return mkdocs_job_content

def add_changelog(job_path, job_name, mkdocs_job_content):
  # For now, we are just getting the latest release, but we will be adding a full link to the release later
  latest_release = listdir(job_path + "/" + job_changelog_dir)[-1][0:-3]
  env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
  template = env.get_template(template_changelog)
  mkdocs_job_content += template.render(latest_release=latest_release)

  for release in listdir(job_path + "/" + job_changelog_dir)[::-1]:
    with open(job_path + "/" + job_changelog_dir + "/" + release) as file:
      mkdocs_job_content += file.read()
      # TODO replace <TAG_URL> by the link to the release
  
  # Adding a new line for consistency
  mkdocs_job_content += "\n"
  return mkdocs_job_content

def add_license(job_path, job_name, mkdocs_job_content):
  env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
  template = env.get_template(template_license)
  mkdocs_job_content += template.render()

  # Concatenate license to final file
  with open(job_path + "/" + job_license_file) as file:
    for line in file.readlines():
      mkdocs_job_content += "    " + line
  return mkdocs_job_content

def add_code_owner(job_path, job, mkdocs_job_content, code_owner):
  url = gitlab_api_url + "users?username=" + code_owner

  response = requests.request("GET", url)

  if response.status_code == 200:
    user = response.json()[0]

    env = Environment(loader=FileSystemLoader(builder_dir + "/" + template_dir))
    template = env.get_template(template_code_owner)
    mkdocs_job_content += template.render(gitlab_image=user["avatar_url"], code_owner_name=user["name"], code_owner=code_owner, code_owner_url=user["web_url"])
  return mkdocs_job_content

def create_job_doc(job):
  job_path = jobs_dir + "/" + job
  mkdocs_job_content = ""

  # Getting conf for indexing  
  conf = get_conf(job_path, job)
  index[conf["default_stage"]].append(conf)

  mkdocs_file_path = mkdocs_dir + "/" + jobs_dir + "/" + conf["default_stage"] + "/" + job + ".md"

  mkdocs_job_content = add_description(job_path, job, mkdocs_job_content)
  mkdocs_job_content = add_changelog(job_path, job, mkdocs_job_content)
  mkdocs_job_content = add_license(job_path, job, mkdocs_job_content)
  code_owner = conf.get("code-owner")
  if code_owner:
    mkdocs_job_content = add_code_owner(job_path, job, mkdocs_job_content, conf["code-owner"])

  # Write final file
  with open(mkdocs_file_path, 'w+') as file:
    file.write(mkdocs_job_content)

def add_placeholder():
  # Verify that there is a .md file for every stage, or mkdocs will break
  stages = listdir(mkdocs_dir + "/" + jobs_dir)
  stages.remove(".pages")

  for stage in stages:
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
