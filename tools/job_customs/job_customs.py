#!/usr/bin/env python3

import os
import logging
import sys
import yaml
import argparse
import re

# Job variables
JOBS_DIR = "jobs"
JOBS_EXTENSION = "yml"
LOGFILE_NAME = os.getenv("JOB_LOGFILE")
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

patterns = [
    "git commit",
    "git push"
]

scripts = [
    "before_script",
    "script",
    "after_script"
]

def argparse_setup():
    """Setup argparse

    Return
    ------
    obj
        Python object with arguments parsed
    """
    parser = argparse.ArgumentParser()
    return parser.parse_args()

if __name__ == "__main__":
    """Main function, verify if the script part of every job isn't modifying the code with patterns
    Return
    ------
    0
        If no code was modified during the script
    1
        If the code is modified during the script
    """

    # Setup argparse
    args = argparse_setup()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOGFILE_NAME),
            logging.StreamHandler()
        ]
    )

    return_code = EXIT_SUCCESS
    for job in os.listdir(JOBS_DIR):

        logging.info(f"Getting the script for job {job}")

        data = {}
        with open(f"{JOBS_DIR}/{job}/{job}.{JOBS_EXTENSION}", 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

        for script in scripts:

            try:
                if script in data[job].keys():
                    for line in data[job][script]:
                        if any(re.match(pattern, line) for pattern in patterns):
                            logging.error(f"Code modification discovered in script of job {job}")
                            return_code = EXIT_FAILURE
                elif "extends" in data[job].keys():
                    if script in data[data[job]['extends']].keys():
                        for line in data[data[job]['extends']][script]:
                            if any(re.match(pattern, line) for pattern in patterns):
                                logging.error(f"Code modification discovered in script of job {job}")
                                return_code = EXIT_FAILURE
            # If the extended job isn't in the file, it produce a KeyError
            except KeyError :
                logging.warning('The job %s extends a job not declared in the file, we aren\'t able to check what %s does',
                                job, script)
                # TODO: check images from included jobs ==> https://gitlab.com/r2devops/hub/-/issues/282

    sys.exit(return_code)
