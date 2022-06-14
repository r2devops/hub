## Objective

Build HTML documentation form Markdown source using Docusaurus, and can even embed JSX components into your Markdown thanks to MDX.
In order to build Docusaurus, the user must `init` a Docusaurus project, checkout the [documentation](https://docusaurus.io/docs/installation){:target="_blank"}. 

## How to use it

1. Ensure that your project has [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
      file.
1. Check the Docusaurus [documentation](https://docusaurus.io/docs){:target="_blank"} to install and configure a Docusaurus project.
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `docusaurus_build`
* Docker image:
[`node:18-buster`](https://hub.docker.com/r/_/node)
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative path in your repository to your Docusaurus project. <img width=175/>| `.` <img width=100/>|
| `DOCUSAURUS_OUTPUT_PATH` <img width=100/> | Directory who contains the result of the Docusaurus build. <img width=175/>| `website_build` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)