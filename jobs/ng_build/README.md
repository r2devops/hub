## Objective

Compiles an Angular app into an output directory named dist/ at the given output path. Must be executed from within a workspace directory.
The application builder uses the webpack build tool, with default configuration options specified in the workspace configuration file (angular.json) or with a named alternative configuration. Check the [Angular documentation](https://angular.io/cli/build){:target="_blank"} if you need more information.

## How to use it

1. Ensure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the script required to build (`build` by default)
1. You should specify your project name in the `PROJECT_NAME` variable, you can find it in your `angular.json` file under the `projects` section. You don't have to go through this step if there is a `defaultProject` value in your `angular.json` because the `ng build` command will be executed on the  `defaultProject`.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Path to the root of project. <img width=175/> | `.` <img width=100/> |
| `PROJECT_NAME`  | Project name specified in the `projects` section of the `angular.json` workspace configuration file. If no `PROJECT_NAME` have been specified it will execute the `ng build` command on the `defaultProject` specified in the `angular.json` file. | ` `  |
| `NG_BUILD_OPTIONS`  | Additional options available for the user, they are added at the end of build command. Check the different options in the official [documentation](https://angular.io/cli/build){:target="_blank"}.  | ` `  |
| `OUTPUT_PATH`  | Path to the output produced by the `ng` build script used (path relative from the `PROJECT_ROOT`) | `website_build/`  |
| `IMAGE_TAG` | The default tag for the docker image | `16.13.1-buster`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
