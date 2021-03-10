## Objective

This job check if there are any errors on the twig templates

## How to use it

1. Put your twig files in the directory "templates"
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:
    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/twig_lint.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `twig_lint`
* Docker image:
[`twig_lint`](https://hub.docker.com/r/jakzal/phpqa/)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TEMPLATE_PATH` <img width=100/> | A general variable for this job <img width=175/>| `./templates` <img width=100/>|
