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


## Jobs criteria

### Structure of a job

!!! tip
    A template of job is available
    [here](https://gitlab.com/r2devops/hub/-/tree/latest/tools/job_template/job_name)
    in the R2Devops hub repository

Jobs are stored in the [R2Devops hub](https://gitlab.com/r2devops/hub)
repository inside the
[`jobs`](https://gitlab.com/r2devops/hub/-/tree/latest/jobs) folder and
follow this standardized structure:

```
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

#### Job definition

This file must have the same name that the job with the `yml` extension:
`<job_name>.yml`. It contains the Gitlab job configuration in `yaml` format.

See [GitLab CI/CD pipeline
configuration reference](https://docs.gitlab.com/ee/ci/yaml/) (`yaml`).

#### Job metadata: `job.yml`

This file, named `job.yml`, contains the job metadata, in `yaml` format, with
the following fields:

* `name`: name of the job
* `description`: short description of the job
* `default_stage`: default stage of the job, you have to choose the most
  relevant stage from our [default stage list](/use-the-hub/#stages)
* `icon`: TODO
* `maintainer`: TODO
* `license`: TODO

Example:

```yaml

```

#### Job documentation: `README.md`
* `README.md`: file containing documentation of a job (`markdown`)
* `versions`: folder containing releases notes files for each versions of the job
    * `0.1.0.md`: release note

### Mandatory criteria

* All mandatory files of the [job structure](/structure#job-structure) must be provided
* All fields from `job.yml` must be fulfilled (excepted `icon` which is optional but if no icon is chosen we put a default icon. We also have to help the user to choose an icon by proving him a link (emojipedia) or anything to choose)
* Job file must be validated by gitlab (CI lint)

## Mandatory rules for **public** jobs (not enforced private jobs, can be customized for on-premise)

* The job must be run in a docker container
* Provide evidences of job working (url, screenshots, output, ...)
* Must be compliant with our security jobs (#230, #229)
* Must be compliant with our job definition (see #39) (ex: a job mustn't be a daemon)
* Variables naming convention (to be defined, should we require the job name uppercase as prefix for all variables ? Think about a way to verify variables in hub pipeline and permit various configuration for on-premise #231)
* Ensure that every resource used by the job has a license permitting to anyone to use it without a strong copyleft
* Ensure that every resource used by the job has a license compatible with the job license
    * **Question**: is it possible to use a GPL tool in my job if my job is delivered under Apache or MIT ?
* Docker image version and version of all tools retrieved must be fixed


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

    Use expose_as like in mkdocs job to expose the artifact in the MR

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
    Creation of a new tag

## Modify existing job

* What about code-owners

    Test the job (How ?)
    Update the doc
    Creation of a new tag

