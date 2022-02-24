## Objective

Allow you to launch unit tests from your python project. The default variables will use `pipenv` and `pytest` to launch the tests, but you're welcome to override them as you want.

## How to use it

1. Prepare your project with unit tests to run in a separate directory: [pytest usage](https://docs.pytest.org/en/stable/usage.html?highlight=usage){:target="_blank"}
2. Prepare a Pipfile for pipenv to install any python dependencies your project may have: [Pipfile for pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html){:target="_blank"}, including your test framework which is chosen by the `TEST_FRAMEWORK` [variable](#variables)
3. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/python_test.yml'
    ```
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `python_test`
* Docker image:
[`python:3.8`](https://hub.docker.com/r/_/python){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

!!! note
    We are not using an [alpine linux](https://alpinelinux.org/){:target="_blank"} docker image in order to improve speed over resource efficiency. Alpine linux is using musl-libc and not glibc, so it can't use the python [wheels](https://pythonwheels.com/){:target="_blank"} with pip to get compiled dependencies while setting up your environment, and have to download and compile from source those libraries. As speed is the real issue that CI can have when building complex systems, we decided to use the general docker image of `python:3.7` based on Debian. You can see the explanation at this [link](https://pythonspeed.com/articles/alpine-docker-python/#:~:text=Don't%20use%20Alpine%20Linux,choosing%20a%20good%20base%20image){:target="_blank"}.

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `APT_PACKAGES` <img width=450/> | Packages that need to be installed | ` ` |
| `PYTHON_SETUP` | Bash commands to setup your python environment | `pip install pipenv; pipenv --bare install --dev` |
| `VENV` | Command to launch your testing environment | `pipenv run` |
| `TEST_FRAMEWORK` | Command to launch your testing framework | `pytest` |
| `OPTIONS` | Options to add to your testing framework | ` ` |
| `TEST_PATH` | Path to test folder | `/tests/unit` |

#### Changing the test framework

If you want for example to change your test framework from pytest to nosetests, you just have to override the `TEST_FRAMEWORK` variable as such in your `gitlab-ci.yml`, after including the job:

```yaml
python_test:
  variables:
    TEST_FRAMEWORK: "nosetests"
```



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)