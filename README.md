# g2s hub

## Description

**g2s hub** is a collaborative hub of CI & CD
ready to use jobs which helps you to quickly build powerful pipelines for your
projects.

Each jobs of the hub can be used unitary or to create fully customs pipelines.
You can use them for any kind of software and deployment type. Each job can be
customized through configuration.

Check the [documentation](https://go2scale.gitlab.io/jobs/).

## How to work on the documentation

### Requirements

Documentation is built using [Mkdocs](https://www.mkdocs.org) and [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/).

Make sure that `python` and `pip` are installed on your system. Then install
all required components:

```shell
pip install mkdocs-material mkdocs-minify-plugin mkdocs-git-revision-date-localized-plugin mkdocs-awesome-pages-plugin pymdown-extensions
```

### Clone the repository

Clone the repository locally

```shell
git clone git@gitlab.com:go2scale/jobs.git
cd jobs
```

### Launch Mkdocs

You can launch mkdocs in order to create a local web server with hot reload to
see your updates in live

```shell
mkdocs serve
```
