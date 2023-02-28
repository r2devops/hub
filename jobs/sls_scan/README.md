## Objective

This job uses the [ShiftLeftSecurity sast scan](https://github.com/ShiftLeftSecurity/sast-scan){:target="_blank"} which is a combination of various vulnerability scanners for different languages to help detect those in your project. This job permit to fully integrate it in Gitlab (sls-scan was developed to be used as a pre-commit and in CI directly).

!!! info
    There are 27 different languages supported(👉 [full list](https://github.com/ShiftLeftSecurity/sast-scan#bundled-tools){:target="_blank"})

!!! summary "sls_scan license"
    [ShiftLeftSecurity sast scan](https://github.com/ShiftLeftSecurity/sast-scan){:target="_blank"} tool is distributed under the [GPL-3.0-or-later license](https://github.com/ShiftLeftSecurity/sast-scan/blob/master/LICENSE)

## How to use it

1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
5. Well done, your job is ready to work ! 😀

!!! info
    By default, the job will fail if it finds minimum the following number of vulnerabilities:
    More about this [here](https://github.com/ShiftLeftSecurity/sast-scan/blob/6ee41bdc7ae3462e909a745ef7c8463c5229e5ef/lib/config.py#L1339){:target="_blank"}

```python
build_break_rules = {
    "default": {"max_critical": 0, "max_high": 2, "max_medium": 5},
    "Secrets Audit": {"max_critical": 0, "max_high": 0, "max_medium": 1},
    "depscan": {"max_critical": 0,"max_high": 2,"max_medium": 5},
}
```
## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `SCAN_OPTIONS` | If you want to add [additional arguments](https://appthreat.com/en/latest/getting-started/?h=command#command-line-arguments) for `scan` | ` ` |
| `ENABLE_BUILD` | The option to use `--build` with the `scan` command | `true` |
| `SLS_TYPE` | If you want to specify a specific scanner to use | ` ` |
| `OUTPUT_PATH` | Path to scan output folder | `sls_scan_report/` |
| `IMAGE_TAG` | The default tag for the docker image | `v1.15.1`  |

## Artifacts

Scan result is available as artifact, and all HTML reports are merged into one single HTML report

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `ShiftLeft security scan` in merge requests.  Exposition of artifact
    currently works only if you keep `OUTPTUT_PATH` default value because of
    [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.

## Bundled tools

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



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)
