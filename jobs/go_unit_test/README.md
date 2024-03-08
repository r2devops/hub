## Description

Execute your golang unit tests and have the results fully integrated with the various areas of the Gitlab UI plus provide code coverage data in pipelines and badges.

## How to use it

1. The job of course assumes that you have written your tests 
2. Choose a version in [version list](https://docs.r2devops.io/get-started/use-templates/#versioning)
3. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the
   [jobs customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
5. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `UT_WORK_DIR` | If for any reason (monorepo for example) your go project is not at root of project, specify the relative path to the project | `$CI_PROJECT_DIR` |
| `UT_TEST_CMD` | Customise the test command if needed | `go test -v` |
| `IMAGE_TAG` | The default tag for the docker image | `1.19.3`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@seanel](https://gitlab.com/seanel)
