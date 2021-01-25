## Description

This job uses the [ShiftLeftSecurity sast scan](https://github.com/ShiftLeftSecurity/sast-scan){:target="_blank"} which is a combination of various vulnerability scanners for different languages to help detect those in your project. This job permit to fully integrate it in Gitlab (sls-scan was developped to be used as a pre-commit and in CI directly).

!!! info
    There are 27 different languages supported(👉 [full list](https://github.com/ShiftLeftSecurity/sast-scan#bundled-tools){:target="_blank"})

## How to use it

1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
2. Choose a version in [version list](#versions)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/sls_scan.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `sls_scan`
* Docker image:
[`shiftleft/sast-scan`](https://hub.docker.com/r/_/shiftleft/sast-scan){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `SLS_TYPE` <img width=450/> | If you want to specify a specific scanner to use | ` ` |
| `STOP_ON_VULN` | If you want the job to stop on the first vulnerability detected | `false` |

### Artifacts

!!! info
    Currently, sls_scan isn't integrated in a merge request widget, so we
    create an exposed artifact containing results.

You can view the report by languages when browsing through the published
artifact and clicking on the HTML outputs in your browser.

### Bundled tools

| Programming Language | Tools                               |
| -------------------- | ----------------------------------- |
| ansible              | ansible-lint                        |
| apex                 | pmd                                 |
| arm                  | checkov                             |
| aws                  | checkov                             |
| bash                 | shellcheck                          |
| bom                  | cdxgen                              |
| credscan             | gitleaks                            |
| depscan              | dep-scan                            |
| go                   | gosec, staticcheck                  |
| groovy               | find-sec-bugs                       |
| java                 | cdxgen, gradle, find-sec-bugs, pmd  |
| jsp                  | pmd, find-sec-bugs                  |
| json                 | jq, jsondiff, jsonschema            |
| kotlin               | detekt, find-sec-bugs               |
| scala                | find-sec-bugs                       |
| kubernetes           | checkov, kubesec, kube-score        |
| nodejs               | cdxgen, njsscan, eslint, yarn, rush |
| php                  | psalm, phpstan (ide only)           |
| plsql                | pmd                                 |
| python               | cfg-scan (\*), bandit, cdxgen       |
| ruby                 | dep-scan                            |
| rust                 | cdxgen                              |
| serverless           | checkov                             |
| terraform            | checkov, tfsec                      |
| Visual Force (vf)    | pmd                                 |
| Apache Velocity (vm) | pmd                                 |
| yaml                 | yamllint                            |
