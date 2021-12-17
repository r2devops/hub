## Objective

Cargo_doc aims to generate rustdoc for your project

## How to use it

1. <Your steps>
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/cargo_doc.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `cargo_doc`
* Docker image:
[`rust:1.57-buster`](https://hub.docker.com/r/_/rust)
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| ONLY_LIB | Generate documentation of current library only | `false` | 
| PROJECT_ROOT | Relative to root of your repository, it is the path to your rust project | `.` | 
| RELEASE_MODE | Generate documentation with optimization for release | `true` | 
| OUTPUT_FOLDER | Directory where are output files | `website_build` | 
| ADDITIONAL_OPTIONS | Possibility to add more options into the command | ` ` | 
