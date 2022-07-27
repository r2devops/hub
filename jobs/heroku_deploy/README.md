## Objective

Deploy your application to Heroku. You can use custom buildpacks depending on our needs, please check out the documentation [here](https://devcenter.heroku.com/articles/buildpacks). It use [`dpl`](https://github.com/travis-ci/dpl), which is a command line tool for deploying code, html, packages, or build artifacts to various service providers.

## How to use it

1. Create an application on [Heroku](https://dashboard.heroku.com/new-app) and fill the application name in the `HEROKU_APP` variable.
1. Copy your API key in the `HEROKU_API_KEY` variable.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `HEROKU_APP` <img width=100/> | The name of the Heroku application <img width=175/>| ` ` <img width=100/>|
| `HEROKU_API_KEY` | ⚠️ Sensitive variable: it should be specified in `Gitlab > CI/CD Settings`. The Heroku application key.  | ` `  |
| `ADDITIONAL_OPTIONS` | Additional [options](https://github.com/travis-ci/dpl#heroku-api) for `dpl` command | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `3.2-rc-buster`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)
