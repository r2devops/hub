## Objective

This job allows users to run several scripts from their `package.json` file using `npm`. Scripts can be used with args.


## How to use it

1. Make sure that your project has 
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains predefined command in the `scripts` object
1. If you want the job to run scripts make sure to add them inside the `variable` `NPM_SCRIPTS` and separate every command with `;`
1. The default stage is `others`, if you want to customize this stage depending of the scripts that you run, check the [stage
   customization](/use-the-hub/#use-custom-stage)
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. You are done, the job is ready to use ! 😉


## Job details

* Job name: `npm_scripts`
* Default stage: `others`
* Docker image: [`node:18-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_SCRIPTS` | Value of several scripts specified in `package.json` that can be separated by `;` | ` ` |
| `NPM_OUTPUT` | Path to the output send by script specified in `package.json` | ` ` |

### Example to use several scripts

Following example of `.gitlab-ci.yml` file describes how to enable Gitlab pages
deployment using this job:

#### Scripts in Package.json
```yaml
  "scripts": {
    "build": "ng build",
    "lint": "ng lint"
  }
```
#### .gitlab-ci
```yaml
stages:
  - others

include:
  - remote: 'https://jobs.r2devops.io/npm_scripts.yml'

npm_scripts:
  variables:
    NPM_SCRIPTS: "build;lint"
```

### Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](/jobs/others/npm_install/#cache)



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@totara-thib](https://gitlab.com/Totara-thib)