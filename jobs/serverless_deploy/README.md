## Objective

This job will help you deploy your serverless resources to AWS using the framework [Serverless.com](https://www.serverless.com/){:target="_blank"}

!!! info
    You can get more information about `serverless deploy` [here](https://www.serverless.com/framework/docs/providers/aws/guide/deploying/){:target="_blank"}

## How to use it

1. Make sure that you have your file `serverless.yml` in the repository
1. Provide the mandatory variables for the job, check [Variables](#variables)
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/serverless_deploy.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `serverless_deploy`
* Docker image:
[`node:15.14-buster`](https://hub.docker.com/r/_/node)
* Default stage: `deploy`
* When: `manual`, only when running on default branch (`$CI_DEFAULT_BRANCH`).
  To update this behavior, see [job customization](https://r2devops.io/use-the-hub/#global) to override [`rules`](https://docs.gitlab.com/ee/ci/yaml/#rulesif)
### Variables

!!! info
    All variables can be set using [Gitlab CI/CD variables](https://docs.gitlab.com/ee/ci/variables/README.html) to avoid exposing them in clear in your `.gitlab-ci.yml`. This is **HIGHLY** recommended for sensible variables such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `SERVERLESS_YAML_DIR` | The path to your `serverless.yml` file | yes | `.` |
| `AWS_ACCESS_KEY_ID` | The access key of your AWS account | yes | ` ` |
| `AWS_SECRET_ACCESS_KEY` | The secret access key of your AWS account | yes | ` ` |
| `SERVERLESS_OPTIONS` | Additional options for the command `serverless` | no | `--verbose` |
| `DEPLOY_STAGE` | The stage to where you want to deploy | no | ` ` |
| `AWS_REGION` | The specific region to where you want to deploy | no | ` ` |

### Artifacts

This job will produce an artifact containing the command's output and the folder `.serverless` which has stack events during deployment.


### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)