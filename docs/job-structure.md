---
title: How to build a CI/CD job
description: Discover the content of a job ! The definition, metadata, documentation, changelogs and screenshots are simply described.
---

# Structure of a job

Jobs are stored in the [R2Devops hub](https://gitlab.com/r2devops/hub)
repository inside the
[`jobs`](https://gitlab.com/r2devops/hub/-/tree/latest/jobs) folder, and
follow this standardized structure:

```
.
└── jobs
    └── <job_name>
        ├── CHANGELOG.md          # Changelog of the job
        ├── job.yml               # Job metadata
        ├── README.md             # Job documentation
        └── screenshots           # (Optional) Job screenshots
            ├── job_picture.png
            └── ...
```

*A template of job is available in the [R2Devops hub repository](https://gitlab.com/r2devops/hub/-/tree/latest/tools/job_template/r2_jobname).*

## 🤖 Job definition

This file must have the same name as the job with the `yml` extension:
`<job_name>.yml`. It contains the Gitlab job configuration in `yaml` format.

The jobs of the hub use the Gitlab CI/CD configuration format. They must specify a Docker image to be run in a container.

!!! info
    If you are curious and want to know more about the job definition, you can go to:

    * [GitLab CI/CD pipeline configuration reference](https://docs.gitlab.com/ee/ci/yaml/){:target=blank}.
    * [R2Devops guidelines and best practices](/create-update-job/#guidelines) about job definition.

Job definition usually contains the following fields:

* **[`image`](https://docs.gitlab.com/ee/ci/yaml/#image){:target="_blank"}**: this is the docker image used to run the job.
* **`stage`** (mandatory): this is the default stage for the job. You can choose you in our [default stage list](/use-the-hub/#stages).
* **[`script`](https://docs.gitlab.com/ee/ci/yaml/#script){:target="_blank"}** (mandatory): this is the heart of the job. It contains a list of shell commands to run the job.
* **[`variables`](https://docs.gitlab.com/ee/ci/yaml/#variables){:target="_blank"}**: in this field, you will find all the variables used by the `script` of the job. This is where you customize its behavior.
* **[`artifacts`](https://docs.gitlab.com/ee/ci/yaml/#artifacts){:target="_blank"}**: it specifies the result of the job that should be exposed to the user through classic artifact or Gitlab reports.

**Here is an example of job definition [`apidoc.yml`](https://r2devops.io/_/r2devops-bot/apidoc/) 👇**

```yaml
apidoc:
  image:
    name: node:12.18.3-alpine3.12
    entrypoint: [""]
  stage: build
  variables:
    APIDOC_CONFIG_PATH: '.'
    APIDOC_OUTPUT_PATH: 'website_build/'
    APIDOC_TEMPLATE_PATH: '/usr/local/lib/node_modules/apidoc/template/'
    APIDOC_VERSION: '0.24.0'
  script:
    - npm install apidoc@$APIDOC_VERSION -g
    - apidoc -c "$APIDOC_CONFIG_PATH" -o "$APIDOC_OUTPUT_PATH" -t "$APIDOC_TEMPLATE_PATH"
  artifacts:
    when: always
    expose_as: "apiDoc build"
    paths:
      - "$APIDOC_OUTPUT_PATH"
```


## 📚 Job documentation

This file, named `README.md`, contains the documentation of a job  in `markdown` format.

!!! info
      The documentation explains what the job does, how to use it and to customize it. A clear documentation is important: no one wants to use a job when you can't understand what it is for!

=== "Example of README.md"

    ```md
    ## Objective

    Creates a versioned HTML documentation from API annotations in your source
    code using [apiDoc](https://www.apidocjs.com/).

    ## How to use it

    1. Prepare your project with API annotations in your source code following
       [apiDoc format](https://apidocjs.com/#examples) and your [apiDoc
       configuration file](https://apidocjs.com/#configuration).
    2. Choose a version in [version list](#changelog)
    3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
       started](/use-the-hub/)). Example:
        ```yaml
        include:
        - remote: 'https://jobs.r2devops.io/apidoc.yml'
        ```
    4. If you need to customize the job (stage, variables, ...) 👉 check the
       [jobs customization](/use-the-hub/#jobs-customization)
    5. Well done, your job is ready to work ! 😀

    ## Variables

    | Name | Description | Default |
    | ---- | ----------- | ------- |
    | `APIDOC_VERSION` | Version of apiDoc to use | `0.24.0` |
    | `APIDOC_CONFIG_PATH` | Path to config file or to directory containing config file (apidoc.json or apidoc.config.js) | `.` |
    | `APIDOC_OUTPUT_PATH` | Output directory path | `/documentation_build` |
    | `APIDOC_TEMPLATE_PATH` | Path to template folder | `/usr/lib/node_modules/apidoc/template/` |
    ```

=== "Result"

    ![Documentation result](images/documentation_result.png){: .documentation_result }


## 🏗 Job changelogs

Jobs keep their changelogs in one file named `CHANGELOG.md`. This file contains all changes made to the job since its creation.It uses the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/){:target="_blank"} format.

!!! info
    * The jobs version must follow the [semantic versioning](https://semver.org/)
    format (`MAJOR.MINOR.PATCH`).
    * The first version for a job must be `0.1.0`.

**Here is an example of `CHANGELOG.md` file for a `docker_build` 👇**

```md
## [0.3.0] - 2020-11-25
* New variable `DOCKER_USE_CACHE` to be able to cache layers of build
* New variable `DOCKER_CACHE_TTL` to define time to live of cache
* New variable `DOCKER_VERBOSITY` to set the verbosity of the build
* New variable `DOCKER_OPTIONS` to be able to add additional options

## [0.2.0] - 2020-11-02
* Add variable `DOCKERFILE_PATH` which permits specifying custom path to
  Dockerfile

## [0.1.0] - 2020-10-21
* Initial version
```

## 🖼️ Job screenshots

An image is worth a thousand words. It is why jobs can include screenshots, or any pictures, to improve documentation and
provide an overview of what the job does.

You can add as many pictures as you want in this folder, but try to add only
relevant images. You just have to put the file inside the folder, and they will
be included in the documentation.

Supported format: `.png`, `.jpeg`, `.jpg`

!!! tip
    If you don't want to add pictures, you don't have to, it's only 
    a bonus to ease the understanding of your new job!
