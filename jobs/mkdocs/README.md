## Objective

Build HTML documentation form Markdown source using
[Mkdocs](https://www.mkdocs.org/){:target="_blank"}. All requirements to use [Material for
Mkdocs](https://squidfunk.github.io/mkdocs-material/){:target="_blank"} are ready to use.

## How to use it

1. Prepare your project with Mkdocs configuration file and sources files as
   described in [Mkdocs
   documentation](https://www.mkdocs.org/#getting-started){:target="_blank"}. In your repository,
   documentation files must be organized as follows:

    ```
    /mkdocs.yml # This is your configuration file
    /docs/      # This folder contains all your documentation markdown files
    ```
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/mkdocs.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `mkdocs`
* Docker image:
[`squidfunk/mkdocs-material`](https://hub.docker.com/r/squidfunk/mkdocs-material){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `MKDOCS_OUTPUT_PATH` | Output directory path | `website_build/` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"} `Mkdocs build` in
merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}. As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.
