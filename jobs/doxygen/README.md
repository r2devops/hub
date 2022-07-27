## Objective

This job generates documentation from popular programming languages
in different output format using this tool [Doxygen](https://www.doxygen.nl/){:target="_blank"}

Programming languages supported by Doxygen include C, C++, C#, D, Fortran, IDL, Java, Objective-C, Perl, PHP, Python, and VHDL.
Other languages can be supported with additional code.
## How to use it


1. Ensure that your source code is documenting using [Doxygen syntax](https://www.doxygen.nl/manual/docblocks.html){:target="_blank"}
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `INPUT` <img width=650px>               | Input directory of your source files <img width=125>| `.` <img width=300>|
| `DOXYGEN_CONFIGFILE`               | Name of your Doxygen configuration file| `Doxyfile`|
| `DOXYGEN_PROJECT_NAME`               | Name of your Doxygen project, for the documentation title| `$CI_PROJECT_NAME`  (Gitlab project name) |
| `DOXYGEN_INPUT`               | The path to your documented source files| `.`|
| `DOXYGEN_OUTPUT_DIRECTORY`               | The path of your documentation generated| `.`|
| `DOXYGEN_OUTPUT_LANGUAGE`               | The language in which your documentation is written| `English`|
| `DOXYGEN_GENERATE_LATEX`               | Set to YES if you want to generate LaTeX documentation | `YES`|
| `DOXYGEN_LATEX_OUTPUT`               | The path of your LaTeX documentation generated| `latex/`|
| `DOXYGEN_GENERATE_HTML`               | Set to YES if you want to generate HTML documentation | `YES`|
| `DOXYGEN_HTML_OUTPUT`               | The path of your LaTeX documentation generated| `website_build/`|
| `DOXYGEN_HTML_EXTRA_STYLESHEET`               | The path of additional user-defined cascading style sheets [CSS](https://www.w3schools.com/css/)| ` `|
| `DOXYGEN_RECURSIVE`               | Specify whether or not subdirectories should be searched for input files as well| `NO`|
| `DOXYGEN_EXCLUDE`               | Specify files and/or directories that should be excluded from the INPUT source files| ` `|
| `DOXYGEN_EXCLUDE_PATTERNS`               | If the value of the INPUT tag contains directories, you can use the EXCLUDE_PATTERNS tag to specify one or more wildcard patterns to exclude certain files from those directories.| ` `|
| `DOXYGEN_PROJECT_LOGO`               | The path of the logo (max-height:55px, max-width:200px) to include in your documentation generated| ` `|
| `IMAGE_TAG` | The default tag for the docker image | `3.12.1`  |


!!! note
    All paths defined in variables are starting from the root of your repository.

## Artifacts

When the job is successful, the build of your documentation is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Doyxgen build` in merge requests.
    Exposition of artifact currently works only if you keep
    `DOXYGEN_HTML_OUTPUT` and/or `DOXYGEN_LATEX_OUTPUT` default value because
    of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)
