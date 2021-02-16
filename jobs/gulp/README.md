## Objective

This job installs `npm` or `yarn` dependencies listed in your `package.json` and installs
 gulp to run your tasks.
It exposes `node_modules` as cache to other jobs of your pipeline. It allows you to run
`npm install` only once in your pipeline.

## How to use it

1. Ensure that your project have
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the requirements
1. Ensure that your project have
  [`gulpfile.js`](https://gulpjs.com/docs/en/getting-started/javascript-and-gulpfiles/#gulpfile-explained){:target="_blank"} or [`gulpfile.ts`](https://gulpjs.com/docs/en/getting-started/javascript-and-gulpfiles/#transpilation){:target="_blank"} file which contains your tasks
1. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:
    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/gulp.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀


### Example of .gitlab-ci.yml file

If you want to [change the default stage](/use-the-hub/#change-the-default-stage-of-job), or [customize your job](/use-the-hub/#global) have a look ont the example below 👇🏽

```yaml
stages:
  - prepare-frontend

include:
  - remote: 'https://jobs.r2devops.io/gulp.yml'

gulp:
  variables:
    PROJECT_ROOT: "frontend/"
    GULP_TASKS: "generate-fonts; minify-css; minify-js; "
    GULPFILE_PATH: "config/gulpfile.js"
```



## Job details

!!! info
    On Gitlab, this job will run `npm_install` in the default first stage of your
    pipeline: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)


* Job name: `gulp`
* Default stage: [`others`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

!!! note
    All paths defined in variables are relative and starts from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=70/>| Path to the directory containing `package.json`  | `.` |
| `PACKAGE_MANAGER` | Package manager to install your dependencies `npm` or `yarn`  | `npm` |
| `INSTALL_OPTIONS` | Additional options for the installation of `PACKAGE_MANAGER` <br/> *Ex: For npm `--save-dev`*  | ` ` |
| `GULPFILE_PATH` | Path (from `PROJECT_ROOT`) to your  gulpfile `gulpfile.js` or `gulpfile.ts`| ` ` |
| `GULP_TASKS` | List of your tasks to run with `gulp` (separated by ; ). <br/> *Ex: "minify-css; minify-js;"* | ` ` |


### Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `$PROJECT_ROOT/node_modules`
* If `npm install` or `yarn install` produces different result than the cached content

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).
