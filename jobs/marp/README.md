## Objective

Build HTML slides form Markdown using [Marp](https://marp.app/){:target="_blank"}.


## How to use it

1. Prepare your project with markdown files (.md files) under a default `slides` root directory (it could be another folder, but the name must be change in the `$MARP_INPUT_PATH` variable).
    
    !!! warning
        if the directory specified doesn't exists or is empty, the job will fails.


2. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/marp.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

4. Well done, your job is ready to work ! 😀
    


## Job details

* Job name: `marp`
* Docker image:
[`zenika/alpine-chrome:89-with-node-14`](https://hub.docker.com/r/zenika/alpine-chrome){:target="_blank"}
* Default stage: `build`
* When: `always`


### Variables

!!! note
    `MARP_INPUT_PATH` is relative and start from the root of your
    repository.  
    `MARP_OUTPUT_PATH` depends on the environment variable `CI_PROJECT_DIR`


| Name | Description | Default |
| ---- | ----------- | ------- |
| `MARP_INPUT_PATH` | Input directory path | `slides/` |
| `MARP_OUTPUT_PATH` | Output directory path | `website_build/` |
| `GENERATE_PDF` | Should generate pdf files | `true` |
| `MARP_ADDITIONNAL_OPTIONS` | Other [options](https://github.com/marp-team/marp-cli#by-cli-option){:target="_blank"} you may want to use with Marp | ` ` |
| `NPM_INSTALL_DIR` | Custom installation directory for `npm` | `.npm-global/` |
| `CHROME_PATH` | Custom path for chromium (needed to avoid permission error on generating pdf) | `/usr/bin/chromium-browser` |


### Artifacts

When the job is successful, the build of your documentation is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `marp build` in merge requests.
    Exposition of artifact currently works only if you keep `MARP_OUTPUT_PATH`
    default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.
