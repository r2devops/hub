#!/usr/bin/env python3

# API documentation: https://docs.gitlab.com/ee/api/labels.html
# 

import requests
from urllib.parse import quote, urlencode
from os import getenv

# API Variables

BASE_API_URL = "https://gitlab.com/api/v4"
PROJECT_NAME = "r2devops/hub"
JOB_TOKEN = getenv("CI_JOB_TOKEN")

def get_labels(project_name, with_counts=False, include_ancestor_groups=True, search=""):
    """Get the first 20 labels of the project
    
    Parameters:
    -----------
    project_name : str
        The name of the project
    with_counts : boolean
        Whether or not to include issue and merge request counts (default : false)
    include_ancestor_groups : boolean
        Include ancestor groups (default : true)
    search : str
        Feywords to filter labels by (default : None)

    Returns:
    --------
    str
        The text of the API response
    """
    headers = {
        'JOB_TOKEN': JOB_TOKEN
    }
    payload = {
        'with_counts': with_counts,
        'include_ancestors_groups': include_ancestor_groups,
        'search': search
    }
    base_label_url = BASE_API_URL + "/projects/" + quote(project_name, safe='') + "/labels"
    url = base_label_url + "?" + urlencode(payload)
    print(url)
    r = requests.get(url, headers=headers)
    return (r.text)


if __name__ == "__main__":
    labels = get_labels(PROJECT_NAME)
    print(labels)