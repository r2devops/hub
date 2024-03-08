## Objective

!!! error "This job is deprecated 🚨"
    This job has been moved to [`s3_deploy`](https://r2devops.io/_/r2devops-bot/s3_deploy) and must be use instead.
    The job is no more maintained and is now deprecated. Despites it still exists to keep working on pipelines.

This job uses the latest AWS CLI version (v2 for now) in order to sync files between a directory and a target S3 bucket. It's compatible with all s3 object storage (not only AWS).

[AWS CLI](https://aws.amazon.com/cli/){:target="_blank"} is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

## How to use it
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Set your credentials variables in the Gitlab CI/CD variables section of your project (see the [S3 documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html){:target="_blank"} about credentials) .

    ??? summary "Need a custom Endpoint ⚓ ?"
      Just type your custom url in the variable `AWS_ENDPOINT`
      For example, you can find the custom endpoint url for Scaleway [here](https://www.scaleway.com/en/docs/storage/object/api-cli/object-storage-aws-cli/){:target="_blank"}.

1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `AWS_ACCESS_KEY_ID` | Access key | ` ` |
| `AWS_SECRET_ACCESS_KEY` | Secret key | ` ` |
| `AWS_DEFAULT_REGION` | Region used | ` ` |
| `AWS_BUCKET_NAME`| The name of the bucket | ` ` |
| `AWS_ENDPOINT` | Custom endpoint if needed | ` ` |
| `AWS_ACL` | If you want to add an ACL (e.g. `public-read`) | ` ` |
| `SYNC_DIR` | Directory to sync | `build` |
| `DELETE_OLD_FILE` | Delete files that exist in the destination but not in the source  | `false` |
| `IMAGE_TAG` | The default tag for the docker image | `3.13.6`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)
