## Objective

{{ description }}

## How to use it

1. <Your steps>
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/{{ job_name }}.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `{{ job_name }}`
* Docker image:
[`{{ image }}`](https://hub.docker.com/r/_/{{ image }})
* Default stage: `{{ stage }}`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `VARIABLE` <img width=100/> | A general variable for this job <img width=175/>| `{{ variable }}` <img width=100/>|
