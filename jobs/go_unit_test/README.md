## Description

Execute your golang unit tests and have the results fully integrated with the various areas of the Gitlab UI plus provide code coverage data in pipelines and badges.

## How to use it

1. The job of course assumes that you have written your tests 
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:
    ```yaml
    include:
    - remote: 'https://jobs.r2devops.io/go_unit_test.yml'
    ```
4. If you need to customize the job (stage, variables, ...) 👉 check the
   [jobs customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `UT_WORK_DIR` | If for any reason (monorepo for example) your go project is not at root of project, specify the relative path to the project | `$CI_PROJECT_DIR` |
| `UT_TEST_CMD` | Customise the test command if needed | `go test -v` |
