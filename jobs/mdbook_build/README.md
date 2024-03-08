## Objective

The markdown documentation builder named [mdBook](https://github.com/rust-lang/mdBook){:target="_blank"} is done in Rust. It is used in documentation like [Rust by example](https://doc.rust-lang.org/rust-by-example/){:target="_blank"}.
This job would build the documentation of a mdBook project.

## How to use it

1. Ensure that you initialized a mdBook project with the `mdbook init` command. If you need more information about mdBook, please check the [documentation](https://github.com/rust-lang/mdBook){:target="_blank"}.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative path in your repository to your mdBook project. <img width=175/>| `.` <img width=100/>|
| `DOCUMENTATION_OUTPUT` <img width=100/> | Relative path in your repository to the output produced by the `mdbook` build script. <img width=175/>| `website_build` <img width=100/>|
| `MDBOOK_VERSION` <img width=100/> | Version of `mdBook` used, by default the job will use the latest stable version of `mdBook`. <img width=175/>| ` ` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `1.57-buster`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
