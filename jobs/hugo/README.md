## Objective

[Hugo](https://gohugo.io/){:target="_blank"} is a static HTML and CSS website generator written in Go. It is optimized for speed, ease of use, and configurability. Hugo takes a directory with content and templates and renders them into a full HTML website.

## How to use it

1. Ensure that your project have been initialised with the `hugo new site website` command. Please, check the [documentation](https://gohugo.io/documentation/){:target="_blank"} to learn more about Hugo.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative to root of your repository, it is the path to your project. <img width=175/>| `.` <img width=100/>|
| `HUGO_VERSION` <img width=100/> | The Hugo version to install and execute. <img width=175/>| `0.92.0` <img width=100/>|
| `HUGO_SOURCE` <img width=100/> | Directory name of the source files to build the Hugo website. <img width=175/>| `website` <img width=100/>|
| `HUGO_OUTPUT` <img width=100/> | Directory name of the Hugo output. <img width=175/>| `public/` <img width=100/>|
| `ADDITIONAL_OPTIONS` <img width=100/> | Possibility to add more options into the Hugo command. <img width=175/>| ` ` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `1.19-buster`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
