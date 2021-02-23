<!-- Check https://docs.github.com/en/free-pro-team@latest/developers/github-marketplace -->


# Contributing guide

Guide to add efficiently and easily new jobs

## hub structure

TODO: define whole structyre

## vision and mission

TODO: define vision and mission but in concept page, not here

## Create an issue

Describe how to write an issue

## Job structure

TODO: move this section in dedicated page ?

All jobs are based on a docker image

Add information about the structure of a job directory and what need to be here.

```tree
.
└── jobs                            # Folder containing jobs sources
    └── docker_build
        ├── docker_build.yml        # Job content
        ├── job.yml                 # Job metadata
        ├── README.md               # Job documentation
        └── versions                # Jobs changelogs
            ├── 0.1.0.md
            └── ...
```

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


## Create a new job

* What about code-owners

### How to choose the best docker to implement new job ?
    Check the job is maintained
    Check the size (smallest is the best)
    Check the job has versioning (not only latest)
    If criteria above are not met --> ##Create my docker from Alpine image
    Choose the officiel Alpine image in latest (think to fix version after)
    Install doxygen in the first line of the script 'apk add --no-cache doxygen==1.8.18-r0'

    The installed version of Doxygen must be specified as variable with the default value on the current latest version 1.8.18-r0
    A fixed tag must be specified for the alpine image used


### How can I test my job locally/easily ?
    Locally ? using the doxygen binary in my own operating system ? (brew install...)
    Using a blank repo in gitlab ? ex: https://gitlab.com/coconux/doxygen and link with the job in WIP Ex: - remote: 'https://gitlab.com/go2scale/hub/-/raw/111-add-doxygen-job/jobs/doxygen/doxygen.yml'
    How can I check the hub documentation went well ?
    ...

### About versions:

    The installed version of Doxygen must be specified as variable with the default value on the current latest version 1.8.18-r0
    A fixed tag must be specified for the alpine image used

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

    Use `expose_as` like in [mkdocs](https://gitlab.com/r2devops/hub/-/blob/latest/jobs/mkdocs/mkdocs.yml) job to expose the artifact in the MR

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

