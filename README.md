# R2Devops Hub

## Description

**R2Devops hub** is a collaborative hub of CI & CD **ready to use** jobs which
helps you to quickly build powerful pipelines for your projects.


Each jobs of the hub can be used independently or to create fully **customized pipelines.**
You can use them for any kind of software and deployment type. Each job can be
customized through configuration.

* **🚀 Find jobs to use in your pipeline in [Jobs index](https://r2devops.io/_/jobs/)**
* **📚 Understand how to use the hub in [Documentation](https://docs.r2devops.io/)**
* **🙋 Add your own job using the [Contributing guide](https://docs.r2devops.io/public-catalog/contribute)**

## Repository

This mono-repo contains several parts:

* Jobs' sources and a job template (jobs structure is described in [documentation](https://docs.r2devops.io/public-catalog/contribute/#template-definition))
* Documentation of the hub
* Tools used in hub pipeline to check jobs

```
.
├── docs            # Documentation sources
├── jobs            # Folder containing jobs sources
│   └── ...
├── mkdocs.yml      # Documentation configuration
├── Pipfile         # Pipenv dependency file to build doc
├── Pipfile.lock
└── tools           # Folder containing tools
    └── ...
```

### How to add or update a job

* Follow the [Contributing guide](https://docs.r2devops.io/public-catalog/contribute)

### How to update the hub documentation

As prerequisites, you need to install following dependencies on your system:

* `python3`
* `pipenv`

1. Clone the repository locally

```shell
git clone git@gitlab.com:r2devops/hub.git
cd hub
```

2. Install requirements

Documentation is built using [Mkdocs](https://www.mkdocs.org) and [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}.

```shell
pipenv install
```

3. Launch Mkdocs

You can launch mkdocs in order to create a local web server with hot reload to
see your updates in live:

```shell
pipenv run mkdocs serve
```

4. See your update in live at [https://localhost:8000](https://localhost:8000)

### CI/CD Pipeline

This file aims to explain all jobs used on the CI/CD pipeline.

#### Jobs & stages

There are several jobs used on the CI/CD pipeline. The following list shows all jobs and their purpose. The jobs are executed in the order they are listed.

##### Static_tests


1. `ci_linter`  
This jobs use the [CI lint API](https://docs.gitlab.com/ee/api/lint.html) to validate the configuration of each jobs.yaml file. 

2. `job_structure`  
This job written in Python ensures every files respect the structure we want. It checks that every file has the right name, the right path and the right content. 

3. `job_customs`  
This job written in Python ensures every script of the jobs doesn't made modifications on the repository. It checks that every script doesn't use `git commit` or `git push`.

4. `job_image_scan`  
Runs only on the default branch. And uses some cache for the images.
This job uses [trivy](https://aquasecurity.github.io/trivy/) to scan all images used in the jobs. It checks that the image doesn't have any vulnerability.

5. `code_spell`
This job uses codespell to check the spelling of the code. It checks that the code doesn't have any spelling mistake.

6. `links_checker`
This job ensures all links are valid in the documentation.

#### merge_test & scheduled pipeline

A scheduled pipeline is triggered at 8 pm each day to launch a full antivirus scan on each jobs. 
This pipeline triggers 3 jobs :  

1. `refresh_job_av_database`   
Refresh antivirus definition's with `freshclam` command. See the [english documentation(https://help.ubuntu.com/community/ClamAV)(english) or [french documentation](https://doc.ubuntu-fr.org/clamav) for more information.
2. `generate_job_av`  
This job is only trigger when a branch is being merged or on a schedule pipeline. Iterates over the jobs to get their image and write a .gitlab-ci.yml that can run a child pipeline in order to use ClamAV for virus detection. The generated .gitlab-ci.yml is launched in the next job.
3. `child_job_av`   
It is launched by the previous job and scan the docker image and warn if they are know virus listed in the database.

#### project_setup

1.`job_gitlab_labels`   
This job retrieve all labels in the project and see if each job has it's own label. If not, it creates it and assign it to the job.


#### deploy

1. `release`  
This job is like a swiss knife ⚒️ and performs many action.  
First, it creates a new release within GitLab and print the `CHANGELOG` of the created/updated job in the release description.  
Then, it sends a discord notification to the `#updates` channel.  


### How to update hub tools

#### Guidelines

For `python` tools:

* Pylint note >= 9
* Usage of logging
* Usage of argparse when args are required
* [`Format`](https://docs.python.org/3/library/functions.html?highlight=format#format) must be used instead of `%s` or string concatenation with `+`
* Docstring format compliant with [Google styleguide](https://google.github.io/styleguide/pyguide.html#244-decision)

#### Requirements

Each tools have their own `Pipfile` in their folder to manage their
dependencies. You must install `pipenv` to work on them:

```shell
pip install pipenv
```
