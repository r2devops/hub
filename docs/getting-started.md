# Getting started

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

## Pipeline templates

First of all, you have to find for a pipeline template matching with your
project in [Pipelines list](#pipelines).

Once selected, you just have to include it. Example of usage of [kubernetes
pipeline template](#kubernetes) in `.gitlab-ci.yml`:

``` yaml
include:
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/pipelines/kubernetes.gitlab-ci.yml'
```

Note that `2020-03-05_1` in url is the versioning `tag` in jobs repository
used to set the version to use, if you want to use latest version at each run,
you can use `master` instead of this `tag`.

## Job templates

Jobs template usage is simillar to pipeline. Select job(s) you want to use in
[Jobs list](#jobs) and include them in `.gitlab-ci.yml`:

``` yaml
include:
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/quality_check.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/helm.gitlab-ci.yml'
```

## Full example

Of course, you can combine pipelines templates, jobs templates and your
own jobs.

An example of a full `.gitlab-ci.yml` file with [kubernetes pipeline
template](#kubernetes), 2 jobs templates and a custom `unit_tests` template:

``` yaml
variables:
  # Go2Scale global variables
  BOT_USER_ID: '5097980'
  TEMPLATES_REPO_URL: 'gitlab.com/go2scale/templates.git'
  TEMPLATES_REPO_USER: 'gitlab+deploy-token-112325'
  GITLAB_URL: $CI_SERVER_URL

include:
  # Go2Scale DevSecOps
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/pipelines/kubernetes.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/terraform.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/load.gitlab-ci.yml'

unit_tests:
  image: python:3.7-alpine3.10
  stage: code_level
  before_script:
    - apk add gcc make musl-dev postgresql-dev git linux-headers libmagic jpeg-dev zlib-dev
    - pip install pipenv && pipenv --bare install --dev
  script:
    - make test
```

*Note that terraform & load jobs used in this example aren't available yet*

An example of a full `.gitlab-ci.yml` file with 2 jobs templates and a custom
`unit_tests` template:

``` yaml
variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: ""
  # Go2Scale global variables
  BOT_USER_ID: '5097980'
  TEMPLATES_REPO_URL: 'gitlab.com/go2scale/templates.git'
  TEMPLATES_REPO_USER: 'gitlab+deploy-token-112325'
  GITLAB_URL: $CI_SERVER_URL

stages:
  - code_level
  - build
  - review
  - application_level
  - staging
  - production

include:
  # Go2Scale DevSecOps
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/quality_check.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/helm.gitlab-ci.yml'

code_quality:
  QUALITY_SEVERITY_LEVEL: 'MAJOR'
  QUALITY_IGNORED_FILES: '.gitlab/**'

unit_tests:
  image: python:3.7-alpine3.10
  stage: code_level
  before_script:
    - apk add gcc make musl-dev postgresql-dev git linux-headers libmagic jpeg-dev zlib-dev
    - pip install pipenv && pipenv --bare install --dev
  script:
    - make test
```

!!! note
    * `code_quality` variable section is specified to customize its behavior
    * because we don't use a pipeline template, we have to declare stages list

