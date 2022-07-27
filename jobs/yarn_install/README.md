## Objective

This job installs `yarn` dependencies listed in your `package.json` and exposes
`node_modules` as cache to other jobs of your pipeline. It allows you to run
`yarn install` only once in your pipeline.


## How to use it

1. Ensure that your project have
   [`package.json`](https://classic.yarnpkg.com/en/docs/package-json/){:target="_blank"}
   file which contains the requirements
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀


    You have to add additional jobs.

* Job name: `yarn_install`
* Default stage: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)
* Docker image: [`node:18-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative path to the directory containing `package.json` (**see warning below**)  | ` ` |
| `YARN_INSTALL_OPTIONS` | Additional options for `yarn install` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

!!! warning
    In the case you are updating `PROJECT_ROOT` and you want to have a properly working cache,
    consider making this variable a global variable in the root of your `.gitlab-ci.yml`. Learn how
    easy it is [here](https://docs.gitlab.com/ee/ci/variables/#create-a-custom-cicd-variable-in-the-gitlab-ciyml-file).

## Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Each branch has its own version
* Cached directory is `$PROJECT_ROOT/node_modules`
* If `package.json` or `yarn.lock` is edited, the cache is updated

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)
