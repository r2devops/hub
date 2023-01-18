## Objective

MegaLinter is an Open-Source tool for CI/CD workflows that analyzes the consistency of your code, IAC, configuration, and scripts in your repository sources, to ensure all your projects sources are clean and formatted whatever IDE/toolbox is used by their developers, powered by [OX security](https://www.ox.security/?ref=r2devops).

[MegaLinter](https://github.com/oxsecurity/megalinter/){:target="_blank"} supports [50 languages, 22 formats, 20 tooling
formats](https://github.com/oxsecurity/megalinter#supported-linters) and it's ready
to use out of the box.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the
   [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed
   version](#changelog) instead of `latest`.
1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Well done, your job is ready to work ! 😀

## Behavior

By default, this job will run MegaLinter on your project, lint all the files and perform a code review with [CodeClimate](https://codeclimate.com/quality).

!!! info "How can i see errors in the report?" 
   While working on a merge_request, the `mega_linter` report summary will be displayed on the overview page inside the `Test summary` and `Code Quality` tabs.
   
!!! info "How can i get results summary directly in the merge request comments?"
   MegaLinter could also write comments directly in the merge request comments section (see `GITLAB_COMMENT_REPORTER` variable). 
   ⚠️ You need to configure an access token between GitLab and MegaLinter, see the [documentation](https://oxsecurity.github.io/megalinter/latest/reporters/GitlabCommentReporter/#configuration){:target="_blank"}.
## Variables

!!! info
    This section describes the most significant variables [from this full
    list](https://oxsecurity.github.io/megalinter/latest/configuration/){:target="_blank"}.

This job can be used without configuration. By default, it will detect files in
your repository and run relevant linter on them. You can also use variables to
customize its behavior.

## General configuration

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DEFAULT_WORKSPACE` <img width=100/> | Directory where the linter will work <img width=175/>| `${CI_PROJECT_DIR}` <img width=100/>|
| `DEFAULT_BRANCH`| Default branch of your project | `${CI_DEFAULT_BRANCH}` |
| `FILTER_REGEX_EXCLUDE` | Regex in order to exclude specific files | ` ` |
| `LINTER_RULES_PATH` | Directory where are stored linters configuration | `.linters` |
| `MEGALINTER_CONFIG` | MegaLinter configuration file location | `.mega_linter.yml` |
| `VALIDATE_ALL_CODEBASE` | Whether linters should only go through **edited** or **new** files | `true` |
| `REPORT_OUTPUT_FOLDER` | Folder where are stored all the reports | `megalinter-reports` |
| `CONVERTED_OUTPUT_FOLDER` | Folder where are stored `CodeClimate` reports | `converted-xml.report` |
|`GITLAB_COMMENT_REPORTER` | Posts Mega-Linter results summary in the comments of the related merge request ([⚠️ GitLab API access require](https://oxsecurity.github.io/megalinter/latest/reporters/GitlabCommentReporter/#configuration){:target="_blank"}) | `true` |
| `DISABLE_LINTERS` | Comma separated list of linters to be disabled | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `v6.13.0` |

## Optimize MegaLinter

MegaLinter provides flavored images with pre-defined linters for most of your
projects, you will find the complete list
[here](https://github.com/oxsecurity/megalinter#flavors).

By using a flavor instead of the default image, you'll be able to optimize the
docker image size and your pipeline. If any of the flavors is matching your
project type, all you have to do is overriding the image used in the job, like
this:

```yaml
mega_linter:
  # Replace FLAVOR by the one matching your project
  image: oxsecurity/megalinter-<flavor>:${IMAGE_TAG}
```

## Artifacts

- [CodeClimate](https://codeclimate.com/quality)'s JSON report to display error report directly in merge request widget.

## Dependencies
The job uses the following dependencies for converting the `output` to `CodeClimate`:
- [sarif-codeclimate](https://www.npmjs.com/package/sarif-codeclimate) tool to convert `SARIF` to `CodeClimate`

## Author and contributors
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@protocole](https://gitlab.com/Protocole)

It was updated in september 2022 by [@GridexX](https://gitlab.com/GridexX) with the help of [@nvuillam](https://github.com/nvuillam)