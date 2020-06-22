# 📗 Mkdocs

## Description

Build HTML documentation form Markdown source using
[Mkdocs](https://www.mkdocs.org/) and deploy it on Gitlab pages. All
requirements to use [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/) are installed.

## How to use it

1. Prepare your project with Mkdocs configuration file and sources files as
   described in [Mkdocs documentation](https://www.mkdocs.org/#getting-started)
2. Choose a version in [version list](#versions)
3. Add the corresponding url to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://gitlab.com/go2scale/jobs/-/raw/2020-06-22_1/Jobs/mkdocs/mkdocs.yml'
    ```

4. If you need set variables in jobs, use `variables` option in
   `.gitlab-ci.yml` file

## Jobs

### Documentation

Build HTML documentation from Makdown source using `Mkdocs`.

* Docker image:
[squidfunk/mkdocs-material](https://hub.docker.com/r/squidfunk/mkdocs-material)
* When: always
* Stage: build
* Artifacts:
    * Result of documentation build exposed as `Documentation`
* Variables:

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DOCUMENTATION_DISABLE` | Disable build | |


### Pages

* Docker image: [ruby](https://hub.docker.com/_/ruby)
* When: only run on `master` branch
* Stage: production
* Artifacts:
    * Result of documentation from previous job. It's used as input for Gitlab
      pages
* Variables:

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DOCUMENTATION_DISABLE` | Disable publication on Gitlab pages| |
| `PAGES_DISABLE` | Disable publication on Gitlab pages | |

## Versions

### Latest

```
https://gitlab.com/go2scale/jobs/-/raw/master/Jobs/mkdocs/mkdocs.yml
```

### Tag `2020-05-31_1`

!!! warning
    This update introduces breaking changes. Follow [this
    guide](https://squidfunk.github.io/mkdocs-material/releases/5/#how-to-upgrade)
    to know how to upgrade.

```
https://gitlab.com/go2scale/jobs/-/raw/2020-05-31_1/Jobs/mkdocs/mkdocs.yml
```

* Upgrade Material for Mkdocs to v5

