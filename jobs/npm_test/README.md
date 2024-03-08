## Objective

This job will run a predefined `test` command that can be specified in the `package.json` configuration file


## How to use it

1. Make sure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the required `test` command in the `scripts` object
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. You are done, the job is ready to use ! 😉


## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_TEST_OPTIONS` | Additional options for `npm test` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `20-buster`  |


## Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](https://r2devops.io/_/r2devops-bot/npm_install)


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
