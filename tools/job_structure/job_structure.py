#!/usr/bin/env python3

import os
import logging
import sys
import yaml

# Job variables
JOBS_DIR = "jobs"
TOOLS_DIR = "tools"
JOB_TEMPLATE_DIR = "job_template"
JOB_DIR = "job_name"
JOB_YAML = "job.yml"
LOGFILE_NAME = os.getenv("JOB_LOGFILE")
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def check_job_yaml(job):
    """Verify the content of job.yaml for every job

    Parameters
    ----------
    job
        Name of the job

    Returns
    -------
    0
        On success
    1
        If at least one key is missing
    """
    ret = EXIT_SUCCESS

    with open(f"{TOOLS_DIR}/{JOB_TEMPLATE_DIR}/{JOB_DIR}/{JOB_YAML}", "r") as template_yml, open(f"{JOBS_DIR}/{job}/{JOB_YAML}", "r") as job_yml:
        template_content = yaml.load(template_yml, Loader=yaml.FullLoader)
        job_content = yaml.load(job_yml, Loader=yaml.FullLoader)

        logging.info("Checking the content of %s in job %s", JOB_YAML, job)
        diff = set(template_content.keys()) - set(job_content.keys())
        if len(diff) > 0:
            for item in diff:
                logging.error("Key %s in %s of job %s is missing", item, JOB_YAML, job)
            ret = EXIT_FAILURE
        else:
            logging.info("%s for job %s is complete", JOB_YAML, job)
    return ret

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

    # Change "job_name" in template for the actual job name for comparison
    template_structure_tmp = [obj.replace("job_name", f"{job}") for obj in template_structure]

    job_structure = [os.path.join(parent, name) for (parent, subdirs, files) in os.walk(f"{JOBS_DIR}/{job}") for name in files + subdirs]
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

    ret = EXIT_SUCCESS
    if len(set(template_structure_tmp).intersection(job_structure)) != len(template_structure_tmp):
        # Not every file and directories in template_structure_tmp matched the job structure
        logging.error("Job structure of %s does not match the template:", job)
        for item in set(template_structure_tmp) - set(template_structure_tmp).intersection(job_structure):
            logging.error("\tFile/directory missing: %s", item)
        ret = EXIT_FAILURE
    else:
        logging.info("Job structure of %s matches the template", job)
    return ret


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

    # Iterate over every directories in jobs directory to create their job.md for the documentation
    jobs = os.listdir(JOBS_DIR)
    template_structure = [os.path.join(parent, name) for (parent, subdirs, files) in os.walk(f"{TOOLS_DIR}/{JOB_TEMPLATE_DIR}") for name in files + subdirs]
    # Clear the first 2 directories
    template_structure = [obj[obj.find('/') + 1:] for obj in template_structure]
    template_structure = [obj[obj.find('/') + 1:] for obj in template_structure]

    ret = EXIT_SUCCESS
    for job in jobs:
        if check_directory_structure(template_structure, job) != EXIT_SUCCESS:
            ret = EXIT_FAILURE
        elif check_job_yaml(job) != EXIT_SUCCESS:
            ret = EXIT_FAILURE
    sys.exit(ret)
