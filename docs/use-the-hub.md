---
title: How to use the hub | Prerequisites and quick setup
description: Discover how to use the hub. You’ll find here the prerequisites, a quick setup and how to customize a job. Those topics will have no secret for you!
---

# Use the hub

## 📝 Prerequisites

* 🦊  Manage your project in GitLab and understand what is [CI/CD with GitLab](https://docs.gitlab.com/ee/ci/){:target="_blank"}
* 🔫  Be aware: each file modification in your project can trigger a [Pipeline](/r2bulary/#pipeline)
* 🗝  Have access to the pipelines page in your GitLab project and write access to your project `.gitlab-ci.yml` file

## ⏳ Quick setup

Follows these steps to setup your CI/CD pipeline in less than 5 minutes!

1. If you haven't yet a `.gitlab-ci.yml` file in the root on your repository:
   create it with the following list of stages:

    ```yaml
    stages:
      - build
      - tests
      - provision
      - review
      - release
      - deploy
      - others
    ```

    !!! info
        You can check the [stages](#stages) section to get more information about this list
        or if you already have a configuration with different stages.

2. Select the Jobs you want in the [jobs section](https://r2devops.io/jobs) and append their URL in the
   `include` list of your `.gitlab-ci.yml` file:

    ```yaml
    include:
       - remote: 'https://api.r2devops.io/job/r/<owner_name>/<job_name>/<version_number>.yml'
       - remote: 'https://api.r2devops.io/job/r/<owner_name>/<job_name>/<version_number>.yml'
      - ...
    ```

    !!! note

        By default, the `latest` version of a job is used. You can choose to
        use a specific version thank to a `tag`. Available tags are described for
        each job in the [labels section](/labels). The description of the `tag` format is
        available in the [versioning page](/versioning/).

        Once your pipeline is functional, we recommend using a specific version
        for the jobs in order to ensure that your pipeline will not be broken by a
        job update.

3. The jobs can be customized 👉 check the [jobs
   customization](#jobs-customization) section.

4. Everything is ready! You can now benefit the full power of a CI/CD
   pipeline 🎉🚀

    !!! tip
        You can also combine job's templates and your own jobs in your
        `.gitlab-ci.yml` configuration file.

<a alt="See all jobs" href="https://r2devops.io/_/jobs">
    <button class="md-button border-radius-10 md-button-center" >
        See all jobs available <img alt="" class="heart" src="../images/rocket.png">
    </button>
</a>

## 🤓 Pipeline examples

* Several examples of projects using R2Devops hub:

    * Python flask based REST API permitting to play TicTacToe 👉 [tictactoe/grid-api](https://gitlab.com/tictac-toe/grid-api)
    * Vue.js project providing a client to the TicTacToe API 👉 [tictactoe/grid-frontend](https://gitlab.com/tictac-toe/grid-frontend)
    * React.js project providing our landing page 👉 [r2devops/landing-page](https://gitlab.com/r2devops/landing-page)

* An example of a full `.gitlab-ci.yml` configuration using jobs from the hub 👇

    !!! info "Jobs used in the example"
        * Plug-and-play set of jobs from the hub to automatically build, test
          and deploy static documentation website:
            * [`mkdocs`](https://r2devops.io/_/r2devops-bot/mkdocs/) (`latest`
              version)
            * [`lighthouse`](https://r2devops.io/_/r2devops-bot/lighthouse/)
              (`latest` version)
            * [`pages`](https://r2devops.io/_/r2devops-bot/pages/) (`latest`
              version)
        * Plug-and-play set of jobs from the hub to automatically build, push
          and test docker images:
            * [`docker_build`](https://r2devops.io/_/r2devops-bot/docker_build/)
              (version `0.3.0`)
            * [`trivy_image`](https://r2devops.io/_/r2devops-bot/trivy_image/)
              (version `0.2.0`)
        * A custom manual job `unit_tests`

    ``` yaml
    stages:
    - build
    - tests
    - provision
    - review
    - release
    - deploy
    - others

    # Jobs from r2devops.io (they don't need any configuration in standard cases)
    include:
    - remote: 'https://api.r2devops.io/job/r/r2devops-bot/mkdocs/latest.yaml'
    - remote: 'https://api.r2devops.io/job/r/r2devops-bot/lighthouse/latest.yaml'
    - remote: 'https://api.r2devops.io/job/r/r2devops-bot/pages/latest.yaml'
    - remote: 'https://api.r2devops.io/job/r/r2devops-bot/docker_build/0.2.0.yaml'
    - remote: 'https://api.r2devops.io/job/r/r2devops-bot/trivy_image/0.2.0.yaml'

    # Locally configured job
    unit_tests:
      image: python:3.9-alpine
      stage: tests
      before_script:
        - pip install pipenv && pipenv --bare install --dev
      script:
        - make test
    ```

## ▶ Stages

By default, each job from the hub is a part of on these stages:

* **🧱 Build:** building and packaging of the software
* **🔎 Tests:** testing your repository files with dynamic and static tests
* **🛠 Provision:** preparation of the software infrastructure
* **👌 Review:** deployment of the software in an isolated review environment
* **🏷 Release:** releasing and tagging of the software
* **🚀 Deploy:** deployment of the software on environments
* **🦄 Others:** all other magic jobs not included in previous stages

This is an efficient and simple workflow. Nevertheless, if you want to use your
own custom stage list: you can re-declare yourself the stage of any job from
the hub. Follow the [customization section](#jobs-customization) to do it.

## 🔧 Jobs customization

!!! info
    All the jobs from the `r2devops/hub` specify a docker image to be run in a
    docker container.

### 🖌 Global

Each jobs of the hub can be customized. To do it, you have to include the job
URL as usual and, in addition, override the options you want to customize.

!!! tip
    This way, you can override all Gitlab jobs parameters. All parameters
    are described in [Gitlab
    documentation](https://docs.gitlab.com/ee/ci/yaml/){:target="_blank"}.

For example, if you want to use the [trivy_image](https://r2devops.io/_/r2devops-bot/trivy_image) job and
customize it by:

* Redefining the `stage` to `security` to fit in your personal stages workflow,
* Set the variable `TRIVY_VERSION` to `0.9.1` to use this version instead of
  the default,
* Set the variable `TRIVY_SEVERITY` to `CRITICAL` to display only CRITICAL
  issues.

```yaml
include:
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/trivy_image/latest.yaml'

trivy_image:
  stage: security
  variables:
    TRIVY_VERSION: "0.9.1"
    TRIVY_SEVERITY: "CRITICAL"
```

### ✏️  Use custom stage

If you want to use your own stage name, it's possible to do so when including
your job. Example:

```yaml
stages:
  - security

include:
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/trivy_image/latest.yaml'

trivy_image:
  stage: security
```


### 🐳 Advanced: `services`

You may want one of your job to interact with a container instance (API,
database, web server...) to work. GitLab has an option to run a container next
to a job: [`services`](https://docs.gitlab.com/ee/ci/yaml/#services).

To use this option, you must have access to an image of the container you want
to run as a service. For example, if you are using our
[docker_build](https://r2devops.io/_/r2devops-bot/docker_build/) job to build an
image of your application, and you want to test this image using the
[nmap](https://r2devops.io/_/r2devops-bot/nmap) job, just add the following configuration in
your `.gitlab-ci.yml` file:

!!! info
    * The `name` option must contain your image name and tag, or an image name from [Docker Hub](https://hub.docker.com){:target="_blank"}.
    * The `alias` option permits to the job to reach your application using a name. This name
    must be the same that the one specified inside the job target's variable.
    * You may also run some other services, like a database depending on your application needs.

```yaml
nmap:
  services:
    - name: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
      alias: app
```


### 🎶 Multiple usage of the same job in your pipeline


If you want to reuse a job from the hub, for example launching `apiDoc` to build 2 API documentations in the same pipeline, you can easily do so with the Hub's jobs using ==extends== GitLab keyword.

``` yaml hl_lines="13"

stages:
  - build

include:
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/apidoc/0.2.0.yaml'

apidoc:
  variables:
    APIDOC_CONFIG_PATH: src/doc/project1/apidoc.json
    APIDOC_OUTPUT_PATH: website_build/apidoc/project1/

apidoc_project2:
  extends: apidoc
  variables:
    APIDOC_CONFIG_PATH: src/doc/project2/apidoc.json
    APIDOC_OUTPUT_PATH: website_build/apidoc/project2/

```

!!! warning
    Be aware to have different artifacts path to not overwrite your first artifact by the second one.

--8<-- "includes/abbreviations.md"
