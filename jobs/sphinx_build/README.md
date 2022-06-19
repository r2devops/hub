## Objective

[Sphinx](https://www.sphinx-doc.org/en/master/index.html){:target="_blank"} is a tool that makes it easy to create intelligent and beautiful documentation for python projects.

## How to use it

1. Ensure that your project has been initialized with the `sphinx-quickstart` command, it will generate the source directory where you can edit your `conf.py` file.
1. You can specify the `APIDOC_SOURCE` variable, in this case the job will run the `sphinx-apidoc` command which will generate the Sphinx sources automatically. If you leave it empty the `sphinx-apidoc` command will be skipped.
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `sphinx_build`
* Docker image:
[`python:3.10-buster`](https://hub.docker.com/r/_/python){:target="_blank"}
* Default stage: `build`
* When: only run on `main` branch

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative to root of your repository, it is the path to your project. | `.` |
| `SPHINX_THEME` | HTML theme builder to download, sphinx comes with [builtin themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes){:target="_blank"}. Check this [site](https://sphinx-themes.org/){:target="_blank"} to download third party themes | ` ` |
| `SPHINX_BUILDER` | Builder used for site generation, check the [builder list](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options){:target="_blank"}.| `html` |
| `SPHINX_SOURCE` | Directory name of the source files to build the Sphinx website.  | `docs/` |
| `SPHINX_OUTPUT` | Output directory path produced by the `sphinx-build`. | `website_build/` |
| `SPHINX_OPTIONS` | Possibility to add more [options](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#options){:target="_blank"} into the `sphinx-build` command. | ` ` |
| `APIDOC_SOURCE` | Directory name of the source files to build the Sphinx sources automatically, check the `sphinx-apidoc` [documentation](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html){:target="_blank"} to learn more. Leave this variable empty if you don't want to execute this command. | ` ` |
| `APIDOC_OUTPUT` | Output directory path produced by the `sphinx-apidoc`. | `docs/reference/source/` |
| `APIDOC_OPTIONS` | Possibility to add more [options](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html#options){:target="_blank"} into the `sphinx-apidoc` command. | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `3.10-buster`  |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)