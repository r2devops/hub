## Objective

Deploy your static website or frontend application really quick with [Cloudflare pages](https://pages.cloudflare.com/).
This job allows you to deploy 500 time per month your site for free. You can take a look at the [documentation](https://developers.cloudflare.com/pages/get-started/). 

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Set credentials variables `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` in
   the GitLab CI/CD variables section of your project. Follow the [documentation](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/#generate-an-api-token) for retrieving them.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀


## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PAGES_BUILD_PATH` <img width=100/> | Path to folder which contains the static website files to publish <img width=175/>| `website_build` <img width=100/>|
| `PROJECT_NAME` | Project name of your deployment on Cloudflare | `$CI_PROJECT_PATH_SLUG` |
| `PRODUCTION_BRANCH` | The name of the production branch | `$CI_DEFAULT_BRANCH` |
| `DEPLOY_PRODUCTION` | Publish the website on production | `true` |
| `DOMAIN_NAME` | Set one custom domain name for your website. It must be registered on Cloudflare | ` ` |
| `CLOUDFLARE_API_TOKEN` | ⚠️ Mandatory variable : define your [API token](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/#generate-an-api-token). This variable should be specified in `GitLab > CI/CD Settings`.  | ` ` |
| `CLOUDFLARE_ACCOUNT_ID` | ⚠️ Mandatory variable : define your [Account ID](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/#get-project-account-id). This variable should be specified in `GitLab > CI/CD Settings`.  | ` ` |
| `CLOUDFLARE_ZONE_ID` | ⚠️ Mandatory variable : define your [Zone ID](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/), related to the `DOMAIN_NAME`. This variable should be specified in `GitLab > CI/CD Settings`.  | ` ` |
| `CLOUDFLARE_API` | The URL of the Cloudflare API. | `https://api.cloudflare.com/client/v4` |
| `WRANGLER_VERSION` | Version of the npm package [wrangler](https://npmjs.com/package/wrangler) used to publish the website | `2.1.1` |
| `IMAGE_TAG` | The default tag for the docker image | `18-alpine` |

   !!! info "Set up a custom domain name 🛣"
   If you want one custom domain, registered on Cloudflare, you must set the two variable :  
      - `DOMAIN_NAME` : the domain name you want to use  
      - `CLOUDFLARE_ZONE_ID` : the Zone ID of your domain name, you can find it in the [Cloudflare dashboard](https://developers.cloudflare.com/fundamentals/get-started/basic-tasks/find-account-and-zone-ids/).

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)