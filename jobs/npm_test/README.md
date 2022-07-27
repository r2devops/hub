## Objective

This job will run a predefined `test` command that can be specified in the `package.json` configuration file


## How to use it

1. Make sure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the required `test` command in the `scripts` object
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
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
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |


## Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](https://r2devops.io/_/r2devops-bot/npm_install)


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
