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

## Guidelines and Best practices

!!! info
    These guidelines are made for R2Devops/hub repository

**TODO**

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














**TODO:**

* Must be compliant with our job definition (see #39) (ex: a job mustn't be a daemon)
    * Ensure that every resource used by the job has a license permitting to anyone to use it without a strong copyleft
* All mandatory files of the [job structure](/structure#job-structure) must be provided
* Provide evidences of job working (url, screenshots, output, ...)
* Job file must be validated by gitlab (CI lint)
* Must be compliant with our security jobs (#230, #229)
* Ensure that every resource used by the job has a license permitting to anyone to use it without a strong copyleft
* Docker image version and version of all tools retrieved must be fixed
    * Tag of the image must be a fixed version (not latest)
    * Any tools used in the image must Docker image version and version of all tools retrieved must be fixed
* Variables naming convention (to be defined, should we require the job name uppercase as prefix for all variables ? Think about a way to verify variables in hub pipeline and permit various configuration for on-premise #231)
* Use expose_as like in mkdocs job to expose the artifact in the MR
* Explain verification pipeline
* Explain in how to use the hub the fact that jobs from the hub run in docker
  containers
* Add contact us at each blocking issue points
