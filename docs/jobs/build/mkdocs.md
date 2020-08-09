# 📃 Mkdocs

## Description

Build HTML documentation form Markdown source using
[Mkdocs](https://www.mkdocs.org/). All requirements to use [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/) are ready to use.

## How to use it

1. Prepare your project with Mkdocs configuration file and sources files as
   described in [Mkdocs
   documentation](https://www.mkdocs.org/#getting-started). In your repository,
   documentation files must be organized as follows:

    ```
    /mkdocs.yml # This is your configuration file
    /docs/      # This folder contains all your documentation markdown files
    ```
2. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/mkdocs.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `mkdocs`
* Docker image:
[`squidfunk/mkdocs-material`](https://hub.docker.com/r/squidfunk/mkdocs-material)
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `MKDOCS_OUTPUT_PATH` | Output directory path | `/ documentation_build` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as) `Documentation` in
merge requests

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129). As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.

## Versions

* **Latest** (current -> `2020-08-09_1`) : `https://jobs.go2scale.io/latest/mkdocs.yml`
* **Tag `2020-08-09_1`** : `https://jobs.go2scale.io/2020-08-09_1/mkdocs.yml`
    * Rename the job from `documentation` to `mkdocs`
    * Update the default output folder to `/documentation_build` in order to
      ensure plug and play compatibility with [pages](/jobs/deployment/pages)
      deployment job. **Note**: output folder can be customized using
      `MKDOCS_OUTPUT_PATH` [variable](#variables)
* **Tag `2020-08-05_1`** : `https://jobs.go2scale.io/2020-08-05_1/mkdocs.yml`

    !!! warning
        Since this version, `pages` job, which publish documentation on Gitlab
        pages, isn't included anymore. It's now a dedicated job:
        [pages](Jobs/pages).

* **Tag `2020-05-31_1`** (legacy): `https://gitlab.com/go2scale/hub/-/raw/2020-05-31_1/jobs/documentation.gitlab-ci.yml`

    !!! warning
        This update introduces breaking changes. Follow [this
        guide](https://squidfunk.github.io/mkdocs-material/releases/5/#how-to-upgrade)
        to know how to upgrade.
    * Upgrade Material for Mkdocs to v5

* **Tag `2020-05-31_1`** (legacy): `https://gitlab.com/go2scale/hub/-/raw/2020-05-05_3/jobs/documentation.gitlab-ci.yml`

    * Initial version
