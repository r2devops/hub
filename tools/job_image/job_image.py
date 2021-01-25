#!/usr/bin/env python3

import os
import sys
import logging
import yaml
import argparse

# Job variables
JOBS_DIR = "jobs"
JOBS_EXTENSION = "yml"
LOGFILE_NAME = os.getenv("JOB_LOGFILE")
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def argparse_setup():
    """Setup argparse

    Return
    ------
    obj
        Python object with arguments parsed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("job", help="job name to get the image from")
    return parser.parse_args()

if __name__ == "__main__":
    """Main function, get the name of the image for a job

    Parameters
    ----------
    str
        Job name as argument of the script

    Return
    ------
    0
        If we were able to print that name
    1
        On error
    """
    # Setup argparse
    args = argparse_setup()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOGFILE_NAME),
            logging.StreamHandler(sys.stderr)
        ]
    )

    if args.job is None:
        logging.error(f"No argument provided")
        exit(EXIT_FAILURE)
    logging.info(f"Getting the image for job {args.job}")
    with open(f"{JOBS_DIR}/{args.job}/{args.job}.{JOBS_EXTENSION}", 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        if "image" in data[args.job].keys():
            if isinstance(data[args.job]['image'], dict):
                print(data[args.job]['image']['name'])
            else:
                print(data[args.job]['image'])
        elif "extends" in data[args.job].keys():
            if isinstance(data[data[args.job]['extends']]['image'], dict):
                print(data[data[args.job]['extends']]['image']['name'])
            else:
                print(data[data[args.job]['extends']]['image'])