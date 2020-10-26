# 🐘 PHPUnit Testing

## Description

Using this job you'll be able to launch PHPUnit tests. You need nothing more than a valid phpunit.xml.

Results of tests are available in a report named `report-phpunit.xml` as an artifact.

## How to use it

1. Have a valid `phpunit.xml` in the root of your project. See [Variables]( #variables) if it is not in the root.
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/phpunit_test.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `phpunit_test`
* Docker image:
[`lorisleiva/laravel-docker:7.3`](https://hub.docker.com/r/lorisleiva/laravel-docker)
* Default stage: `static_tests`
* When: `always`


### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PHPUNIT_VERBOSITY` <img width=250/> | Define the verbosity of PHPUnit | `v` |
| `PROJECT_ROOT` <img width=250/> | Define where your project and the phpunit.xml are | `/` |
