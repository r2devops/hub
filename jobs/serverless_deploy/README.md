## Objective

This job will help you deploy your serverless resources to AWS using the framework [Serverless.com](https://www.serverless.com/){:target="_blank"}

!!! info
    You can get more information about `serverless deploy` [here](https://www.serverless.com/framework/docs/providers/aws/guide/deploying/){:target="_blank"}

## How to use it

1. Make sure that you have your file `serverless.yml` in the repository
1. Provide the mandatory variables for the job, check [Variables](#variables)
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

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
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

## Artifacts

This job will produce an artifact containing the command's output and the folder `.serverless` which has stack events during deployment.


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
