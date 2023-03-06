#!/usr/bin/env python3
""" Generating a discord release notification for a job

.. moduleauthor:: Alexandre Burgoni <alexandre@go2scale.com>

"""

import sys
import os
import random
import argparse
import logging
import requests
import yaml

ROOT_DIR = os.getenv("CI_PROJECT_DIR", "../")
QUOTES_URL = "https://gitlab.com/r2devops/hub/-/snippets/2046463/raw/master/snippetfile1.txt" # Link to snippet
AVATAR_URL = "https://go2scale.io/wp-content/uploads/2021/08/R2_Plan-de-travail-1-05.png" # Avatar of the author showed in the footer also
USERNAME = "R2" # Message's author
EMBED_COLOR = 1127128 # Trailing color at left of message
EMBED_TITLE = "A new job version is available for " # Title of the message
EMBED_DESCRIPTION = "Wanna see what's new ? :point_down:" # Content of the message (body)
DOC_LINK = "https://r2devops.io/_/gitlab/r2devops/hub"
API_JOBS_LINK = "https://api.r2devops.io/job/gitlab/r2devops/hub"
IGNORE_QUERY_PARAM = "ignore=true"

def get_random_quote():
    """Retrieve a random quote from R2Devops Snippet

    Returns:
        str: A quote from R2
    """
    with requests.get(QUOTES_URL) as response:
        data = response.json()
        return random.choice(data)

def generate_data(name: str, version: str, changelog: str):
    """Generate the body of the request

    Args:
        name (str): Name of the job
        version (str): Version of the job
        changelog (str): Changelog of the job
    Returns:
        object: Describe the format and content of discord notification
    """

    logging.debug("generateData(%s, %s)", name, version)

    job_path = "{0}/jobs/{1}/{1}.yml".format(ROOT_DIR, name.lower())
    logging.debug(job_path)

    #send an http GET request to the quotes url
    job_url="{0}/{1}?{2}".format(API_JOBS_LINK, name.lower(), IGNORE_QUERY_PARAM)
    job_metadata_request=requests.get(job_url)
    icon = "🏷"

    if job_metadata_request.status_code != 200:
        logging.error("[WARN] Job %s not found with request %s", name.lower(), job_url)
        logging.error("[WARN] In order to proceed, we are replacing the job icon by default: 🏷")
    else:
        icon = job_metadata_request.json()["icon"]


    data_format = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [
            {
                "title": "{} {}`{}`".format(EMBED_TITLE, icon, name),
                "color": EMBED_COLOR,
                "description": EMBED_DESCRIPTION,
                "fields": [
                        {
                            "name": "Documentation",
                            "value": "{0}/{1}/".format(DOC_LINK, name.lower())
                        },
                        {
                            "name": "Version",
                            "value": "*{}*".format(version)
                        },
                        {
                            "name": "Version changelog",
                            "value": changelog
                        }
                    ],
                "footer": {
                    "text": get_random_quote(),
                    "icon_url": AVATAR_URL
                }
            }
        ]
    }

    logging.debug("Dataformat content %s", data_format)
    return data_format

def send_message(web_hook: str, data_format: object):
    """Create the HTTP request to discord API

    Args:
        webHook (str): Discord webhook link
        dataFormat (object): Message body generated from generateData()
    """
    logging.debug("sendMessage(%s, %s)", web_hook, data_format)

    if not web_hook:
        logging.error("[ERROR] Cannot send discord notification as no webHook URL is defined")
        logging.error("[ERROR] Either define environment variable DISCORD_WEBHOOK_RELEASE")
        logging.error("[ERROR] or add argument --webhook")
        sys.exit(1)

    result = requests.post(web_hook, json=data_format)

    if result.status_code != 204:
       logging.error("[ERROR] A problem occurred when sending discord message for this release")
       logging.error("[ERROR] Returned error code: %d", result.status_code)
       logging.error("[ERROR] Result body: %s", result.text)
       sys.exit(1)

    logging.info("Discord notification sent successfully")

def main():
    """Main function of this script
    """
    parser = argparse.ArgumentParser(description="Discord Release Notifier")

    parser.add_argument("--name", '-n',
    type=str, required=True, help="R2DevOps job's name")

    parser.add_argument("--version", "-v",
    type=str, required=True, help="R2DevOps job's version")

    parser.add_argument("--changelog", "-c",
    type=str, required=True, help="R2DevOps job's changelog")

    parser.add_argument("--webhook", "-w",
    type=str, default=os.getenv("DISCORD_RELEASE_WEBHOOK"),
    help="Custom Discord WebHook (default: {})".format(os.getenv("DISCORD_RELEASE_WEBHOOK")))

    parser.add_argument("--debug", "-d",
    dest="loglevel", action="store_const", const=logging.DEBUG,
    default=logging.INFO, help="Logging Level")

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    data_format = generate_data(args.name, args.version, args.changelog)
    send_message(args.webhook, data_format)

if __name__ == "__main__":
    main()
