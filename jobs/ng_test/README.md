## Objective

This job allows you to run the units tests on Angular project. The `ng test` command builds the application in watch mode, and launches the Karma test runner.

## How to use it

1. Ensure sure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
1. You should specify your project name in the `PROJECT_NAME` variable, you can find it in your `angular.json` file under the `projects` section. You don't have to go through this step if there is a `defaultProject` value in your `angular.json` because the `ng test` command will be executed on the  `defaultProject`.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

!!! info
    If no `PROJECT_NAME` have been specified it will execute the `ng test` command on the `defaultProject` specified in the `angular.json` file.

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the root of project to test  | `.` |
| `PROJECT_NAME` | Project name specified in the `projects` section of the `angular.json` workspace configuration file. | ` ` |
| `NG_TEST_OPTIONS` | Additional options available for the user, they are added just after the test command | ` ` |
| `NG_CODE_COVERAGE` | 	Boolean which define if the script will output a code coverage report. | `true` |
| `IMAGE_TAG` | The default tag for the docker image | `latest`  |


## Cache

To cache `node_modules` folder for other `npm` jobs, take a look at [`npm_install`](https://r2devops.io/_/gitlab/r2devops/hub/npm_install/#cache)


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexiaognard](https://gitlab.com/alexiaognard)
