# Create or update a job

This page describes how to create or update a job in the
[R2Devops/hub](https://gitlab.com/r2devops/hub/) repository.

In order to contribute efficiently, we recommend you to know following topics:

* [R2Devops hub job structure](#job-structure)
* [Gitlab CI/CD](https://docs.gitlab.com/ee/ci/)

## Contributing workflow

Follow 3 quick steps above to contribute in the hub 👇

### 🍴 Step 1: Fork !

The first step is to create your own copy of the
[`r2devops/hub`](https://gitlab.com/r2devops/hub/) repository to be
able to work on it before merging your update in the real project.

1. Go on the fork page creation: [`r2devops/hub new fork`](https://gitlab.com/r2devops/hub/-/forks/new)
1. Select the group in which you want to create the fork

### 💻 Step 2: Work in your fork

!!! note
    To leverage the R2Devops validaty and security checks on your job, do not
    update the CI/CD configuration file in your fork (`.gitlab-ci.yml` file).
    If you alter it, we will not be able to merge your job in `r2devops/hub`
    repository.

1. If you want to add a new job, create a new directory dedicated to your job in `jobs/` folder
1. Ensure to respect rules in this guide
1. Do not update the CI/CD configuration (file `.gitlab-ci.yml`)
1. Test your job and ensure it works

### 🚀 Step 3: Merge request

1. Ensure that the last pipeline in your fork passed before going further
   (check it in `CI/CD > Pipelines`)
1. Create a new merge request in your fork (`Merge Requests > New merge request`)
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
          contribution is related to an existing issue, add a reference.
          Example:
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
       branche, check the box
       [`Contribution`](https://docs.gitlab.com/ee/user/project/merge_requests/allow_collaboration.html)
        (this isn't available for protected branches like `latest`)
1. In the newly created MR, ensure to fulfill all steps of the [job Definition
   of Done](#job-definition-of-done) and tick related boxes
1. Thanks a lot for your contribution 😀🎉 ! Now, we will take a look on your
   contribution and merge it if everything is ok 👀 Meanwhile, you can join our
   [Discord community](https://discord.gg/5QKpGqR), we love talking with our
   contributors and users !


## Guidelines

!!! warning
    Following these guidelines is required to contribute in
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository

Each jobs must:

* [ ] Be compliant with [job structure](/job-structure/)
* [ ] Use the `image` option. Goal is to provide **plug and play** jobs working in
  any environments thanks to containers
* [ ] Use Docker image with a fixed tag. It shouldn't be `latest` or any tag that
  will be overwritten
* [ ] Use fixed versions to retrieves external tools
* [ ] Use only resource with license compatible with the job licence and permits to
  anyone to use it
* [ ] Pass our Continuous Integration pipeline which includes security check jobs
  (pipeline will be run automatically inside your fork)
* [ ] Be compliant with [our job definition](/r2bulary/#job)


## Best practices

!!! info
    Following these best practices is recommended to contribute in
    [R2Devops/hub](https://gitlab.com/r2devops/hub/) repository

### Job variables

* Declare variables using uppercase
* Variables naming convention (to be defined, should we require the job name uppercase as prefix for all variables ? Think about a way to verify variables in hub pipeline and permit various configuration for on-premise #231)

### Choose the best docker image

* Check if there is an image dedicated for the tool to run in the job
    * Check if the image is official (+++)
    * Check if the image is maintained (++)
    * Check if the image is largely used (++)
    * Check if the image is efficient to run the job (++) *difficult to check for the user*
    * Check if the image use the latest version of the tool (how to check it automatically)(+)
    * Check the size (smallest is the best, it should only contain essential tools, KISS) (+)
    * Check if the image has versioning (not only latest) (-)
* If no, check if there is an image already setup for the language of the tool (python, node, go...)
    * Check if the image is official (+++)
    * Check if the image is maintained (++)
    * Check if the image is largely used (++)
    * Check if the image is efficient to run the job (++) *difficult to check for the user*
    * Check the size (smallest is the best, it should only contain essential tools, KISS) (+)
    * Check if the image has versioning (not only latest) (-)
    * Install the tool in the image using package manager (fixed version)
* If no, use docker alpine and install tool in it. If the installation is too long in the job: create your own image (fixed version)



### About versions:

> The installed version of Doxygen must be specified as variable with the default value on the current latest version 1.8.18-r0
> A fixed tag must be specified for the alpine image used

### Compliance with another job

* Compliance with another job


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

* Use expose_as like in mkdocs job to expose the artifact in the MR
> integration in MR widget ? expose_as ?
> artifact retention


### About compliance with pages job:

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


### Job definition of done

TODO


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


### Continuous integration pipeline

TODO: describe our CI/CD pipeline


### TODO

* Stage list in job file with only one stage: the one of the job
* Add contact us at each blocking issue points
