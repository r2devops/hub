## Objective

This job installs `composer` dependencies listed in your `composer.lock` or `composer.json` and exposes the folder
`vendor` as cache to other jobs of your pipeline. It allows you to run
`composer install` only once in your pipeline.


## How to use it

!!! info
    If you don't have `composer.lock`, the job will look for `composer.json` and use it instead


1. Ensure that your project has
   [`composer.lock`](https://getcomposer.org/doc/01-basic-usage.md#installing-with-composer-lock){:target="_blank"}
   file which contains the dependencies and their exact versions
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀


!!! info
    On Gitlab, this job will be run in the default first stage of your
    pipeline: [`.pre`](https://docs.gitlab.com/ee/ci/yaml/#pre-and-post)
    For this reason, using only this job in your pipeline will not trigger a pipeline in Gitlab.
    You have to add additional jobs.

## Variables

!!! note
    All paths defined in variables are relative and starts from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `composer.lock`  | `.` |
| `COMPOSER_INSTALL_OPTIONS` | Additional options for `composer install` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `7.3`  |


## Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `$PROJECT_ROOT/vendor`
* If `composer install` produces different result than the cached content

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html){:target="_blank"}.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
