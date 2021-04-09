## Objective

This job will run a predefined `test` command that can be specified in the `package.json` configuration file


## How to use it

1. Make sure that your project has 
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the required `test` command in the `scripts` object
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/npm_test.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. You are done, the job is ready to use ! 😉


## Job details

* Job name: `npm_test`
* Default stage: `static_tests`
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_TEST_OPTIONS` | Additional options for `npm test` | ` ` |


### Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](/jobs/others/npm_install/#cache)