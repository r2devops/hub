# R2Devops Hub

## Description

**R2Devops hub** is a collaborative hub of CI & CD **ready to use** jobs which
helps you to quickly build powerful pipelines for your projects.


Each jobs of the hub can be used independently or to create fully **customized pipelines.**
You can use them for any kind of software and deployment type. Each job can be
customized through configuration.

* **🚀 Find jobs to use in your pipeline in [Jobs index](https://r2devops.io/jobs/)**
* **📚 Understand how to use the hub in [Documentation](https://r2devops.io)**
* **🙋 Add your own job using the [Contributing guide](https://r2devops.io/how-to-contribute/)**

## Repository

This mono-repo contains several parts:

* Jobs' sources and a job template (jobs structure is described in [documentation](https://r2devops.io/job-structure/))
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

* Follow the [Contributing guide](https://r2devops.io/how-to-contribute/)

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

### How to update hub tools

#### Guidelines

For `pyhton` tools:

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
