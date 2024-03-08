## Objective

This job checks if your PHP application depends on PHP packages with known security vulnerabilities.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. By default, the output is optimized for terminals, change it via the variable `FORMAT_OUTPUT` (supported formats: `ansi`, `markdown`, `json`, and `yaml`):
  `--format=json`
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `COMPOSER_PATH` <img width=100/> | A general variable for this job <img width=175/>| `./composer.lock` <img width=100/>|
| `FORMAT_OUTPUT` | A variable for the format of the output | ` ` |
| `SECURITY_CHECKER_VERSION` | The version of Local PHP Security Checker | `2.0.6` |
| `IMAGE_TAG` | The default tag for the docker image | `3.17`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@melheb.younes](https://gitlab.com/melheb.younes)
