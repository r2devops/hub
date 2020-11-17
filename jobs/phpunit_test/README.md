# 🐘 PHPUnit Testing

## Description

Using this job you'll be able to launch PHPUnit tests.

## How to use it

1. Put a `phpunit.xml` (check [syntax](https://phpunit.readthedocs.io/en/latest/configuration.html#the-phpunit-element){:target="_blank"}) in the root of your php project. Edit `PHPUNIT_CONFIG_FILE` (see [Variables](#variables)) to change the default behavior.

2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/phpunit_test.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `phpunit_test`
* Docker image:
[`lorisleiva/laravel-docker:7.3`](https://hub.docker.com/r/lorisleiva/laravel-docker){:target="_blank"}
* Default stage: `static_tests`
* When: `always`


### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PHPUNIT_OUTPUT` <img width=100/> | Output file <img width=175/>| `report_phpunit.xml` <img width=100/>|
| `PHPUNIT_CONFIG_FILE` | Config file source in repository | `phpunit.xml` |
| `PHPUNIT_COLORS` | Use colors in output | `never` |
| `PHPUNIT_OPTIONS` | Custom user options for phpunit | ` ` |
| `PROJECT_ROOT` | PHP Project location | `/` |

!!! note
    All paths defined in variables are starting from the root of your repository.

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.
The report defined in variable `PHPUNIT_OUTPUT` is also available directly in the artifacts.
