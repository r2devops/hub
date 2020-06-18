# Getting started

1. Select jobs you want in [Jobs section](/Jobs/)
2. Fulfil the following file with all selected jobs

    ```yaml
    stages:
      - code_level
      - build
      - review
      - application_level
      - staging
      - production
      - performance

    include:
      - remote: '<JOB-URL>'
      - remote: '<JOB2-URL>'
      - remote: ...
    ```

3. Store this file in `.gitlab-ci.yml` in the root on your repository
4. Use the full power of a CI/CD pipeline 🚀

## Example

Of course, you can combine jobs templates and your own jobs.

An example of a full `.gitlab-ci.yml` file with [kubernetes pipeline
template](#kubernetes), 2 jobs templates and a custom `unit_tests` template:

``` yaml

stages:
  - code_level
  - build
  - review
  - application_level
  - staging
  - production
  - performance

# Jobs from g2s hub
include:
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_3/jobs/mkdocs/mkdocs.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_3/jobs/coala/coala.yml'

# Some jobs can be configured with variables
variables:
  QUALITY_ERROR_LEVEL: MAJOR
  DOC_TOOL: mkdocs

# You can also include your own jobs
unit_tests:
  image: python:3.7-alpine3.10
  stage: code_level
  before_script:
    - apk add gcc make musl-dev postgresql-dev git linux-headers libmagic jpeg-dev zlib-dev
    - pip install pipenv && pipenv --bare install --dev
  script:
    - make test
```

<!--

TODO: Check what to do about it. Should we require a standard template and put
configuration doc here ?






## Global configuration

In your Gitlab 🦊 project, your configuration is defined in `.gitlab-ci.yml`
file. If it doesn't exist, create it.

Go2Scale templates needs some global variables, defined at root level
of `.gitlab-ci.yml`:

* `BOT_USER_ID`: ID of your bot user
* `TEMPLATE_REPO_URL`: URL of template repository. If you don't use custom templates, use `gitlab.com/go2scale/templates.git`

Example of declaration in `.gitlab-ci.yml` file:

``` yaml
variables:
  # Go2Scale global variables
  BOT_USER_ID: '5097980'
  TEMPLATES_REPO_URL: 'gitlab.com/go2scale/templates.git'
```

Additionally, you have to decalare secrets variables
([how to do it ?](https://docs.gitlab.com/ee/ci/variables/#creating-a-custom-environment-variable))
in project (or supergroup) CI/CD settings:

* `DOCKER_AUTH_CONFIG`: docker auth configuration (*given by Go2Scale*) to access images
* `BOT_TOKEN`: secret token of bot user to interact with Gitlab API

### Optional configuration

If you want to use custom template repo with a restricted access add
these variables. Note that **SECRET** variables must be declared in
CI/CD settings and never in clear text in `.gitlab-ci.yml`:

* `TEMPLATES_REPO_USER`: user name to with at least read access to repository
* **SECRET** `TEMPLATES_REPO_PASSWORD`: password (or token) with at least read access to templates repository

