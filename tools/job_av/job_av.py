#!/usr/bin/env python3

import os
import logging
import json
import sys
import copy
import argparse
import yaml
from tools.job_image.job_image import get_image

# Import the Config module and set the path to run the script from root project
# /!\ This instruction is only working if you run this script from the root of the project
sys.path.insert(0, "./")
from tools.utils.utils import Config

utils = Config()

# Job variables
CI_FILENAME = os.getenv("GENERATED_YAML")
PARALLEL_LIMIT = 50

BASE_FILE = "base-gitlab-ci.yml"
JOB_DIR = "job_av"

SCANNED_IMAGES_FILE = os.getenv("SCANNED_IMAGES_FILE")
SCANNED_IMAGES = []

BLACKLIST = ["github/super-linter:v3.14.3", "shiftleft/sast-scan:v1.9.29", "oxsecurity/megalinter:v6.8.0", "github/super-linter:v4.9.0"]


def argparse_setup():
    """Setup argparse

    Return
    ------
    obj
        Python object with arguments parsed
    """
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def get_scanned_images():
    """Fetch already scanned images by
    the schedule pipeline

    :return: string[] with a list of scanned images
    """
    try:
        with open(SCANNED_IMAGES_FILE, "r") as images_file:
            scanned_image = json.load(images_file)
            logging.info("Scanned images list: %s", scanned_image)
            return scanned_image
    except OSError:
        logging.warning("There isn't any file containing already scanned images")
        with open(SCANNED_IMAGES_FILE, "w") as new_file:
            json.dump([], new_file)
            return []


def set_default_image(current_ci):
    """When there is no image to scan
    We replace the base-gitlab-ci.yml into a
    simple child pipeline job, saying "nothing to run"

    Based on test this "default job" lasts 20 seconds.
    """
    current_ci["job_av"]["script"] = []
    current_ci["job_av"]["script"].append("echo 'There is not any image to scan, finishing...'")

    current_ci["job_av"].pop("services")
    current_ci["job_av"].pop("artifacts")
    current_ci["job_av"].pop("cache")
    current_ci["job_av"].pop("parallel")
    current_ci["job_av"]["image"] = "alpine:3.13.2"

    logging.info("No image to scan, putting default useless child job")

def save_scanned_images(already_scanned):
    """Save the scanned images into
    needed file

    :param scanned_images: array with a list of image
    :return:
    """
    try:
        with open(SCANNED_IMAGES_FILE, 'w') as images_file:
            json.dump(already_scanned, images_file)

        logging.info("Saved successfully scanned images in this pipeline")
        logging.info("There is %s images now scanned", len(already_scanned))
    except OSError as error:
        logging.error("Failed to write new scanned images file %s", error)
        sys.exit(1)


if __name__ == "__main__":
    """Main function, iterate over the jobs to get their image
    and write a .gitlab-ci.yml that can run a child pipeline
    in order to use ClamAV for virus detection

    Returns
    -------
    0
        On success
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
            logging.StreamHandler()
        ]
    )

    logging.info("Getting all images from every job in the hub")
    jobs = os.listdir(utils.JOBS_DIR)
    scanned_images = get_scanned_images()
    images = [
    ]

    for job in jobs:
        image = get_image(job)
        logging.info("Checking %s image", image)
        if (image is not None and image not in images
            and image not in BLACKLIST and image not in scanned_images):
            logging.info("Adding %s image to list of images to scan", image)
            images.append(image)

    logging.info("There is %s images to scan in this pipeline", len(images))

    image_chunks = [images[x: x + PARALLEL_LIMIT] for x in range(0, len(images), PARALLEL_LIMIT)]
    save_scanned_images(images + scanned_images)

    ci_file = {}
    with open(f"{utils.TOOLS_DIR}/{JOB_DIR}/{BASE_FILE}") as file:
        ci_file = yaml.load(file, Loader=yaml.FullLoader)

    logging.info("Creating jobs for each chunks of %i images to run in parallel", PARALLEL_LIMIT)
    for chunk_index, chunk in enumerate(image_chunks):
        if chunk_index == 0:
            for image_index, image in enumerate(chunk):
                logging.info("Adding image %s to job n°%i", image, chunk_index)
                ci_file["job_av"]["parallel"]["matrix"][0]["IMAGE"].append(image)
        else:
            ci_file[f"job_av_{chunk_index}"] = copy.deepcopy(ci_file["job_av"])
            ci_file[f"job_av_{chunk_index}"]["parallel"]["matrix"][0]["IMAGE"] = []
            for image_index, image in enumerate(chunk):
                logging.info("Adding image %s to job n°%i", image, chunk_index)
                ci_file[f"job_av_{chunk_index}"]["parallel"]["matrix"][0]["IMAGE"].append(image)

    if not images:
        set_default_image(ci_file)

    logging.info("Writing %s file", CI_FILENAME)
    with open(CI_FILENAME, "w+") as file:
        yaml.dump(ci_file, file, sort_keys=False)
