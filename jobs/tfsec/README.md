## Objective

Analyze the security for your Terraform code with [tfsec](https://github.com/aquasecurity/tfsec). It supports many popular cloud providers, such as AWS, Azure, GCP, DigitalOcean, and [others](https://github.com/aquasecurity/tfsec#included-checks) and is and ready to use out of the box.

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `TFSEC_CHECK_DIR` | The directory to check for Terraform files. | `terraform` |
| `TFSEC_CONFIG_FILE` <img width=100/> | The path or a remote link for the configuration file. See the [documentation](https://aquasecurity.github.io/tfsec/v1.27.6/guides/configuration/config/). <img width=175/>| `tfsec.config.yml` <img width=100/>|
| `TFSEC_FORMATS` | Outputs format list. Each format should be separate by a comma and are saved as artifacts. | `sarif` |
| `TFSEC_MIN_SEVERITY` | The minimum severity to report. One of CRITICAL, HIGH, MEDIUM, LOW. | `LOW` |
| `TFSEC_REGO_DIR` | The directory to check for [custom Rego policies](https://aquasecurity.github.io/tfsec/v1.27.6/guides/rego/rego/), if you wants to add your own rules. See the [documentation](https://www.openpolicyagent.org/docs/latest/policy-language/).  | `rego_policies` |
| `TFSEC_VERSION` | The version for the tfsec CLI. | `1.27.6` |
| `ADDITIONAL_OPTIONS` | Additional options for  the tfsec CLI. | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18-alpine` |

## Job details

By default the job shows the results in the [Code Quality widget](https://docs.gitlab.com/ee/ci/testing/code_quality.html#code-quality-widget) inside the merge request. It also reports tests inside the `Test` section in the CI/CD pipeline.

## Artifacts

The result are also saved as artifacts. You can find them in the `artifacts` section of the job.  
Two formats are available by default :
- [JUnit](https://junit.org/junit5/)'s XML report to display error report directly in pipeline `Test` tab and in
merge request widget.
- [CodeClimate](https://codeclimate.com/quality)'s JSON report to display error report directly in merge request widget.

⚠️ Those report are only available if the variable `TFSEC_FORMATS` contains `sarif`.

!!! info "Formats"
    If you want to have more artifacts with other formats, you can add them in the `TFSEC_FORMATS` variable. Available formats can be found [here](https://aquasecurity.github.io/tfsec/v1.27.6/guides/usage/). All specified format will be saved in a file `tfsec-result.<format>`.

## Dependencies

The job uses the following dependencies for converting the `output` to `JUnit` or `CodeClimate`:
- [sarif-junit](https://www.npmjs.com/package/sarif-junit) tool to convert `SARIF` to `JUnit`
- [sarif-codeclimate](https://www.npmjs.com/package/sarif-codeclimate) tool to convert `SARIF` to `CodeClimate`


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@GridexX](https://gitlab.com/GridexX)
