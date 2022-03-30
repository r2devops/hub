## Objective

Publish HTML documentation located in `public` folder, retrieved as an artifact
from previous job named `documentation`.

## How to use it

!!! note "Requirements"
    You have to use a job which build your documentation in a previous stage.
    We recommend you to use a documentation job available on the hub in [build
    📦 stage](/jobs/#build). They build documentation and publish it as
    artifact in `website_build/` folder.

!!! note "Documentation jobs list:"
    * [ApiDoc](/jobs/build/apidoc/)
    * [Mkdocs](/jobs/build/mkdocs/)
    * [Doxygen](/jobs/build/doxygen/)
    * [PHPDocumentor](/jobs/build/phpdocumentor/)
    * [OpenAPI](/jobs/build/openapi/)

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
2. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
3. Well done, your job is ready to work ! 😀


## Job details

* Job name: `pages`
* Docker image: [`ruby`](https://hub.docker.com/_/ruby){:target="_blank"}
* Stage: `deploy`
* When: only run on `master` branch

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PAGES_BUILD_PATH` | Path to folder which contains the static website files to publish | `website_build/` |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)