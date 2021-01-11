# Create a new job

<!-- Check https://docs.github.com/en/free-pro-team@latest/developers/github-marketplace -->

Guide to add efficiently and easily new jobs

## Workflow

!!! note
    To leverage the R2Devops validaty and security checks on your job, do not
    update the CI/CD configuration file in your fork (`.gitlab-ci.yml` file).
    If you alter it, we will not be able to merge your job in `r2devops/hub`
    repository.


* Fork the [`r2devops/hub`](https://gitlab.com/r2devops/hub/-/forks/new) project
    <!-- TODO: * Do we need to specify rules about fork visibility ? -->
* Clone the repository locally
* Create a new directory dedicated to your job in `jobs/` folder
* Ensure to respect rules in this guide
* Do not update the CI/CD configuration
* Ensure that the last pipeline in your fork passed
* Ensure to fulfill the [job Definition of Done](#job-definition-of-done)
* Submit Merge request from your fork to source project
* Go2Scale team check and validate your job using automated tests
    <!-- TODO: * How to manage CI/CD pipeline from their project ? We have to manually ensure that they don't alter it? -->


## Structure of a job

!!! tip
    A template of job is available
    [here](https://gitlab.com/r2devops/hub/-/tree/latest/tools/job_template/job_name)
    in the R2Devops hub repository

Jobs are stored in the [R2Devops hub](https://gitlab.com/r2devops/hub)
repository inside the
[`jobs`](https://gitlab.com/r2devops/hub/-/tree/latest/jobs) folder and
follow this standardized structure:

```shell
.
└── jobs
    └── <job_name>
        ├── <job_name>.yml        # Job definition
        ├── job.yml               # Job metadata
        ├── README.md             # Job documentation
        └── versions              # Jobs changelogs
            ├── 0.1.0.md
            └── ...
```

* All mandatory files of the [job structure](/structure#job-structure) must be provided
* All fields from `job.yml` must be fulfilled (excepted `icon` which is optional but if no icon is chosen we put a default icon. We also have to help the user to choose an icon by proving him a link (emojipedia) or anything to choose)

**Mandatory rules for **public** jobs (not enforced private jobs, can be customized for on-premise)**

* Provide evidences of job working (url, screenshots, output, ...)

### 🤖 Job definition

This file must have the same name that the job with the `yml` extension:
`<job_name>.yml`. It contains the Gitlab job configuration in `yaml` format.

!!! info
    * Jobs of the hub uses the Gitlab CI/CD configuration format
    * Jobs of the hub must specify a Docker image to be run in a container
    * See [GitLab CI/CD pipeline configuration reference](https://docs.gitlab.com/ee/ci/yaml/)


**TODO:**
* Must be compliant with our job definition (see #39) (ex: a job mustn't be a daemon)
* What about `stages` global list ?
* Job file must be validated by gitlab (CI lint)
* Must be compliant with our security jobs (#230, #229)

Your job definition file must at least contains the following fields:

* [`image`](#image)
* [`stage`](#stage)
* [`script`](#script)

#### Image

Tag of the image must be a fixed version (not latest)
* Ensure that every resource used by the job has a license permitting to anyone to use it without a strong copyleft
* Docker image version and version of all tools retrieved must be fixed

TODO: link to "how to choose my docker image"

#### Stage

Default stage for the job, from our [default stage list](/use-the-hub/#stages)

#### Script

* Ensure that every resource used by the job has a license permitting to anyone to use it without a strong copyleft
* Docker image version and version of all tools retrieved must be fixed

#### Variables

* Variables naming convention (to be defined, should we require the job name uppercase as prefix for all variables ? Think about a way to verify variables in hub pipeline and permit various configuration for on-premise #231)

#### Artifacts

Use expose_as like in mkdocs job to expose the artifact in the MR

See our Best Practices: TODO LINK

#### Other options


### 🗂 Job metadata

!!! note "Example of `job.yml`"
    ```yaml
    name: super_linter
    description: Bundle of various linters, to validate the quality of your code
    icon: 🔎
    default_stage: static_tests
    maintainer: thomasboni
    license: MIT
    ```

This file, named `job.yml`, contains the job metadata in `yaml` format with
the following fields:

| Name | Description | Mandatory |
| ---- | ----------- | --------- |
| `name` <img width=80/> | Name of the job, must be unique | Yes |
| `description` | Short description of the job | Yes |
| `icon` | Unicode emoji character to represent the job ([emojipedia](https://emojipedia.org))| Yes |
| `default_stage` | Default stage of the job, you have to choose the most relevant stage from our [default stage list](/use-the-hub/#stages) | Yes |
| `maintainer` | Gitlab username of the maintainer | Yes |
| `license` | Open-source licence for the job. You can choose between `Apache-2.0` and `MIT` | Yes |


### 📚 Job documentation

This file, named `README.md`, contains the documentation of a job  in `markdown` format.

### 🏗 Job changelogs

Jobs keep their changelogs in one folder named `versions`. This folder contains
`markdown` files, each of them representing a version and containing list of
changes provided by this version.

!!! info
    * Jobs version must follows the [Semantic Versioning](https://semver.org/)
    format (`MAJOR.MINOR.PATCH`)
    * The first version for a job must be `0.1.0`

Example of a `versions` folder for a job:

```shell
.
└── versions
    ├── 0.1.0.md
    ├── 0.2.0.md
    └── 0.3.0.md
```

**📃 `0.1.0.md`**

```md
* Initial version
```

**📃 `0.2.0.md`**
```md
* Add variable `DOCKERFILE_PATH` which permits specifying custom path to Dockerfile
```

**📃 `0.3.0.md`**
```md
* New variable `DOCKER_USE_CACHE` to be able to cache layers of build
* New variable `DOCKER_CACHE_TTL` to define time to live of cache
* New variable `DOCKER_VERBOSITY` to set the verbosity of the build
* New variable `DOCKER_OPTIONS` to be able to add additional options%
```


## Mandatory criteria



* What about code-owners


### About process:

    The configuration file path must be a variable in the job with default value Doxygen
    If the configuration file already exists: just run Doxygen with variable specifying path to conf file
    Else, as you have started to do:
        Select relevant configuration options in the doxygen doc
        Add them in variables section of the job with the same default value that Doxygen
        DO NOT Generate a default configuration file.
        Create an empty the configuration file (using path specified in variable)
        For all input variables, add them in the file, like:

    - echo "HTML_OUTPUT=$DOXYGEN_HTML_OUTPUT" >> $DOXYGEN_CONFIGURATION
    - echo "INPUT=$DOXYGEN_INPUT" >> $DOXYGEN_CONFIGURATION

    Then, run doxygen like : - doxygen $DOXYGEN_CONFIGURATION

### About artifact:


### About compliance with pages job:

    Add this job to the list of documentation builder jobs in pages documentation
    The documentation output must be specified in a variable with the default value to documentation_build/ in order to be retrieved by pages job by default


### Documentation of your job `README.md`

<!-- TODO: est ce qu'on met les variables dans le fichier job.yml ? -->

### Job definition of done

<!-- TODO -->

### Advises to keep your job generic
<!-- TODO: * Advises or rules ? -->

* Try to avoid using `rules`: in majority of cases, `rules` of a job are specific to the project on which they will be used. If you use it, your job will loose its genericity. Also, some feature requiring specific workflows, as [Gitlab Merge Trains](https://docs.gitlab.com/ee/ci/merge_request_pipelines/pipelines_for_merged_results/merge_trains/) are more easily implemented by users if you don't specify `rules` in your job.
<!-- TODO: * What if the user push the job only for him ? should we refuse ? What about private jobs ? -->

### Merge to `r2devops/hub` latest

<!-- TODO: Guide must include commit squash guidelines: see @Protocole presentation -->

### ABCD

    Create the job
    Test it (How ?)
    Create the documentation page following template
    Add the job in the index list

## Modify existing job

* What about code-owners

    Test the job (How ?)
    Update the doc
    Creation of a new version

