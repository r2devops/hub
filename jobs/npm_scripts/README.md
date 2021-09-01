## Objective

This job will permits users to run several scripts from their `package.json` file using `npm`. Scripts can be used with args.


## How to use it

1. Make sure that your project has 
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains predefined command in the `scripts` object
2. If you want the job to run scripts make sure to add them inside the `variable` `NPM_SCRIPTS` and separate every command with `;`
3. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/npm_scripts.yml'
    ```
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. You are done, the job is ready to use ! 😉


## Job details

* Job name: `npm_scripts`
* Default stage: `others`
* Docker image: [`node:16.8-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `NPM_SCRIPTS` | Value of several scripts specified in `package.json` that can be separated by `;` | ` ` |
| `NPM_OUTPUT` | Path to the output send by script specified in `package.json` | ` ` |


### Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](/jobs/others/npm_install/#cache)
