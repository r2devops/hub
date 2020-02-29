# Go2Scale DevSecOps templates

Go2Scale DevSecOps CI & CD jobs & pipelines templates repository

* [Description](#description)
* [Getting started](#getting-started)
    * [Global configuration](#global-configuration)
        * [Optional configuration](#optional-configuration)
    * [Pipeline templates](#pipeline-templates)
    * [Jobs templates](#jobs-templates)
* [Pipeline](#pipeline)
    * [Kubernetes](#kubernetes)
* [Jobs](#jobs)
    * [Quality](#quality)
    * [Build](#build)
    * [Helm](#helm)

## Description

[Jobs repository](https://gitlab.com/go2scale/jobs) contains all Go2Scale
DevSecOps CI & CD jobs & pipelines templates. This documentation goal is to
explain how to use them efficiently and easilly in your projects.

We offer 2 levels of modules:

**Pipeline** templates: multiple jobs assembled in a workflow
* Easy to use, just import the template in your CI configuration
* Must be consitent with your software and deployment type
* Customizable through configuration

**Jobs** templates: only one jobs
* Can be used unitary or to create fully customs pipelines
* Adaptable to any kind of software and deployment type
* Customizable through configuration

## Getting started

### Global configuration

In your Gitlab 🦊 project, your configuration is defined in `.gitlab-ci.yml`
file. If it doesn't exist, create it.

Go2Scale templates needs some global variables, defined at root level
of `.gitlab-ci.yml`:
* `BOT_USER_ID`: ID of your bot user
* `TEMPLATE_REPO_URL`: URL of template repository. If you don't use custom templates, use `gitlab.com/go2scale/templates.git`

Example of declaration in `.gitlab-ci.yml` file:

```
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

#### Optional configuration

If you want to use custom template repo with a restricted access add
these variables. Note that **SECRET** variables must be declared in
CI/CD settings and never in clear text in `.gitlab-ci.yml`:
* `TEMPLATES_REPO_USER`: user name to with at least read access to repository
* **SECRET** `TEMPLATES_REPO_PASSWORD`: password (or token) with at least read access to templates repository

### Pipeline templates

First of all, you have to find for a pipeline template matching with your
project in [Pipelines list](#pipelines).

Once selected, you just have to include it. Example of usage of [kubernetes
pipeline template](#kubernetes) in `.gitlab-ci.yml`:

```
include:
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/kubernetes.gitlab-ci.yml'
```

Note that `2020-02-24_1` in url is the versioning `tag` in jobs repository
used to set the version to use, if you want to use latest version at each run,
you can use `master` instead of this `tag`.

### Job templates

Jobs template usage is simillar to pipeline. Select job(s) you want to use in
[Jobs list](#jobs) and include them in `.gitlab-ci.yml`:

```
include:
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/quality_check.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/helm.gitlab-ci.yml'
```

### Full example

Of course, you can combine pipelines templates, jobs templates and your
own jobs.

An example of a full `.gitlab-ci.yml` file with [kubernetes pipeline
template](#kubernetes), 2 jobs templates and a custom `unit_tests` template:

```
variables:
  # Go2Scale global variables
  BOT_USER_ID: '5097980'
  TEMPLATES_REPO_URL: 'gitlab.com/go2scale/templates.git'
  TEMPLATES_REPO_USER: 'gitlab+deploy-token-112325'
  GITLAB_URL: $CI_SERVER_URL

include:
  # Go2Scale DevSecOps
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/kubernetes.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/terraform.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/load.gitlab-ci.yml'

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

```
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
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/quality_check.gitlab-ci.yml'
  - remote: 'https://gitlab.com/go2scale/jobs/raw/2020-02-24_1/helm.gitlab-ci.yml'

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

Note:
* `code_quality` variable section is specified to customize its behavior
* because we don't use a pipeline template, we have to declare stages list

## Pipelines

### Kubernetes

Build project as Docker image and deploy it on Kubernetes using Helm.

#### Specifications
* File: https://gitlab.com/go2scale/jobs/raw/<TAG>/pipelines/kubernetes.gitlab-ci.yml
* Integration
  * [quality check](#quality)
  * [build](#build)
* Deployment
  * [helm](#helm)

## Jobs

### Quality

Auto-detect file in repo and run all [coala](https://coala.io) relevant linters on it.

#### How to use it
* Variables:
  * **TODO:** put variables from https://gitlab.com/go2scale/dockerfiles/quality-check here

#### Specifications
* File: https://gitlab.com/go2scale/jobs/raw/<TAG>/jobs/quality_check.gitlab-ci.yml
* Publications:
  * Full report as artifact
  * Short report in merge request and job logs
* Image:
  * Repository: https://gitlab.com/go2scale/dockerfiles/quality-check
  * Documentation: https://go2scale.gitlab.io/dockerfiles/quality-check

### Build
*Work in progress...*

### Helm

Deploy on your kubernetes cluster using Helm charts.
* In issue branch: review environment
* In master branch: staging environment
* In master branch: production environment (manual)

#### Specifications
* File: https://gitlab.com/go2scale/jobs/raw/<TAG>/jobs/helm.gitlab-ci.yml
* Publications: *TODO*
* Image:
  * Repository: https://gitlab.com/go2scale/dockerfiles/helm
  * Documentation: https://go2scale.gitlab.io/dockerfiles/helm

#### How to use it
* Chart and values files must be in repo, see Variables section
* Use [helm secrets](https://github.com/futuresimple/helm-secrets) to encrypt/decrypt secrets values files
* Values files must be named like `<ENV>.yaml` for clear text and `secrets.<ENV>.yaml` for encrypted
* Variables:
  * `REVIEW_DISABLE`: disable review deployment
  * `STAGING_DISABLE`: disable staging deployment
  * `PRODUCTION_DISABLE`: disable production deployment
  * `CHART_PATH`: path of helm chart to use. Default: `/charts/$CI_PROJECT_NAME`
  * `VALUES_PATH`: path of values files to use. Default: `./conf/values`
* Secret variables:
  * `PGP_PUBLIC`: public PGP key to decrypt secrets values. Use `file` type.
  * `PGP_PRIVATE`: private PGP key to decrypt secrets values. Use `file` type.


