## Objective

A ready-to-use job to lint your Golang project. It includes a lot of linters such as gosimple, errcheck, ... For more information, check the [documentation](https://golangci-lint.run/usage/linters/)

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the
   [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed
   version](#changelog) instead of `latest`.
1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/>  | Path to the root of the project to lint <img width=175/>| `.` <img width=100/>|
| `GOLINT_CONFIG` | Specify whether a [config file](https://golangci-lint.run/usage/configuration/) needs to be used.  | ` ` |
| `GOLINT_REPORTS_DIRECTORY` | Name for the reports directory | `reports` |
| `GOLINT_OUTPUT_FORMAT` | Format for the linters. Could be `junit-xml`, `code-climate` or `colored-line-number` for printing the output in the console.  | `junit-xml` |
| `ADDITIONAL_OPTIONS` | [Additional options](https://golangci-lint.run/usage/configuration/) available for the user, they are added at the end of lint command | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `v1.50.1`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Alexia](https://gitlab.com/alexiaognard). Was improved by [@GridexX](https://gitlab.com/GridexX) on October 2022.
