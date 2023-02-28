## Objective

Deploy your static website on a Clever Cloud application.

## How to use it

1. On your computer, install the Clever Cli and login into your account by following the [documentation](https://www.clever-cloud.com/doc/getting-started/cli/) .
1. Retrieve your secret in the file `~/.config/clever-cloud` and set variables `CLEVER_TOKEN` and `CLEVER_SECRET` in the GitLab CI/CD variables section of your project.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `CLEVER_BUILD_PATH` <img width=100/> | Path to folder which contains the static website files to publish <img width=175/>| `website_build` <img width=100/>|
| `CLEVER_APP` | Name of the application | `$CI_PROJECT_PATH_SLUG` |
| `CLEVER_TOKEN` | ⚠️ Mandatory variable. The clever token used for authentication. This variable should be specified in GitLab > CI/CD Settings. | ` ` |
| `CLEVER_SECRET` | ⚠️ Mandatory variable. The clever secret used for authentication. This variable should be specified in GitLab > CI/CD Settings. | ` ` |
| `CLEVER_PACKAGE_VERSION` | The version of the npm packages [clever-tools](https://gitlab.com/r2devops/hub/-/blob/latest/npmjs.com/package/clever-tools) | `2.9.1` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster` |

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)
