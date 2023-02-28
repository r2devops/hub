## Objective

Deploy your static website on following S3-compatible cloud-providers:
- AWS
- Scaleway

## How to use it

1. Include this job in your configuration. Copy/paste link in the right panel
   and see [use the
   hub](https://docs.r2devops.io/get-started/use-templates/)
1. Set credentials variables `S3_ACCESS_KEY_ID` and `S3_SECRET_ACCESS_KEY` in
   the Gitlab CI/CD variables section of your project. Follow these guides
   depending of your Cloud-provider:
    - [AWS](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-creds-create){:target="_blank"}
    - [Scaleway](https://www.scaleway.com/en/docs/console/my-project/how-to/generate-api-key/){:target="_blank"}
1. If you are not using AWS: specify the S3 endpoint of your provider in
   `S3_ENDPOINT` variable.
    - [Scaleway](https://www.scaleway.com/en/docs/storage/object/api-cli/object-storage-aws-cli/){:target="_blank"}
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `S3_PROVIDER` | Name of the Provider, could be `aws` or `scaleway` | `aws` |
| `S3_ACCESS_KEY_ID` | Access key | ` ` |
| `S3_SECRET_ACCESS_KEY` | Secret key | ` ` |
| `S3_REGION` | Region used | `us-west-1` |
| `S3_SYNC_DIR` | Directory to sync | `website_build` |
| `S3_BUCKET_NAME`| The name of the bucket | `$CI_PROJECT_PATH_SLUG` |
| `S3_ENV` | Name of the development environment. Is used to suffixed bucket's name if it is sets and not equal to `production`. | `$CI_ENVIRONMENT_SLUG` |
| `S3_ACL` | Use custom ACL ([from this list](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl)) | `public-read` |
| `S3_ENDPOINT` | Custom endpoint if needed. If not set use `https://s3.fr-par.scw.cloud` for `scaleway` provider. | ` ` |
| `S3_DELETE_OLD_FILE` | Delete files that exist in the destination but not in the source  | `true` |
| `S3_BUCKET_POLICY_FILE` | The policy applied to the bucket. If not set will apply `${S3_SNIPPET_POLICY_LINK}/bucket_policy-${S3_PROVIDER}.json`. Otherwise, it should be declared in Gitlab CI/CD variables section as `file` | ` ` |
| `S3_DEPLOY_WEBSITE` | Should deploy a static website on the bucket | `true` |
| `S3_WEBSITE_HOMEPAGE` | The file for the homepage | `index.html` |
| `S3_WEBSITE_ERRORPAGE` | The file for the error page | `error.html` |
| `S3_CLI_VERSION` | The version of `AWS` cli | `2.7.7` |
| `S3_SNIPPET_POLICY_LINK` | The link where to fetch policy files | `https://gitlab.com/r2devops/hub/-/snippets/2351961` |
| `S3_OPTIONS` | Additional option(s) to use in AWS CLI | ` ` |
| `IMAGE_TAG` | The default tag for the image | `2.7.12` |

## Author

This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)**
added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by
[@GridexX](https://gitlab.com/GridexX)
