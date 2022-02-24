## Objective

This job will use the tool [pylint](https://pylint.pycqa.org/en/latest/intro.html) that checks for errors in your Python code, tries to enforce a coding standard and looks for code smells.

## How to use it

1. Make sure that your project has [`__init__.py`](https://docs.python.org/3/tutorial/modules.html){:target="_blank"} 
1. You can use a pylintrc file on your project or use [environment variable](https://pylint.pycqa.org/en/latest/user_guide/run.html), to specify options for `pylint`.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/pylint.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `pylint`
* Docker image:
[`python:3.10-buster`](https://hub.docker.com/r/_/python)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `PYLINT_OPTIONS` | [Additional options](https://pylint.pycqa.org/en/latest/user_guide/run.html) for `pylint` | `` |
| `PYLINT_OUTPUT` | Output file | `report_pylint.xml` |
| `PYLINT_EXIT_ZERO` | Returns a non-zero status code. If the option is specified, and Pylint runs successfully, it will exit with 0 regardless of the number of lint issues detected. | `true` |


### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexiaognard](https://gitlab.com/alexiaognard)