## Objective

This job checks if your PHP application depends on PHP packages with known security vulnerabilities.

## How to use it

1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/php_security_checker.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. By default, the output is optimized for terminals, change it via the variable `FORMAT_OUTPUT` (supported formats: `ansi`, `markdown`, `json`, and `yaml`):
  `--format=json`
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `php_security_checker`
* Docker image:
[`1.55-php7.4`](https://hub.docker.com/r/jakzal/phpqa/)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `COMPOSER_PATH` <img width=100/> | A general variable for this job <img width=175/>| `./composer.lock` <img width=100/>|
| `FORMAT_OUTPUT` <img width=100/> | A variable for the format of the output<img width=175/>| ` ` <img width=100/>|



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@melheb.younes](https://gitlab.com/melheb.younes)