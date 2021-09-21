## Objective

This job uses the AWS CLI (v1 for now) in order to sync files between a directory and a target S3 bucket. See changes between the two versions [here](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html).

[AWS CLI](https://aws.amazon.com/cli/){:target="_blank"} is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

## How to use it
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/aws_s3_sync.yml'
    ```
2. Fill the variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` or `AWS_DEFAULT_REGION` with yours. See the [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).
    ??? summary "Need a custom Endpoint ⚓ ?"
        Just type your custom url in the variable `AWS_ENDPOINT`
        For example, you can find the custom endpoint url for Scaleway on their [documentation](https://www.scaleway.com/en/docs/storage/object/api-cli/object-storage-aws-cli/).

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details
* Job name: `aws_s3_sync`
* Docker image: [bitnami/aws-cli:2.2.39](https://hub.docker.com/r/bitnami/aws-cli){:target="blank"}
* Default stage: `others`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `AWS_ACCESS_KEY_ID` | Access key | ` ` |
| `AWS_SECRET_ACCESS_KEY` | Secret key | ` ` |
| `AWS_DEFAULT_REGION` | Region used | ` ` |
| `AWS_ENDPOINT` | Custom endpoint if needed | ` ` |
| `AWS_ACL` | If you want to add an ACL (e.g. `public-read`) | ` ` |
| `SYNC_DIR` | Directory to sync | `build` |
| `BUCKET_NAME`| The name of the bucket | ` ` |
| `ADDITIONAL_OPTIONS` | Additional options to the CLI | ` ` |