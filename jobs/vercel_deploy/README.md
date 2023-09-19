## Objective

Deploy your frontend application to [Vercel](https://vercel.com). Vercel supports a wide range of the most popular frontend frameworks ([see list](https://vercel.com/docs/frameworks)), optimizing how your site builds and runs no matter what tool you use.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. If you want to manually set a custom domain already register inside your Vercel dashboard, you must set `$CUSTOM_DOMAIN` and `$VERCEL_ENV_GENERATED_URL` variables (see variables list below), it will trigger the `vercel alias set` command ([see Vercel alias documentation](https://vercel.com/docs/cli/alias)), more details below
1. By default this job will deploy with the production environment, if you want to deploy with another environment, you must set `$VERCEL_ENV` variable (see variables list below and [Vercel environments documentation](https://vercel.com/docs/concepts/deployments/environments))
1. Well done, your job is ready to work ! 😀

## Preview and Production Environments on Vercel

To have both a `preview` and a `production` environment simultaneously, you can follow a workaround. By default, Vercel sets the `preview` and `production` environments to the same branch if you don't specify a branch explicitly.

However, this causes an issue because you can't have two environments with the same branch. If you have a domain set for the `staging` environment (`preview` environment in Vercel), it will be overwritten when you deploy the `production` environment.

To overcome this problem, you need to define an unused branch that you won't be using. Then, in your Vercel dashboard, navigate to `Project Settings > Domains` and set this unused branch for the `preview` environment.

Next, you must set the `$VERCEL_ENV_GENERATED_URL` variable (refer to the [Vercel CLI URL documentation](https://vercel.com/docs/concepts/deployments/generated-urls#url-with-vercel-cli)) with the URL of the `preview` environment. Additionally, set the `$CUSTOM_DOMAIN `variable with your `custom domain` that you want to assign to the environment.

By doing this, the [vercel alias set](https://vercel.com/docs/cli/alias) command will be triggered.

## How to use this job multiple times

If you want to deploy multiple times on different environments.

You can do that by using the [extends](https://docs.gitlab.com/ee/ci/yaml/#extends) keyword.

### Example for two environments:

```yml
include:
    - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/vercel_deploy.yml'

stages:
  - deploy
  - deploy_prod

# Override of variables of the remotely included vercel_deploy job
vercel_deploy: 
  variables:
    VERCEL_ENV: "preview" # change the default value "production"
    TEAM_SLUG_SCOPE: "team-slug" # your team slug
    VERCEL_ENV_GENERATED_URL: "project-name-author-name-scope-slug.vercel.app" # your vercel preview environment generated url
    CUSTOM_DOMAIN: "mycustomdomain.tech" # your custom domain

# New job that extends the remotely included vercel_deploy job
vercel_deploy_prod: 
  stage: deploy_prod # change the default stage `deploy` to run this job after the preview deployment
  extends:
    - vercel_deploy
  variables:
    VERCEL_ENV: "production"
    TEAM_SLUG_SCOPE: "team-slug" # your team slug
    VERCEL_ENV_GENERATED_URL: "project-name-scope-slug.vercel.app" # your vercel production environment generated url
    CUSTOM_DOMAIN: "mycustomdomain.com" # your custom domain
```

## Variables

!!! info
    `$VERCEL_ORG_ID`, `$VERCEL_PROJECT_ID` and `$VERCEL_TOKEN` variables should be specified in the `Gitlab > CI/CD Settings` section of your project.
    ⚠️ If you set these variables as protected they won't be accessible inside others branches than the default one.

| Name                                  | Description                                                                                                                                   | Default              |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `VERCEL_TOKEN` <img width=100/> | ⚠️ Mandatory variable. Defined in [Personal Account Settings > Tokens](https://vercel.com/account/tokens). This variable should be specified in the `Gitlab > CI/CD Settings` section of your project. <img width=175/> | ` ` <img width=100/> |
| `VERCEL_ORG_ID` <img width=100/> | ⚠️ Mandatory variable. Defined in `Team Settings > General > Team ID`. This variable should be specified in the `Gitlab > CI/CD Settings` section of your project. <img width=175/> | ` ` <img width=100/> |
| `VERCEL_PROJECT_ID` <img width=100/> | ⚠️ Mandatory variable. Defined in `Project Settings > General > Project ID`. This variable should be specified in the `Gitlab > CI/CD Settings` section of your project. <img width=175/> | ` ` <img width=100/> |
| `VERCEL_ENV`| The deployment environment | `production` |
| `TEAM_SLUG_SCOPE`| ⚠️ Mandatory variable if you have set a `VERCEL_TOKEN` with the `Full account` scope but still want to deploy to a project inside one of your `Vercel Teams`. Defined in `Team Settings > General > Team URL`| ` ` |
| `VERCEL_ENV_GENERATED_URL`             | The [environment generated url](https://vercel.com/docs/concepts/deployments/generated-urls#url-with-vercel-cli) to assign a `custom domain` to it. ⚠️ `$CUSTOM_DOMAIN` must also be set                                                                                                                           | ` `              |
| `CUSTOM_DOMAIN`                 | The custom domain to assign a `$VERCEL_ENV_GENERATED_URL` to it.        ⚠️ `$VERCEL_ENV_GENERATED_URL` must also be set                                                                                                                       | ` `             |
| `IMAGE_TAG`                           | The default tag for the node docker image                                                                                                          | `16.16.0`          |

## Troubleshooting

!!! info "You don't have access to the domain <domain_name> under <scope_slug>"
    This error can occur when you have set a `VERCEL_TOKEN` with the `Full account` scope but want to deploy to use a domain set inside one of your `Vercel Teams`.
    To fix it you must set `$TEAM_SLUG_SCOPE` with the `Team slug` containing your domain

## Author

This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Totara-thib](https://gitlab.com/Totara-thib)
