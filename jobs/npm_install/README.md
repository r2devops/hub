## Objective

This job installs `npm` dependencies listed in your `package-lock.json` and exposes
`node_modules` as cache to other jobs of your pipeline. It allows you to run
`npm install` only once in your pipeline.


## How to use it

!!! info
    If you don't have `package-lock.json`, the job will look for `package.json` and use it instead

1. Ensure that your project have
   [`package-lock.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-lock-json){:target="_blank"}
   file which contains the requirements  
2. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/npm_install.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to be used ! 😀


## Job details

!!! info
    On Gitlab, this job will be run in the default first stage of your
    pipeline: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)

    ⚠️ For this reason, using only this job in your pipeline will not trigger a pipeline in Gitlab.
    You have to add additional jobs.

* Job name: `npm_install`
* Default stage: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables


| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative path to the directory containing `package.json` (**see warning below**)  | ` ` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_USE_CI` | Enable usage of `npm ci` instead of classic `npm install` | `true` |

!!! warning
    In the case you are updating `PROJECT_ROOT` and you want to have a properly working cache,
    consider making this variable a global variable in the root of your `.gitlab-ci.yml`. Learn how
    easy it is [here](https://docs.gitlab.com/ee/ci/variables/#create-a-custom-cicd-variable-in-the-gitlab-ciyml-file).

### Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Each branch has its own version
* Cached directory is `$PROJECT_ROOT/node_modules`
* If `package.json` or `package-lock.json` is edited, the cache is updated

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)