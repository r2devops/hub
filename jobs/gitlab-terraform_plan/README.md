## Objective

This job will initialize a working directory containing Terraform configuration files and prepare your working directory for other terraform commands

!!! info
    By default, this job will run using the default `local` backend, but if you want to use other [remote backends](https://www.terraform.io/docs/language/settings/backends/index.html){:target="_blank"} instead, you need to configure it in advance, check [this](https://www.terraform.io/docs/language/settings/backends/remote.html){:target="_blank"} for more information
## How to use it

1. Make sure that you have your terraform files in your repository
2. Make sure to add your necessary credentials
3. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
5. Well done, your job is ready to work ! 😀

## Variables

!!! info
    All variables can be set using [Gitlab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html) to avoid exposing them in clear in your `.gitlab-ci.yml`. This is **HIGHLY** recommended for sensitive credential variables such as cloud providers tokens and passwords

!!! warning
    This job use `TF_ROOT` which is a global variable and must be defined in your `.gitlab-ci.yml`

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TF_ROOT` | Directory path to terraform files | `${CI_PROJECT_DIR}/terraform` |
| `TF_ADDRESS` | Address to terraform state backend | `${CI_API_V4_URL}/projects/${CI_PROJECT_ID}/terraform/state/main` |
| `INIT_OPTIONS` | Additional options to terraform CLI init | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `v0.20.0`  |

## Artifacts

* The output of the commands will be available as an artifact exposed as `Terraform Plan artifact`

## Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `.terraform/` and file `.terraform.lock.hcl`

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html){:target="_blank"}.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@totara-thib](https://gitlab.com/Totara-thib)
