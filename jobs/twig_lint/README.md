## Objective

This job check if there are any errors on the twig templates

## How to use it

1. Put your twig files in the directory "templates"
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TEMPLATE_PATH` <img width=100/> | A general variable for this job <img width=175/>| `./templates` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `php7.4`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@melheb.younes](https://gitlab.com/melheb.younes)
