#!/usr/bin/env python3

import os
import sys
import logging
import re
import yaml
import argparse

# Import the Config module and set the path to run the script from root project
# /!\ This instruction is only working if you run this script from the root of the project
sys.path.insert(0, "./")
from tools.utils.utils import Config

utils = Config()

IMAGE_TAG_REGEX = "\${([a-zA-Z_-]+)}"


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


def get_image(job):
    """Get the image of a job

    Parameters
    ----------
    job
        Job name

    Return
    ------
    str
        The string of the image of the job, or empty
    """
    logging.info(f"Getting the image for job {job}")

    with open(f"{utils.JOBS_DIR}/{job}/{job}.yml", 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        if "image" in data[job].keys():
            if isinstance(data[job]['image'], dict):
                return data[job]['image']['name']
            else:
                return data[job]['image']
        elif "extends" in data[job].keys():
            if isinstance(data[data[job]['extends']]['image'], dict):
                return data[data[job]['extends']]['image']['name']
            else:
                return data[data[job]['extends']]['image']


def print_or_replace(image, variables):
    """ Check whether the image tag given is composed of environment variable
    If it's the case, it will fetch the default value from variables in CI

    Finally, it will print the sanitized image tag in stdout

    :param image: Image tag to check (python:1.0.0 or python:${IMAGE_VERSION})
    :param variables: The list of variables that are available in the job

    :return It returns nothing
    """

    match_pattern = re.search(IMAGE_TAG_REGEX, image)

    if match_pattern is None:
        # If image tag / name is raw without env var, we print it & end the function
        print(image)
        return

    # We can assume pattern group is fulfilled as match_pattern isn't None
    env_var_name = match_pattern.groups()[0]
    env_var_value = variables[env_var_name]

    if env_var_value is None:
        print("Environment variable for {} is not available in variables {}", image, variables)
        sys.exit(1)

    image = re.sub(IMAGE_TAG_REGEX, env_var_value, image)
    print(image)


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

    job_data = data[args.job]

    # If image option is directly specified in the job
    if "image" in data[args.job].keys():
        if isinstance(data[args.job]['image'], dict):
            print_or_replace(job_data['image']['name'], job_data["variables"])
        else:
            print_or_replace(job_data['image'], job_data['variables'])

    # If image isn't specified in the job but extends is
    elif "extends" in data[args.job].keys():

        try:
            if isinstance(data[data[args.job]['extends']]['image'], dict):
                print_or_replace(data[data[args.job]['extends']]['image']['name'], job_data['variables'])
            else:
                print_or_replace(data[data[args.job]['extends']]['image'], job_data['variables'])
        # If the extended job isn't in the file, it produce a KeyError
        except KeyError:
            logging.warning(
                'The job %s doesn\'t declare its image and extends a job from outside of the file, we aren\'t able to check its image vulnerabilities',
                args.job)
            # TODO: check images from included jobs ==> https://gitlab.com/r2devops/hub/-/issues/282
