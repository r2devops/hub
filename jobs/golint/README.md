## Objective

A ready-to-use job to lint your Golang project. It includes a lot of linters such as gosimple, errcheck, ... For more informations, check the [documentation](https://golangci-lint.run/usage/linters/)

## How to use it

1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/golint.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `CONFIG_LOCATION` <img width=100/> | Specify whether a config file needs to be used <img width=175/>| ` ` <img width=100/>|
| `PROJECT_ROOT` | Path to the root of project to lint | `.` |
| `ADDITIONAL_OPTIONS` | [Additional options](https://golangci-lint.run/usage/configuration/) available for the user, they are added at the end of test command | ` ` |
| `GOLINT_OUTPUT` | Name of the output file | `report-golint.xml` |
| `IMAGE_TAG` | The default tag for the docker image | `v1.43.0`  |
