## Objective

This job will run a predefined `test` command specified in the scripts section of the `package.json` configuration file

## How to use it

1. Make sure that your project has `package.json` file which contains the required `test` command in the `scripts` object.
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀

## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `PNPM_INSTALL_OPTIONS` | Additional options for `pnpm install` | ` ` |
| `PNPM_TEST_COMMAND` | The command to run test specified in your `package.json` | `test` |
| `PNPM_TEST_OPTIONS` | Additional options for `pnpm test` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `20-buster`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)