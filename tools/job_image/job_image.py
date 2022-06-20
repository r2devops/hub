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
        current_data = data[job]
        variables = {}

        if "variables" in current_data:
            variables = current_data["variables"]

        if "image" in data[job].keys():
            if isinstance(data[job]['image'], dict):
                image = current_data['image']['name']
                return raw_or_replace_tag(image, variables)
            else:
                image = current_data['image']
                return raw_or_replace_tag(image, variables)
        elif "extends" in data[job].keys():
            extension = data[current_data['extends']]
            #In case the extension has variable, we take in consideration for the parsing
            if "variables" in extension:
                variables.update(extension['variables'])

            if isinstance(data[data[job]['extends']]['image'], dict):
                image = data[current_data['extends']]['image']['name']
                return raw_or_replace_tag(image, variables)
            else:
                image = data[current_data['extends']]['image']
                return raw_or_replace_tag(image, variables)


def raw_or_replace_tag(image, variables):
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
        return image

    # We can assume pattern group is fulfilled as match_pattern isn't None
    env_var_name = match_pattern.groups()[0]
    env_var_value = None

    if env_var_name in variables:
        env_var_value = variables[env_var_name]

    if env_var_value is None:
        print("Environment variable for {} is not available in variables {}", image, variables)
        sys.exit(1)

    image = re.sub(IMAGE_TAG_REGEX, env_var_value, image)
    return image


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
    output_image = ""

    # If image option is directly specified in the job
    if "image" in data[args.job].keys():
        if isinstance(data[args.job]['image'], dict):
            output_image = raw_or_replace_tag(job_data['image']['name'], job_data["variables"])
        else:
            output_image = raw_or_replace_tag(job_data['image'], job_data['variables'])

    # If image isn't specified in the job but extends is
    elif "extends" in data[args.job].keys():
        variables = {}

        if "variables" in job_data:
            variables = job_data['variables']

        try:
            # if the job extends another one, we fetch the extension variables
            # and update them
            if isinstance(data[data[args.job]['extends']]['image'], dict):
                extension = data[data[args.job]['extends']]
                if "variables" in extension:
                    variables.update(extension['variables'])
                output_image = raw_or_replace_tag(extension['image']['name'],
                                                  variables)
            else:
                extension = data[data[args.job]['extends']]
                if "variables" in extension:
                    variables.update(extension['variables'])

                output_image = raw_or_replace_tag(data[data[args.job]['extends']]['image'], variables)
        # If the extended job isn't in the file, it produce a KeyError
        except KeyError:
            logging.warning(
                'The job %s doesn\'t declare its image and extends a job from outside of the file, we aren\'t able to check its image vulnerabilities',
                args.job)
            # TODO: check images from included jobs ==> https://gitlab.com/r2devops/hub/-/issues/282

    print(output_image)
