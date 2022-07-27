## Objective

This job check if there are any errors on the twig templates

## How to use it

1. Put your twig files in the directory "templates"
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TEMPLATE_PATH` <img width=100/> | A general variable for this job <img width=175/>| `./templates` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `php7.4`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@melheb.younes](https://gitlab.com/melheb.younes)
