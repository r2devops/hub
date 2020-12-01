# 🔗 Links Checker

## Description

Using this job you will be able to detect most (see [here](#types-of-link-verified)) broken links in your **Markdown** or **HTML** files.

It uses the tool [`Liche`](https://github.com/raviqqe/liche){:target="_blank"} in [Go](https://golang.org/){:target="_blank"} to test and find the links in your documents. In its default state, this job will analyze your whole project for eligible files to verify.

## How to use it

1. Have `.md` or `.html` files in your project
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/links_checker.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `links_checker`
* Docker image:
[`peterevans/liche:1.1.1`](https://hub.docker.com/r/peterevans/liche){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `LICHE_DIRECTORY` <img width=450/> | Path to the directory to be scanned | ` ` |
| `LICHE_FILES` | A list of files (separated with spaces) to scan. It can be used with `LICHE_DIRECTORY` | ` ` |
| `LICHE_EXCLUDE` | A [regular expression](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"} | ` ` |
| `LICHE_PRINT_OK` | In addition to broken links, it will add not-broken links in the report (see [artifacts](#artifacts)) | `true` |
| `LICHE_RECURSIVE` | When `LICHE_DIRECTORY` is filled it will search for files recursively  | `true` |
| `FAIL_ON_BROKEN` | Make your pipeline fails when a broken link is found | `false` |
| `LICHE_OPTIONS` | Additional options (see [options](https://github.com/raviqqe/liche){:target="_blank"}) | ` ` |
| `REPORT_OUTPUT` | Report file's name | `junit-report.xml` |

### Types of link verified

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.
