## Objective

Clippy runs a format check onto your Rust project and logs any unexpected linting warning or error in your project into the pipeline.

## How to use it

1. By default, the job will not fail when encountering warnings or errors. If you want the job to fail, change `ADDITIONAL_OPTIONS` value to `-- -D clippy::all`.
1. If you want to add more options into the `clippy` command, please check the official [documentation](https://github.com/rust-lang/rust-clippy#readme){:target="_blank"}.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization){:target="_blank"}
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative to root of your repository, it is the path to your rust project <img width=175/>| `.` <img width=100/>|
| `ADDITIONAL_OPTIONS` <img width=100/> | Possibility to add more options into the command <img width=175/>| `-- -W clippy::all` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image | `1.57-buster`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
