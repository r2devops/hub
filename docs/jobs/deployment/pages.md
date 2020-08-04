# 🦊 Pages

## Description

Publish HTML documentation located in `public` folder, retrieved as an artifact
from previous job named `documentation`.

## How to use it

!!! note "Requirements"
    * Use a `documentation` job in build 📦 stage to be able to retrieve the
      documentation to publish as artifact. Example: [Mkdocs](/jobs/mkdocs/)

1. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/pages.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)

5. Well done, your job is ready to work ! 😀


## Job details

* Job name: `pages`
* Docker image: [`ruby`](https://hub.docker.com/_/ruby)
* Stage: `deployment`
* When: only run on `master` branch

### Variables:

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
