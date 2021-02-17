# Create or update a job

This page describes how to create or update a job in the
[R2Devops/hub](https://gitlab.com/r2devops/hub/) repository.

In order to contribute efficiently, we recommend you to know following topics:

* [x] [R2Devops hub job structure](/job-structure/)
* [x] [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/){:target=blank}

## Contributing workflow

Follow 3 quick steps above to contribute in the hub 👇

### 🍴 Step 1: Fork !

The first step is to create your own copy of the
[`r2devops/hub`](https://gitlab.com/r2devops/hub/) repository to be
able to work on it before merging your update in the real project.

1. Go on the fork page creation: [`r2devops/hub`](https://gitlab.com/r2devops/hub/-/forks/new)
1. Select the group in which you want to create the fork

### 💻 Step 2: Work in your fork

!!! error "Do not alter `.gitlab-ci.yml`"
    To leverage the R2Devops validaty and security checks on your job, do not
    update the CI/CD configuration file in your fork (`.gitlab-ci.yml` file).

    If you alter it, we will not be able to merge your job in `r2devops/hub`
    repository 😕

1. If you want to add a new job, create a new directory dedicated to your job in `jobs/` folder
1. Ensure to respect rules in this guide
1. Do not update the CI/CD configuration (file `.gitlab-ci.yml`)
1. Test your job and ensure it works

### 🚀 Step 3: Merge request

!!! note "1. Ensure that the last pipeline in your fork passed before going further (check it in `CI/CD > Pipelines`)"

??? note "2. Create a new merge request in your fork (`Merge Requests > New merge request`) 👇"
    1. Select branches
        * As `Source branch`, select the branch in which you have worked in
        your fork (usually `latest`)
        * As `Target branch`, select latest in `r2devops/hub` project
        * Click on `Compare branches and continue`
    1. In `Title`: add short description of your contribution
    1. In `Description`:
        * Do not remove the default content, this is the Definition of Done
            (DoD)
        * Add a description of your contribution with all information
          permitting us to understand what you have done and why. If your
          contribution is related to an existing issue, add a reference:
            ```md
            ## Contribution
            Addition of a new job permitting to build go binaries. Issue
            related: r2devops/hub#945

            ## Definition of Done
            [...]
            ```
        * Add link to your job running and working in a publicly accessible
          Gitlab project
    1. If you want to allow commits from hub maintainers inside your fork
       branch, check the box
       [`Contribution`](https://docs.gitlab.com/ee/user/project/merge_requests/allow_collaboration.html)
        (this isn't available for protected branches like `latest`)

!!! note "3. In the newly created MR, ensure to fulfill all steps of the [job Definition of Done](#job-definition-of-done) and tick related boxes"

Thanks a lot for your contribution 😀🎉 !

Now, we will take a look on your contribution and merge it if everything is ok
👀 Meanwhile, you can join our [Discord community](https://discord.gg/5QKpGqR),
we love talking with our contributors and users !


## Guidelines

!!! warning
    Following these guidelines is required to contribute in
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository

Each jobs must be compliant with following rules:

* [ ] Be compliant with [job structure](/job-structure/)
* [ ] Use the `image` option. Goal is to provide **plug and play** jobs working
  in any environments thanks to containers
* [ ] Use **fixed tag** for docker image and any external tool used inside the
  job. It shouldn't be `latest` or any tag/version that will be overwritten
* [ ] Use only resource with license compatible with the job licence and
  permits to anyone to use it
* [ ] Pass our Continuous Integration pipeline which includes security check
  jobs (pipeline will be run automatically inside your fork)
* [ ] Be compliant with [our job definition](/r2bulary/#job)


## Best practices

!!! info
    Following these best practices is recommended to contribute in
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository

### 🧮 Variables

In order to be customizable, your job should use `variables`. This section
permits to define environment variables, usable by the job script.

!!! tip
    Set default values to your variables to reflect the most common use-case,
    in this way, your job will remains plug-and-play while being customizable

Example of relevant situation to use variable:

* File name
* Path to files or folders
* Any options/parameters used by the job
* Enable or disable job features
* Version of tools retrieved during the job

Example for `newman` job:

=== "Job content"

    ```yaml
    newman:
        image: node:15.4.0
        stage: dynamic_tests
        variables:
            NEWMAN_COLLECTION: "postman_collection.json"
            NEWMAN_GLOBALS_FILE: ""
            NEWMAN_ADDITIONAL_OPTIONS: ""
            NEWMAN_JUNIT_REPORT: "newman-report.xml"
            NEWMAN_FAIL_ON_ERROR: "true"
            NEWMAN_ITERATIONS_NUMBER: "2"
        script:
            - npm install -g newman newman-reporter-junitfull
            - if [[ ! -z ${NEWMAN_GLOBALS_FILE} ]]; then
            -   NEWMAN_ADDITIONAL_OPTIONS+=" -g ${NEWMAN_GLOBALS_FILE}"
            - fi
            - if [[ ! ${NEWMAN_FAIL_ON_ERROR} == "true" ]]; then
            -   NEWMAN_ADDITIONAL_OPTIONS+=" --suppress-exit-code"
            - fi
            - newman run ${NEWMAN_COLLECTION} -r cli,junitfull --reporter-junitfull-export ${NEWMAN_JUNIT_REPORT} -n ${NEWMAN_ITERATIONS_NUMBER} ${NEWMAN_ADDITIONAL_OPTIONS}
        artifacts:
            [...]
    ```

=== "Variables"

    | Name | Description | Default |
    | ---- | ----------- | ------- |
    | `NEWMAN_COLLECTION` <img width=100/> | Name of the Postman collection <img width=175/> | `postman_collection.json` <img width=100/> |
    | `NEWMAN_GLOBALS_FILE` | Name of the Postman globals file for [variables](https://learning.postman.com/docs/sending-requests/variables/) | ` ` |
    | `NEWMAN_ADDITIONAL_OPTIONS` | Other [options](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/) you may want to use with Newman | ` ` |
    | `NEWMAN_FAIL_ON_ERROR` | Fail job on a request/test error | `true` |
    | `NEWMAN_ITERATIONS_NUMBER` | Number of Newman iterations to run (see [documentation](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/#misc)) | `2` |

### 🐳 Choose a Docker image

!!! info
    As described in [our guidelines](#guidelines), all jobs are run inside a
    container instance, so they must specify Docker image to use. Depending of
    your job, it can be tricky to find the perfect image.

The better place to found a docker image is the [docker
hub](https://hub.docker.com/search?q=&type=image). You can start your research
there with following steps :

1. Search for an image prepared with the tool you want to run
    * This is the preferred situation with a ready-to-use docker image that
      doesn't require any additional installation
    * *Example for `mkdocs` job:
      [`squidfunk/mkdocs-material`](https://hub.docker.com/r/squidfunk/mkdocs-material)*
    * If you found it, check it with general guidelines below
1. If there isn't any image prepared with tool you want to run, search for more
general images
    * This case will require to install needed tool as first step of your job.
      If the installation is long or heavy, you should considers to build your
      own image with tool already installed
    * The vast majority of operating system and languages provides official
      images, choose the more appropriate for your job. Examples:
      [`alpine`](https://hub.docker.com/_/alpine),
      [`debian`](https://hub.docker.com/_/debian),
      [`ubuntu`](https://hub.docker.com/_/ubuntu),
      [`python`](https://hub.docker.com/_/python),
      [`node`](https://hub.docker.com/_/node)
1. If you decide to build your own image: the image must be stored in publicly
reachable registry like Docker hub or Gitlab registry

!!! summary "**General guidelines to choose the image**"
    * If the image is official (`OFFICIAL IMAGE` badge on docker hub): this is
      the perfect image for your use case
    * Else, following points should be considered to choose an image:
        * The image must be versioned and not only with `latest` tag. If image
          isn't versioned: it's not usable for your job
        * It should be activelly maintained, with frequent updates and contains
          recent versions
        * The image should be small, containing only required tools
        * The image should be efficient to run the job
        * A large usage of the image can be a good indicator but take care, it
          doesn't guarantee the quality neither security of the image

### 📦 About artifact

The vast majority of jobs produce a result. This result can be of different
kinds:

* Check report
* Build result

In both case, the result should be exposed by the job using
[`artifact`](https://docs.gitlab.com/ee/ci/yaml/#artifacts){:target=blank}
option. It permits to pass artifact to another job of the pipeline and
expose results to users.

Artifact can be configured at different level of integration in Gitlab
interface:

1. Better integration: Gitlab [`artifacts:reports`](https://docs.gitlab.com/ee/ci/yaml/#artifactsreports){:target=blank}

    This is a way to integrate report result in user-friendly way in Gitlab
    interface. We encourage all job contributors to adapt their job output to a
    format compatible with a Gitlab report.

    ??? example "Example of `artifacts:reports:junit` report"
        Example: job [`trivy_image`](/jobs/dynamic_tests/trivy_image/) that
        use its output as `junit` report in `artifacts:repors:junit` section:
        ```yaml
        trivy_image:
          [...]
          artifacts:
            reports:
              junit: "$TRIVY_OUTPUT"
        ```

2. Quick integration with [`artifacts:expose_as`](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target=blank}

    !!! info
        In this case, you need to use `when: always` option under `artifacts`
        if you want to expose result even if job fails.

    This is a way to quickly integrate any format of report in Gitlab Merge
    Request interface. Technically, you don't have to format your report ouput
    in a specific format but we recommend to use `HTML` format. In this way,
    the report is one-click readable from any Merge Request.

    ??? example "Example of `artifacts:expose_as` report"
        Example: job [`trivy_image`](/jobs/dynamic_tests/trivy_image/) that
        use its output as `junit` report in `artifacts:repors:junit` section:
        ```yaml
        nmap:
          [...]
          artifacts:
            expose_as: "nmap-report"
            paths:
              - "${HTML_OUTPUT}"
            when: always
        ```

3. Simple artifact without integration

    !!! info
        In this case, you need to use `when: always` option under `artifacts`
        if you want to expose result even if job fails.

    ??? example "Example of `artifacts`"
        Example: job [`trivy_image`](/jobs/dynamic_tests/trivy_image/) that
        use its output as `junit` report in `artifacts:repors:junit` section:
        ```yaml
        job_name:
          [...]
          artifacts:
            paths:
              - "output"
            when: always
        ```


### Compliance with another job

* Compliance with another job
* Compliance with pages

    Add this job to the list of documentation builder jobs in pages documentation
    The documentation output must be specified in a variable with the default value to documentation_build/ in order to be retrieved by pages job by default


### Documentation of your job `README.md`

TODO

### How to test my job

TODO

* How can I test my job locally/easily ?
> Locally ? using the doxygen binary in my own operating system ? (brew install...)
> Using a blank repo in gitlab ?
> ex: https://gitlab.com/coconux/doxygen and link with the job in WIP Ex: - remote: 'https://gitlab.com/go2scale/hub/-/raw/111-add-doxygen-job/jobs/doxygen/doxygen.yml'
> How can I check the hub documentation went well ?
> Note about including a local job file


### Advises to keep your job generic

TODO

* Try to avoid using `rules`: in majority of cases, `rules` of a job are
  specific to the project on which they will be used. If you use it, your job
  will loose its genericity. Also, some feature requiring specific workflows,
  as [Gitlab Merge
  Trains](https://docs.gitlab.com/ee/ci/merge_request_pipelines/pipelines_for_merged_results/merge_trains/)
  are more easily implemented by users if you don't specify `rules` in your
  job.

* Usage of `rules`, `before_script`, `after_Script`, ...


### TODO in another issue

* Stage list in job file with only one stage: the one of the job
* Add contact us at each blocking issue points
* Describe our CI/CD pipeline
