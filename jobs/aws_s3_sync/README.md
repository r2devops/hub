## Objective

This job uses the latest AWS CLI version (v2 for now) in order to sync files between a directory and a target S3 bucket. It's compatible with all s3 object storage (not only AWS).

[AWS CLI](https://aws.amazon.com/cli/){:target="_blank"} is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

## How to use it
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/aws_s3_sync.yml'
    ```
1. Set your credentials variables in the Gitlab CI/CD variables section of your project (see the [S3 documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html){:target="_blank"} about credentials) .

    ??? summary "Need a custom Endpoint ⚓ ?"
      Just type your custom url in the variable `AWS_ENDPOINT`
      For example, you can find the custom endpoint url for Scaleway [here](https://www.scaleway.com/en/docs/storage/object/api-cli/object-storage-aws-cli/){:target="_blank"}.

1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details
* Job name: `aws_s3_sync`
* Docker image: [alpine:3.13.6](https://hub.docker.com/_/alpinei){:target="blank"}
* Default stage: `deploy`

### Variables

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
