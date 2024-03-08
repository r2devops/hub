## Objective

Build HTML documentation form Markdown source using Docusaurus, and can even embed JSX components into your Markdown thanks to MDX.
In order to build Docusaurus, the user must `init` a Docusaurus project, checkout the [documentation](https://docusaurus.io/docs/installation){:target="_blank"}.

## How to use it

1. Ensure that your project has [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
      file.
1. Check the Docusaurus [documentation](https://docusaurus.io/docs){:target="_blank"} to install and configure a Docusaurus project.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative path in your repository to your Docusaurus project. <img width=175/>| `.` <img width=100/>|
| `DOCUSAURUS_OUTPUT_PATH` <img width=100/> | Directory who contains the result of the Docusaurus build. <img width=175/>| `website_build` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
