# R2Devops Hub

## Description

**R2Devops hub** is a collaborative hub of CI & CD **ready to use** jobs which
helps you to quickly build powerful pipelines for your projects.


Each jobs of the hub can be used independently or to create fully **customized pipelines.**
You can use them for any kind of software and deployment type. Each job can be
customized through configuration.

Check the [Documentation](https://r2devops.io) 📚 and [Jobs
index](https://r2devops.io/jobs/) 🚀

## Repository

This mono-repo contains several parts:

* Documentation sources
* Jobs
* Tools
    * Builder: build the jobs' documentation
    * Notify: send notification about jobs' updates to our [discord server](https://discord.gg/5QKpGqR)
    * Template: job template

```
.
├── docs                            # Documentation sources
├── jobs                            # Folder containing jobs sources
│   ├── docker_build
│   │   ├── docker_build.yml        # Job content
│   │   ├── job.yml                 # Job metadata
│   │   ├── README.md               # Job documentation
│   │   └── versions                # Jobs changelogs
│   │       ├── 0.1.0.md
│   │       └── ...
│   └── ...
├── mkdocs.yml                      # Documentation configuration
├── Pipfile                         # Pipenv dependency file to build doc
├── Pipfile.lock
├── requirements.txt                # Python dependency file to build doc
└── tools                           # Folder containing tools
    ├── builder
    │   ├── builder.py
    │   ├── Pipfile
    │   ├── Pipfile.lock
    │   └── templates
    ├── job_template
    └── notify
        ├── discord_release_notify.py
        ├── Pipfile
        └── Pipfile.lock
```

## How to update the documentation

### Clone the repository

Clone the repository locally

```shell
git clone git@gitlab.com:r2devops/hub.git
cd hub
```

### Requirements

Documentation is built using [Mkdocs](https://www.mkdocs.org) and [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"}.

You can use `pipenv` or `pip` to install python requirements:

* Using `pipenv`

    ```shell
    pipenv install
    pipenv shell
    ```

* OR using `pip`

    ```shell
    pip install -r requirements
    ```

🚨 Take care to update both `Pipfile` and `requirements.txt` when you modify
dependencies.

### Launch Mkdocs

You can launch mkdocs in order to create a local web server with hot reload to
see your updates in live:

```shell
mkdocs serve
```

## How to update tools

### Requirements

Each tools have their own `Pipfile` in their folder to manage their
dependencies. You must install `pipenv` to work on them:

```shell
pip install pipenv
```

### Work on `builder`

```shell
cd tools/builder
pipenv install
pipenv shell
```

### Work on `notify`

```shell
cd tools/notify
pipenv install
pipenv shell
```
