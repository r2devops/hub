## Objective

This job will run a predefined `test` command that can be specified in the `package.json` configuration file


## How to use it

1. Make sure that your project has
   [`package.json`](https://yarnpkg.com/configuration/manifest){:target="_blank"}
   file which contains the required `test` command in the `scripts` object
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the
   [jobs customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀


## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `YARN_INSTALL_OPTIONS` | Additional options for `yarn install` | ` ` |
| `YARN_TEST_OPTIONS` | Additional options for `yarn test` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |


## Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](https://r2devops.io/_/gitlab/r2devops/hub/npm_install/#cache)



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Totara-thib](https://gitlab.com/Totara-thib)
