# 🔐 Gitleaks

## Description

[Gitleaks](https://github.com/zricethezav/gitleaks/wiki/Scanning) is a tool
made to detect hardcoded secrets like passwords, api keys and tokens in git
repos. As it written in go, it is much faster than most of the 
[alternatives](https://github.com/zricethezav/gitleaks/wiki/Comparison-with-other-tools).

## How to use it


1. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/gitleaks.yml'
    ```
2. Well done, your job is ready to work ! 😀

## Job details

* Job name: `gitleaks`
* Docker image:
[`python:3.6-stretch`](https://hub.docker.com/r/_/python)
* Default stage: `static_tests`
* When: `always`
