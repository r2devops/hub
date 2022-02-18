## Objective

This job will compile local packages and all of their dependencies on Rust project.

## How to use it

1. Ensure that your project have a [`cargo.toml`](https://doc.rust-lang.org/cargo/reference/manifest.html){:target="_blank"} file which contains the requirements.
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/cargo_build.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `cargo_build`
* Docker image:
[`rust:1.57-buster`](https://hub.docker.com/r/_/rust)
* Default stage: `build`
* When: `always`

### Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `RELEASE_MODE` | Build optimized artifacts with the release profile. See also the [--profile](https://doc.rust-lang.org/cargo/commands/cargo-build.html#compilation-options) option for choosing a specific profile by name. | `true` |
| `CARGO_EXCLUDE` | Exclusion of packages in the build process, separated by `,`. Must be used in conjunction with the `CARGO_WORKSPACE` flag. | ` ` |
| `CARGO_INCLUDE` | Inclusion of packages in the build process, separated by `,` | ` ` | 
| `PROJECT_ROOT` | Relative path to the directory containing `cargo.toml` | `.` |
| `CARGO_WORKSPACE` | Build all members in the workspace | `false` |
| `OUTPUT_DIR` | Directory for all generated artifacts and intermediate files | `target` | 
| `ADDITIONAL_OPTIONS` | [Additional options](https://doc.rust-lang.org/cargo/commands/cargo-build.html) available for the user, they are added just after the build command | ` ` | 

This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexiaognard](https://gitlab.com/alexiaognard)