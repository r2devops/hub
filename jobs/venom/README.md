## Objective

This job manages and runs your integration tests with efficiency thanks to executors and assertions. Please, check the [Venom documentation](https://github.com/ovh/venom#readme){:target="_blank"}, if you want to learn more about the tool.

## How to use it

1. Write your test suite for Venom and specified the path to the test file with the `VENOM_TESTS` variable. Check the [documentation](https://github.com/ovh/venom#testsuites){:target="_blank"} to learn more about test suite.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/venom.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `venom`
* Docker image:
[`golang:1.17.6-buster`](https://hub.docker.com/r/_/golang){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description                                                                                                                                                                       | Default                  |
| ---- |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| `PROJECT_ROOT` <img width=100/> | Relative path in your repository to your project. <img width=175/>                                                                                                                | `.` <img width=100/>     |
| `VENOM_VERSION` <img width=100/> | The Venom version to install and execute. <img width=175/>                                                                                                                        | `1.0.1` <img width=100/> |
| `VENOM_TESTS` <img width=100/> | Relative path to a single `yml` file which contains your test suite. <img width=175/>                                                                                             | ` ` <img width=100/>     |
| `REPORT_FORMAT` <img width=100/> | Format of the Venom report, available formats are  JUnit (xml), json, yaml and tap. <img width=175/>                                                                              | `xml` <img width=100/>   |
| `OUTPUT_DIRECTORY` <img width=100/> | Directory path to the Venom reports output. <img width=175/>                                                                                                                      | `dist` <img width=100/>  |
| `ADDITIONAL_OPTIONS` <img width=100/> | Possibility to add [more options](https://github.com/ovh/venom#executors){:target="_blank"} into the Venom command, like changing the default executor and more. <img width=175/> | ` ` <img width=100/>     |
