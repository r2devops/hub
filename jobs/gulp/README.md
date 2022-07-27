## Objective

This job installs `npm` or `yarn` dependencies listed in your `package.json` and installs
 gulp to run your tasks.

## How to use it

1. Ensure that your project have
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the requirements
1. Ensure that your project have
   [`gulpfile.js`](https://gulpjs.com/docs/en/getting-started/javascript-and-gulpfiles/#gulpfile-explained){:target="_blank"}
   or
   [`gulpfile.ts`](https://gulpjs.com/docs/en/getting-started/javascript-and-gulpfiles/#transpilation){:target="_blank"}
   file which contains your tasks
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀


## Example of `.gitlab-ci.yml` file

If you want to [change the default stage](/use-the-hub/#use-custom-stage), or [customize your job](/use-the-hub/#global) have a look on the example below 👇🏽

```yaml
stages:
  - prepare-frontend

include:
  - remote: 'https://jobs.r2devops.io/gulp.yml'

gulp:
  stage: prepare-frontend
  variables:
    PROJECT_ROOT: "frontend/"
    GULP_TASKS: "generate-fonts; minify-css; minify-js; "
    GULPFILE_PATH: "config/gulpfile.js"
```

## Variables

!!! note
    All paths defined in variables are relative and starts from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `GULP_VERSION` <img width=105/>| Version of Gulp to use  | `2.3.0` |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `PACKAGE_MANAGER` | Package manager to install your dependencies `npm` or `yarn`  | `npm` |
| `INSTALL_OPTIONS` | Additional options for the installation of `PACKAGE_MANAGER` <br/> *Ex: For npm `--save-dev`*  | ` ` |
| `GULPFILE_PATH` | Path (from `PROJECT_ROOT`) to your  gulpfile `gulpfile.js` or `gulpfile.ts`| ` ` |
| `GULP_TASKS` | List of your tasks to run with `gulp` (separated by ; ). <br/> *Ex: "minify-css; minify-js;"* | ` ` |
| `GULP_OUTPUT_FOLDER` | If needed, path to the output produced by your scripts (path relative from the `PROJECT_ROOT`) | `build` |
| `PAGES_DEPLOY` | If enabled, prepare your build result to be deployed on pages (require [pages job](jobs/deploy/pages/)) | `false` |
| `PAGES_FOLDER` | Path where to copy the output to be exposed for deployment on [pages](jobs/deploy/pages/) (path relative from the root of the repository) | `./website_build` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

## Artifacts

When the job is successful, Gulp result is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `gulp artifact` in merge requests.
    Exposition of artifact currently works only if you keep `PROJECT_ROOT` and
    `GULP_OUTPUT_FOLDER` default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)
