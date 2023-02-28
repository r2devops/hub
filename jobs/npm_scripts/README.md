## Objective

This job allows users to run several scripts from their `package.json` file using `npm`. Scripts can be used with args.


## How to use it

1. Make sure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains predefined command in the `scripts` object
1. If you want the job to run scripts make sure to add them inside the `variable` `NPM_SCRIPTS` and separate every command with `;`
1. The default stage is `others`, if you want to customize this stage depending of the scripts that you run, check the [stage
   customization]((https://docs.r2devops.io/get-started/use-templates/#use-a-template))/#use-custom-stage)
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. You are done, the job is ready to use ! 😉


## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_SCRIPTS` | Value of several scripts specified in `package.json` that can be separated by `;` | ` ` |
| `NPM_OUTPUT` | Path to the output send by script specified in `package.json` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

## Example to use several scripts

Following example of `.gitlab-ci.yml` file describes how to enable Gitlab pages
deployment using this job:

### Scripts in Package.json
```yaml
  "scripts": {
    "build": "ng build",
    "lint": "ng lint"
  }
```
### .gitlab-ci
```yaml
stages:
  - others

include:
  - remote: 'https://jobs.r2devops.io/npm_scripts.yml'

npm_scripts:
  variables:
    NPM_SCRIPTS: "build;lint"
```

## Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](https://r2devops.io/_/gitlab/r2devops/hub/npm_install/#cache)



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@totara-thib](https://gitlab.com/Totara-thib)
