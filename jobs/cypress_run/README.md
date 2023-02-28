## Objective

This job test your front end web application by running tests headlessly in a CI context.

## How to use it

!!! warning
    You must override `CYPRESS_BASE_URL` variable.
    To ensure that the job work you have to specify the URL of your server (Example: `http://localhost:4200` for Angular web Application, `http://localhost:3000` for React, etc.).
    It's used to     prevent Cypress runs before your web sever is up and available. You can see more [here](https://docs.cypress.io/guides/continuous-integration/introduction#Boot-your-server)


1. Ensure that your project is set to use Cypress. You can refer to the [Cypress Getting Started](https://docs.cypress.io/guides/getting-started/installing-cypress). You can see your job record on the Cypress Dashboard by connecting your GitLab account and set the `CYPRESS_RECORD_KEY` variable. See how to [Set up your project to record](https://docs.cypress.io/guides/dashboard/projects#Set-up-a-project-to-record) and [Connect GitLab with Cypress Dashboard](https://docs.cypress.io/guides/dashboard/gitlab-integration#Installing-the-GitLab-integration).

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `CYPRESS_CONFIG_FILE` | Specify a config file to use | `cypress.json` |
| `CYPRESS_PROJECT_PATH` | Path to project directory | `.` |
| `CYPRESS_RECORD_KEY` | Specify a record key in order to get a video of tests | ` ` |
| `CYPRESS_REPORTER` | Name of the [Mocka reporter](https://docs.cypress.io/guides/tooling/reporters) used| `spec` |
| `CYPRESS_BASE_URL`  | **(MANDATORY)** The base URL of your server | ` `|
| `ADDITIONAL_OPTIONS` | Additional options to the run | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `node16.5.0-chrome94-ff93`  |


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)
