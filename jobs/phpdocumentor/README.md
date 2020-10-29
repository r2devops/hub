# 📑 PHPDocumentor

## Description

Build a complete HTML documentation based on a PHP Project using [DocBlocks](https://docs.phpdoc.org/3.0/guide/guides/docblocks.html) from [PHPDoc](https://www.phpdoc.org/).

## How to use it

1. Have a PHP Project with well documented files.
2. Edit [variables](#variables) or use a `phpdoc.dist.xml` file (see [syntax](https://docs.phpdoc.org/3.0/guide/references/configuration.html)).
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/phpdocumentor.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)

5. Well done, your job is ready to work ! 😀

!!! note 
   If you use a `phpdoc.dist.xml` you can place it anywhere in your repository. But don't forget to edit `PHPDOC_CONFIG_FILE`, so the job knows where the config file is.

## Job details

* Job name: `phpdocumentor`
* Docker image:
[`phpdoc/phpdoc:3.1`](https://hub.docker.com/r/phpdoc/phpdoc)
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PHPDOC_OUTPUT`<img width=100/> | Output directory path<img width=175/> | `/documentation_build` <img width=100/>|
| `PHPDOC_CONFIG_FILE` | Specific `phpdoc.dist.xml` file to use | ` ` |
| `PHPDOC_TITLE` | Custom title for documentation | ` ` |
| `PHPDOC_VERBOSITY` | Print more logs in the job | ` ` |
| `PHPDOC_TEMPLATE` | Template used by PHPDoc | ` ` |
| `PHPDOC_INCLUDE_HIDDEN` | Include hidden PHP files | `false` |
| `PHPDOC_IGNORE_SYMLINKS` | Ignore symbolic links to avoid loops | `false` |
| `PHPDOC_MARKERS` | Custom comment [markers](https://docs.phpdoc.org/3.0/guide/guides/running-phpdocumentor.html#Markers) | ` ` |
| `PHPDOC_OPTIONS` | Additional custom options  | ` ` |
| `PROJECT_ROOT` | PHP Project location in your repository | `/` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as) `PHPDoc Build` in
merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129). As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.
