# 📒 ApiDoc

## Description

Creates a versioned HTML documentation from API annotations in your source
code using [apiDoc](https://www.apidocjs.com/){:target="_blank"}.

## How to use it

1. Prepare your project with API annotations in your source code following
   [apiDoc format](https://apidocjs.com/#examples){:target="_blank"} and your [apiDoc
   configuration file](https://apidocjs.com/#configuration){:target="_blank"}.
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/apidoc.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `apidoc`
* Docker image:
[`node`](https://hub.docker.com/r/_/node){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `APIDOC_VERSION` <img width=250/> | Version of apiDoc to use <img width=400/> | `0.24.0` |
| `APIDOC_CONFIG_PATH` | Path to config file or to directory containing config file (apidoc.json or apidoc.config.js) | `.` |
| `APIDOC_OUTPUT_PATH` | Output directory path | `/documentation_build` |
| `APIDOC_TEMPLATE_PATH` | Path to template folder | `/usr/lib/node_modules/apidoc/template/` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"} `apiDoc build` in
merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}. As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.
