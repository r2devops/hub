# 🦊 Pages

## Description

Publish HTML documentation located in `public` folder, retrieved as an artifact
from previous job named `documentation`.

## How to use it

!!! note "Requirements"
    * Use a `documentation` job in build 📦 stage to be able to retrieve the
      documentation to publish as artifact. Example: [Mkdocs](/jobs/mkdocs/)

1. Choose a version in [version list](#versions)
2. Add the corresponding url to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/pages.yml'
    ```

3. If you need set variables in jobs, use `variables` option in
   `.gitlab-ci.yml` file

## Jobs

### Pages

* Docker image: [ruby](https://hub.docker.com/_/ruby)
* When: only run on `master` branch
* Stage: deployment
* Artifacts:
    * Result of documentation from previous job. It's used as input for Gitlab
      pages
* Variables:

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DOCUMENTATION_DISABLE` | Disable publication on Gitlab pages| |
| `PAGES_DISABLE` | Disable publication on Gitlab pages | |

## Versions

* **Latest** (current -> `2020-05-31_1`): `https://jobs.go2scale.io/latest/pages.yml`
* **Tag `2020-05-31_1`** : `https://jobs.go2scale.io/2020-05-31_1/pages.yml`

    !!! warning
        This update introduces breaking changes. Follow [this
        guide](https://squidfunk.github.io/mkdocs-material/releases/5/#how-to-upgrade)
        to know how to upgrade.
    * Initial version
