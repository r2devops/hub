## Objective

Build a package's documentation for local package and all dependencies. Check the doc here 👉 [cargo-doc](https://doc.rust-lang.org/cargo/commands/cargo-doc.html) for more information.
## How to use it

1. Ensure that your project has `Cargo.toml` file and its members folders are hierarchically below the workspace root.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| ONLY_LIB | Generate documentation of current library only | `false` |
| PROJECT_ROOT | Relative to root of your repository, it is the path to your rust project | `.` |
| RELEASE_MODE | Generate documentation with optimization for release. See the release profile here [release profile](https://doc.rust-lang.org/cargo/reference/profiles.html#release) | `true` |
| OUTPUT_FOLDER | Directory where are output files | `website_build` |
| ADDITIONAL_OPTIONS | Possibility to add more options into the command | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `1.57-buster`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)
