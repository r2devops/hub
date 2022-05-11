## Objective

Creates a versioned HTML documentation from API annotations in your source
code using [apiDoc](https://apidocjs.com/){:target="_blank"}.

## How to use it

1. Prepare your project with API annotations in your source code following
   [apiDoc format](https://apidocjs.com/#examples){:target="_blank"} and your [apiDoc
   configuration file](https://apidocjs.com/#configuration){:target="_blank"}.
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `apidoc`
* Docker image:
[`node:18.1-alpine3.14`](https://hub.docker.com/r/_/node){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

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

### Artifacts

When the job is successful, the build of your documentation is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `apiDoc Build` in merge requests.
    Exposition of artifact currently works only if you keep `APIDOC_OUTPUT_PATH`
    default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)