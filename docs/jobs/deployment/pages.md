# 🦊 Pages

## Description

Publish HTML documentation located in `public` folder, retrieved as an artifact
from previous job named `documentation`.

## How to use it

!!! note "Requirements"

    You have to use a job which build your documentation in a previous stage.
    We recommend you to use a documentation job available on the HUB in [build
    📦 stage](/jobs/#build). They build documentation and publish it as
    artifact in `documentation_build/` folder.

    **Documentation jobs list:**

    * [ApiDoc](/jobs/build/apidoc/)
    * [Mkdocs](/jobs/build/mkdocs/)

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

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PAGES_BUILD_PATH` | Path to folder which contains documentation build | `documentation_build/` |

## Versions

* **Latest** (current -> `2020-08-05_1`): `https://jobs.go2scale.io/latest/pages.yml`
* **Tag `2020-08-05_1`** : `https://jobs.go2scale.io/2020-08-05_1/pages.yml`

    * Initial version
