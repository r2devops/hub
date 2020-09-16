#!/usr/bin/env python3

# This script is used to build the documentation that hub.go2scale.com will be using for every job added to the hub

# Directory skeleton for a job:
# ── jobs
#     └── <job_name>
#         ├── <job_name>.yml
#         ├── LICENSE
#         ├── README.md
#         └── versions
#             ├── 0.0.1.md
#             ├── 0.0.2.md
#             └──...

from pathlib import Path
from os import listdir
from yaml import full_load
from jinja2 import Environment, FileSystemLoader

# Job variables
jobs_dir = "jobs"
mkdocs_dir = "docs"
job_changelog_dir = "versions"
job_description_file = "README.md"
job_license_file = "LICENSE"
job_metadata_file = "metadata.yml"

mk_changelog_wrapper = "\n## Changelog\n\n* **[latest]**(current -> `<LATEST_RELEASE>`) : `<TAG_URL>`\n"
mk_license_wrapper = "??? License\n"

mkdocs_job_content = ""

# Index variables
builder_dir = "builder"
template_dir = "templates"
template_name = "index.md.j2"
index_file = "index.md"
index = {"static_tests": [], "build": [], "dynamic_tests": [], "review": [], "deployment": []}

def get_conf(job_path, job_name):
  # Load yaml file
  with open(job_path + "/" + job_metadata_file + ".yml") as file:
    return full_load(file)

def add_description(job_path, job_name):
  # Concatenate description to final file
  global mkdocs_job_content
  
  with open(job_path + "/" + job_description_file) as file:
    mkdocs_job_content += file.read()

def add_changelog(job_path, job_name):
  # Concatenate changelog to final file
  global mkdocs_job_content
  
  mkdocs_job_content += mk_changelog_wrapper

  # For now, we are just getting the latest release, but we will be adding a full link to the release later
  latest_release = listdir(job_path + "/" + job_changelog_dir)[-1][0:-3]
  mkdocs_job_content = mkdocs_job_content.replace("<LATEST_RELEASE>", latest_release)

  for release in listdir(job_path + "/" + job_changelog_dir)[::-1]:
    with open(job_path + "/" + job_changelog_dir + "/" + release) as file:
      mkdocs_job_content += file.read()
      # TODO replace <include tag by the link to the release
  # Adding a new line for consistency
  mkdocs_job_content += "\n"

def add_license(job_path, job_name):
  # Concatenate license to final file
  global mkdocs_job_content

  mkdocs_job_content += mk_license_wrapper
  with open(job_path + "/" + job_license_file) as file:
    for line in file.readlines():
      mkdocs_job_content += "    " + line

def create_job_doc(job):
  job_path = jobs_dir + "/" + job

  # Getting conf for indexing  
  conf = get_conf(job_path, job)
  index[conf["default_stage"]].append(conf)

  mkdocs_file_path = mkdocs_dir + "/" + jobs_dir + "/" + conf["default_stage"] + "/" + job + ".md"

  add_description(job_path, job)
  add_changelog(job_path, job)
  add_license(job_path, job)
  
  # Write final file
  with open(mkdocs_file_path, 'w+') as file:
    file.write(mkdocs_job_content)

if __name__ == "__main__":
  # Iterate over every directories in jobs directory to create their job.md for the documentation
  ### TO EDIT
  # for job in listdir(jobs_dir):
  for job in ["python_test", "trivy_image"]:
  ###
    create_job_doc(job)

  # Using jinja2 with a template to create the index
  env = Environment(loader=FileSystemLoader(builder_dir + "/" + 'templates'))
  template = env.get_template(template_name)
  index_content = template.render(index=index)

  with open(mkdocs_dir + "/" + index_file, "w+") as file:
    file.write(index_content)
