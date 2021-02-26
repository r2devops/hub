## Description

Spell_check is using the python program [`PySpelling`](https://github.com/facelessuser/pyspelling/) to fetch your files (by default `Markdown` files)
 and retrieve spelling errors in it, but it won't look for **grammar errors**.

PySpelling has **two alternative** spell checker to verify your files, using [`aspell`](http://aspell.net/) or [`hunspell`](https://hunspell.github.io/),
see [configuration](https://facelessuser.github.io/pyspelling/configuration/) to learn more.

!!! info
    PySpelling needs, by default, to have a configuration file. But this job will include a default configuration
    for check spelling of `Markdown` files if no configuration is given.

## How to use it

1. (Optional) Configure your PySpelling config file (see [here](https://facelessuser.github.io/pyspelling/configuration/))
2. (Optional) According to your PySpelling config, define `PYSPELLING_SPELLER` and `PYSPELLING_LANGUAGE`
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/spell_check.yml'
    ```
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

!!! note "About Hunspell"
    Hunspell can be used as an alternative the aspell, the current spelling checker tool used. In order to have
    a working job, we recommend you to replace `PYSPELLING_SPELLER` with the following string `hunspell=1.7.0-2`.

    The above hunspell version has been tested with this job, it ensures you that this will properly work. Upgrading
    this version can cause your job to be broken, do it at your own risks.

## Job details

* Job name: `spell_check`
* Docker image:
[`python:3.9.1`](https://hub.docker.com/_/python/)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PYSPELLING_LANGUAGE` <img width=100/> | Languages dictionnaries to use (separate each language by a space) <img width=175/>| `en` <img width=100/>|
| `PYSPELLING_SPELLER`  | Speller program to use | `aspell=0.60.7~20110707-6` |
| `PYSPELLING_CONFIG`  | Path to your custom `.pyspelling.yml` | ` ` |
| `PYSPELLING_OPTIONS`  | Additional options for PySpelling | ` ` |
| `SNIPPET_VERSION` | Snippet commit tag | `4cc2af8e840aff6f599a894351de62c9b29ddc69` |

!!! info
    Spell_Check is also using [`allow_failure`](https://docs.gitlab.com/ee/ci/yaml/#allow_failure) Gitlab's variable,
    which is by default true.

    You can change this option to make the pipeline fails if any spelling error is detected. See [jobs cusotmization](/use-the-hub/#jobs-customization).

!!! info
    This job use scripts and default config files in order to be plug and play. These scripts are fetched
    using the commit tag in `SNIPPET_VERSION`.

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.
The report defined as `spelling_junit.xml` is also available directly in the artifacts.
