# Getting started

Follows these steps to setup your CI/CD pipeline in less than 10 minutes !

1. Select jobs you want in [Jobs section](/Jobs/)

    !!! info
        You can choose to use the latest version or a specific one for each
        job. Available version tag and corresponding url are described for each
        jobs in [Jobs section](/Jobs/).

        Once your pipeline is functional, we recommend to use specific version
        for jobs in order to ensure that your pipeline will not be broken by a
        job update.

        Details about versioning format are available in [Versioning
        page](/versioning/).

2. Create a new file named `.gitlab-ci.yml` in the root on your repository
3. Fulfil it with the following content using all selected jobs url:

    ```yaml
    stages:
      - static_tests
      - build
      - dynamic_tests
      - review
      - deployment

    include:
      - remote: '<JOB-URL>'
      - remote: '<JOB2-URL>'
      - remote: ...
    ```

3. Some jobs in [Jobs section](/Jobs/) provides options. You can configure them
   using the `variables` keyword in `.gitlab-ci.yml`:

    ```yaml
    variables:
      <OPTION_JOB1>: <VALUE>
      <OPTION2_JOB1>: <VALUE>
      <OPTION_JOB2>: <VALUE>
      ...
    ```

4. Everything is ready! You can now benefit the full power of a CI / CD
   pipeline 🎉🚀

## Example

You can also combine jobs templates and your own jobs in `.gitlab-ci.yml`
configuration file.

An example of a full `.gitlab-ci.yml` file with:

* One job template with latest version. Note that `/latest` is optional in the
  job URL
* One job template with specific version using tag `2020-06-22_1`
* Configuration for one job using `variables`
* A custom `unit_tests` job

``` yaml
stages:
  - static_tests
  - build
  - dynamic_tests
  - review
  - deployment

# Jobs from g2s hub
include:
  - remote: 'https://jobs.go2scale.io/docker/latest'
  - remote: 'https://jobs.go2scale.io/mkdocs/2020-06-22_1'

# Some jobs can be configured with variables
variables:
  DOC_TOOL: mkdocs

# You can also include your own jobs
unit_tests:
  image: python:3.7-alpine3.10
  stage: static_tests
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

-->
