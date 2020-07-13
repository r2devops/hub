# 📦 Mkdocs

## Description

Build HTML documentation form Markdown source using
[Mkdocs](https://www.mkdocs.org/). All requirements to use [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/) are ready to use.

## How to use it

1. Prepare your project with Mkdocs configuration file and sources files as
   described in [Mkdocs documentation](https://www.mkdocs.org/#getting-started)
2. Choose a version in [version list](#versions)
3. Add the corresponding url to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://gitlab.com/go2scale/hub/-/raw/latest/Jobs/mkdocs/mkdocs.yml'
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


## Versions

* **Latest** : `https://gitlab.com/go2scale/jobs/-/raw/master/Jobs/mkdocs/mkdocs.yml`
* **Tag `2020-07-13_1`** : `https://gitlab.com/go2scale/hub/-/raw/2020-07-31_1/Jobs/mkdocs/mkdocs.yml`

    !!! warning
        Since this version, `pages` job, which publish documentation on Gitlab
        pages, isn't included anymore. It's now a dedicated job:
        [pages](Jobs/pages).

* **Tag `2020-05-31_1`** : `https://gitlab.com/go2scale/hub/-/raw/2020-05-31_1/Jobs/mkdocs/mkdocs.yml`

    !!! warning
        This update introduces breaking changes. Follow [this
        guide](https://squidfunk.github.io/mkdocs-material/releases/5/#how-to-upgrade)
        to know how to upgrade.
    * Upgrade Material for Mkdocs to v5



