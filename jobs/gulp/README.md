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
1. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/gulp.yml'
    ```

1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀


### Example of `.gitlab-ci.yml` file

If you want to [change the default stage](/use-the-hub/#change-the-default-stage-of-job), or [customize your job](/use-the-hub/#global) have a look ont the example below 👇🏽

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

## Job details

* Job name: `gulp`
* Default stage: `others`
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

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
