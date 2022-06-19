## Objective

Tox aims to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.

## How to use it

1. Ensure that your project have
   [`tox.ini`](https://tox.wiki/en/latest/){:target="_blank"} 
   file
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `python_tox`
* Docker image:
[`vicamo/pyenv:slim-focal`](https://hub.docker.com/r/vicamo/pyenv)
* Default stage: `tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative to root of your repository, it is the path to your python project <img width=175/>| `.` <img width=100/>|
| `PYTHON_ENV` | Restrict the test to run on a specific environnement of Python, if none is specified `Tox` will run the test on all environnement listed in the `tox.ini` file. | ` ` |
| `ADDITIONAL_OPTIONS` | [Additional options](https://tox.wiki/en/latest/config.html?result-json#tox) for tox command | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `slim-focal`  |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexiaognard](https://gitlab.com/alexiaognard)