## Objective

This job will use the tool [pylint](https://pylint.pycqa.org/en/latest/intro.html) that checks for errors in your Python code, tries to enforce a coding standard and looks for code smells.

## How to use it

1. Make sure that your project has [`__init__.py`](https://docs.python.org/3/tutorial/modules.html){:target="_blank"}
1. You can use a pylintrc file on your project or use [environment variable](https://pylint.pycqa.org/en/latest/user_guide/run.html), to specify options for `pylint`.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `PYLINT_OPTIONS` | [Additional options](https://pylint.pycqa.org/en/latest/user_guide/run.html) for `pylint` | `` |
| `PYLINT_OUTPUT` | Output file | `report_pylint.xml` |
| `PYLINT_EXIT_ZERO` | Returns a non-zero status code. If the option is specified, and Pylint runs successfully, it will exit with 0 regardless of the number of lint issues detected. | `true` |
| `IMAGE_TAG` | The default tag for the docker image | `3.10-buster`  |


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexiaognard](https://gitlab.com/alexiaognard)
