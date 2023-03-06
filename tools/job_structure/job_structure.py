#!/usr/bin/env python3

import os
import logging
import sys
import yaml
from yaml import full_load, YAMLError

# Import the Config module and set the path to run the script from root project
# /!\ This instruction is only working if you run this script from the root of the project
sys.path.insert(0, "./")
from tools.utils.utils import Config

utils = Config()

# List of available labels for jobs
labels_list = ["GitLab", "Build", "Container", "Docker", "PHP", "Testing", "Utilities",
               "Yarn", "Dependency scan", "Security", "Python", "API", "Documentation",
               "Quality", "SAST", "Linter", "Helm", "DAST", "Kubernetes",
               "NPM"]
# A list of paths where the file / directory is considered as not mandatory
optional_paths=["r2_jobname/screenshots", "r2_jobname/screenshots/.gitkeep"]
set_labels_list = set(labels_list)



def check_directory_structure(template_structure, job):
    """Verify every file and directories in template to be sure they are present in the job

    Parameters
    ----------
    template_structure
        Structure of the template
    job
        Name of the job

    Returns
    -------
    0
        On success
    1
        If at least a file/directory is missing
    """

    # Change "r2_jobname" in template for the actual job name for comparison
    template_structure_tmp = set(template_structure).symmetric_difference(optional_paths)
    template_structure_tmp = [obj.replace("r2_jobname", f"{job}") for obj in template_structure_tmp]

    job_structure = [os.path.join(parent, name) for (parent, subdirs, files)
                     in os.walk(f"{utils.JOBS_DIR}/{job}")
                     for name in files + subdirs]
    # Adding the job directory
    job_structure.append(f"{job}")

    # Clear the first directory
    job_structure = [obj[obj.find('/') + 1:] for obj in job_structure]

    # Check if file/directory is empty
    logging.info("Checking empty file/directory in job structure of job %s", job)
    for item in job_structure:
        if os.path.isfile(item):
            if os.path.getsize(item) == 0:
                logging.error("File %s for job %s is empty", item, job)
        elif os.path.isdir(item):
            if len(os.listdir(item)) == 0:
                logging.error("Directory %s for job %s is empty", item, job)

    ret = utils.EXIT_SUCCESS
    current_len = len(set(template_structure_tmp).intersection(job_structure))

    if current_len != len(template_structure_tmp):
        # Not every file and directories in template_structure_tmp matched the job structure
        logging.error("Job structure of %s does not match the template:", job)
        for item in set(template_structure_tmp) - set(template_structure_tmp).intersection(job_structure):
            logging.error("\tFile/directory missing: %s", item)
        ret = utils.EXIT_FAILURE
    else:
        logging.info("Job structure of %s matches the template", job)
    return ret


if __name__ == "__main__":
    """Main function, iterating over job structures to compare to the template one

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
            logging.FileHandler(utils.LOGFILE_NAME),
            logging.StreamHandler()
        ]
    )

    # Iterate over every directories in jobs directory to create their job.md for the documentation
    jobs = os.listdir(utils.JOBS_DIR)
    template_structure = [os.path.join(parent, name) for (parent, subdirs, files) in
                          os.walk(f"{utils.TOOLS_DIR}/{utils.JOB_TEMPLATE_DIR}") for name in files + subdirs]
    # Clear the first 2 directories
    template_structure = [obj[obj.find('/') + 1:] for obj in template_structure]
    template_structure = [obj[obj.find('/') + 1:] for obj in template_structure]

    ret = utils.EXIT_SUCCESS
    for job in jobs:
        if check_directory_structure(template_structure, job) != utils.EXIT_SUCCESS:
            ret = utils.EXIT_FAILURE
    sys.exit(ret)
