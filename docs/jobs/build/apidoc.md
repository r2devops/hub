# 📒 ApiDoc

## Description

Creates a versioned HTML documentation from API annotations in your source
code using [apiDoc](https://www.apidocjs.com/).

## How to use it

1. Prepare your project with API annotations in your source code following
   [apiDoc format](https://apidocjs.com/#examples) and your [apiDoc
   configuration file](https://apidocjs.com/#configuration).
2. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/apidoc.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `apidoc`
* Docker image:
[`node`](https://hub.docker.com/r/_/node)
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `APIDOC_VERSION` | Version of apiDoc to use | `0.24.0` |
| `APIDOC_CONFIG_PATH` | Path to config file or to directory containing config file (apidoc.json or apidoc.config.js) | `.` |
| `APIDOC_OUTPUT_PATH` | Output directory path | `/documentation_build` |
| `APIDOC_TEMPLATE_PATH` | Path to template folder | `/usr/lib/node_modules/apidoc/template/` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as) `apiDoc build` in
merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129). As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.

## Versions

* **Latest** (current -> `2020-08-09_1`) : `https://jobs.go2scale.io/latest/apidoc.yml`
* **Tag `2020-08-09_1`** : `https://jobs.go2scale.io/2020-08-09_1/apidoc.yml`
    * Rename the job from `documentation` to `apidoc`
    * Update the default output folder to `/documentation_build` in order to
      ensure plug and play compatibility with [pages](/jobs/deployment/pages)
      deployment job. **Note**: output folder can be customized using
      `APIDOC_OUTPUT_PATH` [variable](#variables)
* **Tag `2020-08-07_1`** : `https://jobs.go2scale.io/2020-08-07_1/apidoc.yml`
    * Initial version
