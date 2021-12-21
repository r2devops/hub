## Objective

A job to run end-to-end test

## How to use it

1. <Your steps>
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/cypress_run.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `cypress_run`
* Docker image:
[`node:16-buster`](https://hub.docker.com/r/_/node)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default | 
| ---- | ----------- | ------- |
| `CYPRESS_CONFIG_FILE` | Specify a config file to use | `cypress.json` |
| `CYPRESS_PROJECT_PATH` | Path to project dir | ` ` |
| `CYPRESS_RECORD_KEY` | Specify a record key in order to get a video of tests | ` ` |
| `CYPRESS_RECORDER` | Name of the reporter used | `spec` |
| `ADDITIONAL_OPTIONS` | Additional options to the run | ` ` |
