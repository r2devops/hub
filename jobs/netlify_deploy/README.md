## Objective

Deploy your front-end application to [Netlify](https://netlify.com). It is an all-in-one platform for automating modern web projects. Replace your hosting infrastructure, continuous integration, and deployment pipeline with a single workflow.
See the [documentation](https://docs.netlify.com/) for more information.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NETLIFY_AUTH_TOKEN` <img width=100/> | ⚠️ Mandatory variable. The authentication token of the user. This variable should be specified in `Gitlab > CI/CD Settings`. <img width=175/>| ` ` <img width=100/>|
| `NETLIFY_SITE_ID` | ⚠️ Mandatory variable. The site id. This variable should be specified in `Gitlab > CI/CD Settings`. | ` ` |
| `NETLIFY_BUILD_DIRECTORY` | Directory to deploy | `build` |
| `NETLIFY_CLI_VERSION` | The version of Netlify CLI | `10.5.0` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

!!! info
    A token can be generated on Netlify in the section `User settings > Applications`, see the [documentation](https://docs.netlify.com/cli/get-started/#obtain-a-token-in-the-netlify-ui). Or you could create one via the command [`netlify login`](https://docs.netlify.com/cli/get-started/#obtain-a-token-in-the-netlify-ui).
    A deployment can be created from the dashboard or with the command [`netlify init`](https://docs.netlify.com/cli/get-started/#automated-setup).


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)
