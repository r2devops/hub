# 📑 PHPDocumentor

## Description

Build a complete HTML documentation based on a PHP Project using [DocBlocks](https://docs.phpdoc.org/3.0/guide/guides/docblocks.html) from [PHPDoc](https://www.phpdoc.org/).

## How to use it

1. Have a PHP Project with well documented files (see [how](https://docs.phpdoc.org/3.0/guide/guides/docblocks.html)).
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/phpdocumentor.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

4. Well done, your job is ready to work ! 😀

!!! info 

    This job allows you to use a configuration file named `phpdoc.dist.xml` (see [syntax](https://docs.phpdoc.org/3.0/guide/references/configuration.html)). 
    By default, PHPDoc will search for a configuration file in `PROJECT_ROOT` and will use it if the file does exist. But you can customize the location to `phpdoc.dist.xml` by editing `PHPDOC_CONFIG_FILE`.

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
