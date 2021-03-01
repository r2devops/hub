## Objective

This job installs `yarn` dependencies listed in your `package.json` and exposes
`node_modules` as cache to other jobs of your pipeline. It allows you to run
`yarn install` only once in your pipeline.


## How to use it

1. Ensure that your project have
   [`package.json`](https://classic.yarnpkg.com/en/docs/package-json/){:target="_blank"}
   file which contains the requirements
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/yarn_install.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀


## Job details

!!! info
    On Gitlab, this job will be run in the default first stage of your
    pipeline: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)

    ⚠️ For this reason, using only this job in your pipeline will not trigger a pipeline in Gitlab.
    You have to add additional jobs.

* Job name: `yarn_install`
* Default stage: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

!!! note
    All paths defined in variables are relative and starts from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `YARN_INSTALL_OPTIONS` | Additional options for `yarn install` | ` ` |


### Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `$PROJECT_ROOT/node_modules`
* If `yarn install` produces different result than the cached content

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).
