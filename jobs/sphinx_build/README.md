## Objective

[Sphinx](https://www.sphinx-doc.org/en/master/index.html){:target="_blank"} is a tool that makes it easy to create intelligent and beautiful documentation for python projects.

## How to use it

1. Ensure that your project has been initialized with the `sphinx-quickstart` command, it will generate the source directory where you can edit your `conf.py` file.
1. You can specify the `APIDOC_SOURCE` variable, in this case the job will run the `sphinx-apidoc` command which will generate the Sphinx sources automatically. If you leave it empty the `sphinx-apidoc` command will be skipped.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative to root of your repository, it is the path to your project. | `.` |
| `SPHINX_THEME` | HTML theme builder to download, sphinx comes with [builtin themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes){:target="_blank"}. Check this [site](https://sphinx-themes.org/){:target="_blank"} to download third party themes | ` ` |
| `SPHINX_BUILDER` | Builder used for site generation, check the [builder list](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options){:target="_blank"}.| `html` |
| `SPHINX_SOURCE` | Directory name of the source files to build the Sphinx website.  | `docs/source/` |
| `SPHINX_OUTPUT` | Output directory path produced by the `sphinx-build`. | `website_build/` |
| `SPHINX_OPTIONS` | Possibility to add more [options](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options){:target="_blank"} into the `sphinx-build` command. | ` ` |
| `APIDOC_SOURCE` | Directory name of the source files to build the Sphinx sources automatically, check the `sphinx-apidoc` [documentation](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html){:target="_blank"} to learn more. Leave this variable empty if you don't want to execute this command. | ` ` |
| `APIDOC_OUTPUT` | Output directory path produced by the `sphinx-apidoc`. | `docs/reference/source/` |
| `APIDOC_OPTIONS` | Possibility to add more [options](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html#options){:target="_blank"} into the `sphinx-apidoc` command. | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `3.11-alpine`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
