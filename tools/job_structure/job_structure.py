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


def get_conf(job_path):
    """Parse the YAML config of the job

    Args:
        job_path (string): Path to job.yml

    Returns:
        (dict): Object of parsed YAML
    """
    try:
        with open(job_path + "/" + utils.JOB_YAML) as conf_file:
            return full_load(conf_file)
    except YAMLError as error:
        logging.error("Failed to parse job config '%s/%s", job_path,
                      utils.JOB_YAML)
        logging.error(error)
        sys.exit(1)
    except OSError as error:
        logging.error("Failed to open and read job config '%s/%s",
                      job_path, utils.JOB_YAML)
        logging.error(error)
        sys.exit(1)


def check_job_labels(job):
    """Check and logging if job labels are not in the knonw label set_labels_list

    Parameters:
    -----------
    job : str
        The name of the job
    Returns:
    --------
    """

    ret = utils.EXIT_SUCCESS
    # Getting conf for indexing
    conf = get_conf(utils.JOBS_DIR + "/" + job)
    job_labels = conf.get("labels")

    # If job has no label
    if job_labels is None:
        logging.warning(' 🚫 🏷  Missing label(s) for job Job label: "%s"',
                        job)
    # Check if job lable are weel knonw
    else:
        difference_labels = [label for label in job_labels if label not in set_labels_list]
        if difference_labels != []:
            logging.warning(' ⚠️  🏷  Label(s) unknown: "%s"', difference_labels)


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
    ret = utils.EXIT_SUCCESS

    with open(f"{utils.TOOLS_DIR}/{utils.JOB_TEMPLATE_DIR}/{utils.JOB_DIR}/{utils.JOB_YAML}",
              "r") as template_yml, open(f"{utils.JOBS_DIR}/{job}/{utils.JOB_YAML}", "r") \
            as job_yml:
        template_content = yaml.load(template_yml, Loader=yaml.FullLoader)
        job_content = yaml.load(job_yml, Loader=yaml.FullLoader)

        logging.info("Checking the content of %s in job %s", utils.JOB_YAML, job)
        diff = set(template_content.keys()) - set(job_content.keys())
        if len(diff) > 0:
            for item in diff:
                logging.error("Key %s in %s of job %s is missing", item, utils.JOB_YAML, job)
            ret = utils.EXIT_FAILURE
        else:
            logging.info("%s for job %s is complete", utils.JOB_YAML, job)
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
        elif check_job_yaml(job) != utils.EXIT_SUCCESS:
            ret = utils.EXIT_FAILURE
        check_job_labels(job)
    sys.exit(ret)
