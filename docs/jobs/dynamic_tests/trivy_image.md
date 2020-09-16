# 🐍 Python Testing

## Description

Allow you to launch unit tests from your python project. The default variables will use `pipenv` and `pytest` to launch the tests, but you're welcome to override them as you want.

## How to use it

1. Prepare your project with unit tests to run in a separate directory: [pytest usage](https://docs.pytest.org/en/2.8.7/usage.html)
2. Prepare a Pipfile for pipenv to install any python dependencies your project may have: [Pipfile for pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html), including your test framework which is chosen by the `TEST_FRAMEWORK` [variable](#Variables)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/python_test.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `python_test`
* Docker image:
[`python:3.7`](https://hub.docker.com/r/_/python)
* Default stage: `static_tests`
* When: `always`

!!! note
    We are not using an [alpine linux](https://alpinelinux.org/) docker image in order to improve speed over ressource efficiency. Alpine linux is using musl-libc and not glibc, so it can't use the python [wheels](https://pythonwheels.com/) with pip to get compiled dependencies while setting up your environment, and have to download and compile from source those libraries. As speed is the real issue that CI can have when building complex systems, we decided to use the general docker image of `python:3.7` based on Debian. You can see the explanation at this [link](https://pythonspeed.com/articles/alpine-docker-python/#:~:text=Don't%20use%20Alpine%20Linux,choosing%20a%20good%20base%20image).

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
python_tests:
  variables:
    TEST_FRAMEWORK: "nosetests"
```

## Changelog

* **[latest]**(current -> `0.0.2`) : `<TAG_URL>`
* **[python_test-0.0.2](<include tag>)**
* **[python_test-0.0.1](<include tag>)** (initial version)

??? License
    Copyright 2020 go2scale
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 🧱 Trivy image analysis

## Description

Run a security issue detection in a docker image using
[Trivy](https://github.com/aquasecurity/trivy), a Simple and Comprehensive
Vulnerability Scanner for Containers and other Artifacts. More details on Trivy
vulnerability detection capabilities are available in its official
[README](https://github.com/aquasecurity/trivy#vulnerability-detection)

!!! warning
    With the default configuration, this job will fail if errors are detected.
    It's the recommended configuration to reduce security risks in your
    software. You can disable this behaviour by setting the value `0` to the
    variable `TRIVY_EXIT_CODE`.

## How to use it

1. Check supported OS and packages
   [here](https://github.com/aquasecurity/trivy#vulnerability-detection)
2. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/trivy_image.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `trivy_image`
* Docker image: [`docker`](https://hub.docker.com/_/docker)
* Default stage: `dynamic_tests`

### Variables


| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
|:-|:-|:-
| `IMAGE` <img width=450/> | Target name or target path <img width=500/> | `$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA` <br/> or `$CI_REGISTRY_IMAGE:$CI_COMMIT_TAG` in case of tag creation |
| `TRIVY_VERSION` | Version of trivy to use. Releases version are available [here](https://github.com/aquasecurity/trivy/releases) | `0.9.2` |
| `TRIVY_SEVERITY` | Severities of vulnerabilities to be displayed | `UNKNOWN`,`LOW`,`MEDIUM`,`HIGH`,`CRITICAL`|
| `TRIVY_EXIT_CODE` | Exit code when vulnerabilities were found | 1 |
| `TRIVY_VULN_TYPE` | List of vulnerability types | os,library |
| `TRIVY_OUTPUT` | Output file name | junit-report.xml |
| `TRIVY_IGNOREFILE` | Specify .trivyignore file | .trivyignore |
| `TRIVY_CACHE_DIR` | cache directory | .trivycache/
| `TRIVY_FORMAT` | Format (table, json, template) | template |
| `TEMPLATE_NAME` | Name of used template | junit.tpl |
| `TRIVY_CLEAR_CACHE` | Clear image caches without scanning | false |
| `TRIVY_IGNORE_UNFIXED` | Display only fixed vulnerabilities | false |
| `TRIVY_DEBUG` | Debug mode | false |
| `DOCKER_HOST` | Daemon socket to connect to | tcp://docker:2375 |
| `TRIVY_TIMEOUT` | Docker timeout | 2m0s |
| `TRIVY_LIGHT` | Trivy faster without descriptions and refs | false |
| `TRIVY_DOWNLOAD_DB_ONLY` | Download vulnerability database without scan | false |
| `TRIVY_NO_PROGRESS` | Suppress progress bar | false |
| `TRIVY_QUIET` | Suppress progress bar and log output | false |
| `TRIVY_SKIP_UPDATE` | Skip vulnerability database update | false |
| `TRIVY_REMOVED_PKGS` | Detect vulns of Alpine removed packages | false |


### Artifacts

We use [Junit](https://junit.org/junit5/)'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget

## Changelog

* **[latest]**(current -> `2020-08-05_1`) : `<TAG_URL>`
* **Tag `2020-08-05_1`** (initial version) : `https://jobs.go2scale.io/2020-08-05_1/trivy_image.yml`

??? License
    Copyright 2020 go2scale
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
