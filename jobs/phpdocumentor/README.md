## Objective

Build a complete HTML documentation based on a PHP Project using [DocBlocks](https://docs.phpdoc.org/3.0/guide/guides/docblocks.html){:target="_blank"} from [PHPDoc](https://www.phpdoc.org/){:target="_blank"}.

## How to use it

1. Have a PHP Project with well documented files (see [how](https://docs.phpdoc.org/3.0/guide/guides/docblocks.html){:target="_blank"}).
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/phpdocumentor.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

4. Well done, your job is ready to work ! 😀

!!! info

    This job allows you to use a configuration file named `phpdoc.dist.xml` (see [syntax](https://docs.phpdoc.org/3.0/guide/references/configuration.html){:target="_blank"}).
    By default, PHPDoc will search for a configuration file in `PROJECT_ROOT` and will use it if the file does exist. But you can customize the location to `phpdoc.dist.xml` by editing `PHPDOC_CONFIG_FILE`.

## Job details

* Job name: `phpdocumentor`
* Docker image:
[`phpdoc/phpdoc:3.1`](https://hub.docker.com/r/phpdoc/phpdoc){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PHPDOC_OUTPUT`<img width=100/> | Output directory path<img width=175/> | `website_build/` <img width=100/>|
| `PHPDOC_CONFIG_FILE` | Specific `phpdoc.dist.xml` file to use | ` ` |
| `PHPDOC_TITLE` | Custom title for documentation | ` ` |
| `PHPDOC_VERBOSITY` | Print more logs in the job | ` ` |
| `PHPDOC_TEMPLATE` | Template used by PHPDoc | ` ` |
| `PHPDOC_INCLUDE_HIDDEN` | Include hidden PHP files | `false` |
| `PHPDOC_IGNORE_SYMLINKS` | Ignore symbolic links to avoid loops | `false` |
| `PHPDOC_MARKERS` | Custom comment [markers](https://docs.phpdoc.org/3.0/guide/guides/running-phpdocumentor.html#Markers){:target="_blank"} | ` ` |
| `PHPDOC_OPTIONS` | Additional custom options  | ` ` |
| `PROJECT_ROOT` | PHP Project location in your repository | `/` |

### Artifacts

When the job is successful, the documentation build result is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `PHPDoc Build` in merge requests.  Exposition of artifact currently works
    only if you keep `PHPDOC_OUTPUT` default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.
