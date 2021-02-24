# Create or update a job

This page describes how to create or update a job in the
[R2Devops/hub](https://gitlab.com/r2devops/hub/) repository.

In order to contribute efficiently, we recommend you to know the following topics:

* [x] [R2Devops hub job structure](/job-structure/)
* [x] [GitLab CI/CD](https://docs.gitlab.com/ee/ci/){:target=blank}

## Contributing workflow

Follow the 3 simple steps below to contribute in the hub. You'll see, it will all go smoothly! 👇

### 🍴 Step 1: Fork!

The first step is to create your own copy of the
[`r2devops/hub`](https://gitlab.com/r2devops/hub/) repository, to be
able to work on it before merging your update in the real project.

1. Go on the fork page creation: [`r2devops/hub`](https://gitlab.com/r2devops/hub/-/forks/new).
1. Select the group in which you want to create the fork.

### 💻 Step 2: Work in your fork

!!! error "Do not alter **`.gitlab-ci.yml`**"
    To leverage the R2Devops validity and security checks on your job, do not
    update the CI/CD configuration file in your fork (`.gitlab-ci.yml` file).

    If you alter it, we will not be able to merge your job in `r2devops/hub`
    repository. 😕

1. Create a new directory dedicated to your job in `jobs/` folder if you want to add a new job. You can use the [job
   template](https://gitlab.com/r2devops/hub/-/tree/latest/tools/job_template/job_name)
   as starting point.
2. Be sure to respect the rules we describe in this guide.
3. Do not update the CI/CD configuration (file `.gitlab-ci.yml`).
4. Test your job and ensure it works!

### 🚀 Step 3: Merge request

!!! note "1. Ensure that the last pipeline in your fork passed before going further (check it in `CI/CD > Pipelines`)"

??? note "2. Create a new merge request in your fork (`Merge Requests > New merge request`) 👇"
    1. Select branches
        * As `Source branch`, select the branch in which you have worked in
        your fork (usually `latest`).
        * As `Target branch`, select latest in `r2devops/hub` project.
        * Click on `Compare branches and continue`.
    1. In `Title`: add short description of your contribution.
    1. In `Description`:
        * Do not remove the default content, this is the [Definition of Done (DoD)](https://go2scale.io/definition-of-done-a-recipe-for-optimal-results/)!
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
        * Add a link to your job running and working in a publicly accessible
          Gitlab project.
    1. If you want to allow commits from hub maintainers inside your fork
       branch, check the box
       [`Contribution`](https://docs.gitlab.com/ee/user/project/merge_requests/allow_collaboration.html)
        (this isn't available for protected branches like `latest`).

!!! note "3. In the newly created MR, ensure to fulfill all the steps of the job's Definition of Done, and tick the related boxes"

Thanks a lot for your contribution 😀🎉 !

Now, we will take a look at your contribution and merge it if everything is ok.
👀 Meanwhile, you can join our [Discord community](https://discord.gg/5QKpGqR) to tell us more about your fresh new contribution.
We love talking with our contributors and users!


## Guidelines (Required)

!!! warning
    Following these guidelines is required to contribute to
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository.

Each jobs must be compliant with these following rules:

* [ ] Be compliant with the [job structure](/job-structure/).
* [ ] Use the `image` option. The goal is to provide **plug and play** jobs working
  in any environments thanks to containers.
* [ ] Use **fixed tag** for docker image and any external tool used inside the
  job. **It shouldn't be `latest` or any tag/version that will be overwritten**.
* [ ] Use only resource with license compatible with the job license, and
  permitting anyone to use it.
* [ ] Pass our Continuous Integration pipeline, which includes security check
  jobs (the pipeline will be run automatically inside your fork 🎢).
* [ ] Be compliant with [our job definition](/r2bulary/#job).


## Best practices (Optional)

!!! info
    Following these best practices is recommended to contribute to
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository.

### 🤖 Job definition

#### 🧮 Variables

In order to be customizable, your job should use `variables`. This section
allows to define environment variables, usable by the job script.

!!! tip
    Set default values to your variables to reflect the most common use-case. 
    This, your job will remain plug-and-play while being customizable.

Example of relevant situation to use variable:

* File name.
* Path to files or folders.
* Any options/parameters used by the job.
* Enable or disable job features.
* Version of tools retrieved during the job.

Here is an example for `newman` job 👇

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
            - newman run ${NEWMAN_COLLECTION} -r cli,junitfull
              --reporter-junitfull-export ${NEWMAN_JUNIT_REPORT}
              -n ${NEWMAN_ITERATIONS_NUMBER} ${NEWMAN_ADDITIONAL_OPTIONS}
        artifacts:
            [...]
    ```

=== "Variables"

    | Name | Description | Default |
    | ---- | ----------- | ------- |
    | `NEWMAN_COLLECTION` <img width=105/> | Name of the Postman collection <img width=175/> | `postman_collection.json` <img width=100/> |
    | `NEWMAN_GLOBALS_FILE` | Name of the Postman globals file for [variables](https://learning.postman.com/docs/sending-requests/variables/) | ` ` |
    | `NEWMAN_ADDITIONAL_OPTIONS` | Other [options](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/) you may want to use with Newman | ` ` |
    | `NEWMAN_FAIL_ON_ERROR` | Fail job on a request/test error | `true` |
    | `NEWMAN_ITERATIONS_NUMBER` | Number of Newman iterations to run (see [documentation](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/#misc)) | `2` |

#### 🐳 Docker image

!!! info
    As described in [our guidelines](#guidelines), all jobs are run inside a
    container instance, so they must specify the Docker image to use. Depending on
    your job, it can be tricky to find the perfect image.

The better place to find a docker image is the [docker
hub](https://hub.docker.com/search?q=&type=image). You can start your research
there with the following steps:

??? note "1. Search for an image prepared with the tool you want to run"
        * This is the preferred situation with a ready-to-use docker image that
          doesn't require any additional installation.
        * *Example for `mkdocs` job:
          [`squidfunk/mkdocs-material`](https://hub.docker.com/r/squidfunk/mkdocs-material)*.
        * If you find it, check it with the general guidelines below.

??? note "2. If there isn't any image prepared for the tool you want to run, search for more general images"
    * This case will require to install needed tool as first step of your job.
      If the installation is long or heavy, you should considers to build your
      own image with the tool already installed.
    * The vast majority of operating system and languages provides official
      images, choose the more appropriate for your job. Some examples:
      [`alpine`](https://hub.docker.com/_/alpine),
      [`debian`](https://hub.docker.com/_/debian),
      [`ubuntu`](https://hub.docker.com/_/ubuntu),
      [`python`](https://hub.docker.com/_/python),
      [`node`](https://hub.docker.com/_/node)

!!! note "3. If you decide to build your own image: the image must be stored in a publicly reachable registry, like Docker hub or Gitlab registry"


**General guidelines to choose the image**

* The first thing to check is if the image is official (`OFFICIAL IMAGE` badge on docker hub): this is the
  perfect image for your use case ![Docker official
  badge](images/docker_official_badge.png){: .docker_official_badge }.
* If it is not, the following points should be considered to choose an image:
    * The image must be versioned and not only with `latest` tag. ==If image
      isn't versioned: it's not usable for your job==.
    * It should be actively maintained, with frequent updates, and contains
      recent versions.
    * The image should be small, containing only required tools.
    * The image should be efficient to run the job.
    * A large usage of the image can be a good indicator but be aware, it
      doesn't guarantee the quality neither the security of the image.

#### 📦 Artifacts

The vast majority of jobs produce a result. This result can be of different
kinds:

* Test report.
* Build result.

In both case, the result should be exposed by the job using the
[`artifact`](https://docs.gitlab.com/ee/ci/yaml/#artifacts){:target=blank}
option. It permits passing an artifact to another job of the pipeline and
expose results to users.

!!! info
    * In the case of a test report, you need to use `when: always` option under
      `artifacts` if you want to expose result even if job fails.
    * You can combine both a build result and a test report by using both
      `artifacts:paths` and `artifacts:reports`.

An artifact can be configured at different level of integration in Gitlab
interface:

1. Better integration: Gitlab [`artifacts:reports`](https://docs.gitlab.com/ee/ci/yaml/#artifactsreports){:target=blank}

    This is a way to integrate a report result in an user-friendly way in Gitlab's
    interface. We encourage all job contributors to adapt their job output to a
    format compatible with a Gitlab report.

    ??? example "Example of `artifacts:reports:junit` report"
        Job [`trivy_image`](/jobs/dynamic_tests/trivy_image/) that
        uses its output as `junit` report in `artifacts:reports:junit` section:
        ```yaml
        trivy_image:
          [...]
          artifacts:
            reports:
              junit: "$TRIVY_OUTPUT"
        ```

2. Quick integration with [`artifacts:expose_as`](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target=blank}

    This is a way to quickly integrate any format of report in Gitlab Merge
    Request interface. Technically, you don't have to format your report output
    in a specific format, but we recommend to use `HTML` format. In this way,
    the report is one-click readable from any Merge Request.

    ??? example "Example of `artifacts:expose_as` report"
        Job [`nmap`](/jobs/dynamic_tests/nmap/) uses `artifacts:expose_as`
        to expose its `HTML` report:
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

    ??? example "Example of `artifacts`"
        Job that specify an `artifact`:
        ```yaml
        job_name:
          [...]
          artifacts:
            paths:
              - "output"
            when: always
        ```

#### 🔩 Keep genericity

The jobs of the hub should remain as generic as possible. In order to ensure it:

* Try to avoid using `rules` options, that is strongly linked to the context of
  the user and so should be set by the user. Also, some features requiring
  specific workflows, as [Gitlab Merge
  Trains](https://docs.gitlab.com/ee/ci/merge_request_pipelines/pipelines_for_merged_results/merge_trains/){:target=blank},
  are more easily implemented by users if you don't specify `rules` in your
  job.
* Try to avoid using `before_script` and `after_script` to let users the
  possibility to redefine these options while exploiting to the maximum your
  job.

!!! info
    The jobs of the hub can be dynamically
    [customized](/use-the-hub/#jobs-customization) by users.


### 📖 Job documentation

As described in [R2Devops/hub job
structure](/job-structure/#job-documentation), the documentation of a job is
written inside its `README.md` file.

!!! tip
    Don't hesitate to copy the documentation from another job as starting
    point. For example, the raw content of [openapi
    `README.md`](https://gitlab.com/r2devops/hub/-/raw/latest/jobs/openapi/README.md)

We recommend including the following sections in your documentation:

* Objective: describe the goal of your job.
* How to use it: a list of steps to quickly use your job.
* Job details: describes details of the job (name, docker image, stage, etc).
* Variables: table listing variables used by the job (name, description,
  default value, mandatory if needed).
* Artifacts: describes artifact(s) defined by the job.

### 🚄 Compliance with another job

Several jobs of the hub can be used together without any configuration. This is
currently implemented for all jobs producing an `HTML` output and the job
[`pages`](/jobs/deploy/pages/) which deploys the `HTML` on a webserver.

!!! info
    This feature is empowered by the `artifacts` option: jobs producing a
    static website output give it to the `pages` job through an artifact stored
    in a standard path: `${CI_PROJECT_DIR}/website_build`.

So, if your job produce a static website output, ensure to store the result of
the build in `${CI_PROJECT_DIR}/website_build`, and to configure this path as
artifact. You can see an example in [`mkdocs`](/jobs/build/mkdocs/) job.

### 🧪 Test your job

In order to test your job before merging it into the hub, we recommend you to
follow these steps:

1. Test the behavior of your job inside a local container on your machine (with
   the same image you want to use for the job). To simulate the GitLab job
   that will run it on your project, you can mount the repository folder inside
   the container:
      ```shell
      # Example if your job will use node:15.7-buster as Docker image docker run -v
      /path/to/your/repo:/mnt --entrypoint "/bin/sh" -it node:15.7-buster
      ```

2. Create your job configuration in a repository and test it locally using
   [`include
   local`](https://docs.gitlab.com/ee/ci/yaml/#includelocal){:target=blank},
   instead of `remote` from the hub. For example:

    ```yaml
    include:
        - local: 'my-work-in-progress-job.yml'
    ```
