## Description

Execute your golang unit tests and have the results fully integrated with the various areas of the Gitlab UI plus provide code coverage data in pipelines and badges.

## How to use it

1. The job of course assumes that you have written your tests 
2. Choose a version in [version list](#changelog)
3. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the
   [jobs customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `UT_WORK_DIR` | If for any reason (monorepo for example) your go project is not at root of project, specify the relative path to the project | `$CI_PROJECT_DIR` |
| `UT_TEST_CMD` | Customise the test command if needed | `go test -v` |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@seanel](https://gitlab.com/seanel)