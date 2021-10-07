## Objective

This job will apply all the changes set by `gitlab-terraform_plan` in the file `plan.cache` 

!!! info
    By default, this job will run using the default `local` backend, but if you want to use other [remote backends](https://www.terraform.io/docs/language/settings/backends/index.html){:target="_blank"} instead, you need to configure it in advance, check [this](https://www.terraform.io/docs/language/settings/backends/remote.html){:target="_blank"} for more information
## How to use it

1. Make sure that you have your terraform files in your repository
2. Make sure to add your necessary credentials
3. Make sure that you have created a `plan.cache` file set by `gitlab-terraform_plan`
4. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/gitlab-terraform_apply.yml'
    ```
5. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
6. Well done, your job is ready to work ! 😀

## Job details

* Job name: `gitlab-terraform_apply`
* Docker image:
[`registry.gitlab.com/gitlab-org/terraform-images/releases/1.0:v0.20.0`](https://gitlab.com/gitlab-org/terraform-images)
* Default stage: `deploy`
* When: `always`

### Variables

!!! info
    All variables can be set using [Gitlab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/README.html) to avoid exposing them in clear in your `.gitlab-ci.yml`. This is **HIGHLY** recommended for sensitive credential variables such as cloud providers tokens and passwords

!!! warning
    This job use `TF_ROOT` which is a global variable and must be defined in your `.gitlab-ci.yml`

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TF_ROOT` | Directory path to terraform files | `terraform` |
| `TF_ADDRESS` | Directory path to terraform state files | `terraform` |

### Artifacts

* The output of the commands will be available as an artifact exposed as `Terraform Apply artifact`

### Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `.terraform/` and file `.terraform.lock.hcl`

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html){:target="_blank"}.
