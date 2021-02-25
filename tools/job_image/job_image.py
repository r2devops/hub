#!/usr/bin/env python3

import os
import sys
import logging
import yaml
import argparse

# Import the Config module and set the path to run the script from root project
# /!\ This instruction is only working if you run this script from the root of the project
from tools.utils.utils import Config
sys.path.insert(0, "./")
utils = Config()

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
            logging.FileHandler(utils.LOGFILE_NAME),
            logging.StreamHandler(sys.stderr)
        ]
    )

    if args.job is None:
        logging.error("No argument provided")
        sys.exit(utils.EXIT_FAILURE)

    logging.info("Getting the image for job %s", args.job)

    data = {}
    with open(f"{utils.JOBS_DIR}/{args.job}/{args.job}{utils.JOBS_EXTENSION}", 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # If image option is directly specified in the job
    if "image" in data[args.job].keys():
        if isinstance(data[args.job]['image'], dict):
            print(data[args.job]['image']['name'])
        else:
            print(data[args.job]['image'])

    # If image isn't specified in the job but extends is
    elif "extends" in data[args.job].keys():

        try:
            if isinstance(data[data[args.job]['extends']]['image'], dict):
                print(data[data[args.job]['extends']]['image']['name'])
            else:
                print(data[data[args.job]['extends']]['image'])
        # If the extended job isn't in the file, it produce a KeyError
        except KeyError :
            logging.warning('The job %s doesn\'t declare its image and extends a job from outside of the file, we aren\'t able to check its image vulnerabilities', args.job)
            # TODO: check images from included jobs ==> https://gitlab.com/r2devops/hub/-/issues/282
