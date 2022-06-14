## Objective

Build HTML documentation form Markdown source using
[Mkdocs](https://www.mkdocs.org/){:target="_blank"}. All requirements to use [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"} are ready to use.

## How to use it

1. Prepare your project with Mkdocs configuration file and sources files as
   described in [Mkdocs
   documentation](https://www.mkdocs.org/#getting-started){:target="_blank"}. In your repository,
   documentation files must be organized as follows:
    ```
    /mkdocs.yml # This is your configuration file
    /docs/      # This folder contains all your documentation markdown files
    ```
3. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `mkdocs`
* Docker image:
[`squidfunk/mkdocs-material`](https://hub.docker.com/r/squidfunk/mkdocs-material){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `MKDOCS_OUTPUT_PATH` | Output directory path | `website_build/` |
| `MKDOCS_ADDITIONAL_PLUGINS` | Value of several [plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) to install before the build. They have to be separated by `;` | `mkdocs-awesome-pages-plugin;mkdocs-git-revision-date-localized-plugin;mkdocs-macros-plugin` |
| `IMAGE_TAG` | The default tag for the docker image | `8.1.4`  |

!!! info
    By default `MKDOCS_ADDITIONAL_PLUGINS` variable contains 3 plugins for `Material for mkdocs`
    If you don't override this variable, it will install those 3 plugins `mkdocs-awesome-pages-plugin`,
    `mkdocs-git-revision-date-localized-plugin`, `mkdocs-macros-plugin`

### Artifacts

When the job is successful, the build of your documentation is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Mkdocs Build` in merge requests.
    Exposition of artifact currently works only if you keep `MKDOCS_OUTPUT_PATH`
    default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)