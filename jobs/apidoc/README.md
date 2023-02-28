## Objective

Creates a versioned HTML documentation from API annotations in your source
code using [apiDoc](https://apidocjs.com/){:target="_blank"}.

## How to use it

1. Prepare your project with API annotations in your source code following
   [apiDoc format](https://apidocjs.com/#examples){:target="_blank"} and your [apiDoc
   configuration file](https://apidocjs.com/#configuration){:target="_blank"}.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `APIDOC_VERSION` <img width=250/> | Version of apiDoc to use <img width=400/> | `0.27.1` |
| `APIDOC_CONFIG_PATH` | Path to config file or to directory containing config file (apidoc.json or apidoc.config.js) | `.` |
| `APIDOC_OUTPUT_PATH` | Output directory path | `website_build/` |
| `APIDOC_TEMPLATE_PATH` | Path to template folder | `/usr/lib/node_modules/apidoc/template/` |
| `APIDOC_SOURCE_PATH` | Path to analyzed folder  | ` ` |
| `APIDOC_INCLUDE_FILTER` | Regex to include specific files | ` ` |
| `APIDOC_EXCLUDE_FILTER` | Regex to exclude specific files | ` ` |
| `APIDOC_OPTIONS` | Additional options | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18.1-alpine3.14`  |

## Artifacts

When the job is successful, the build of your documentation is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `apiDoc Build` in merge requests.
    Exposition of artifact currently works only if you keep `APIDOC_OUTPUT_PATH`
    default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)
