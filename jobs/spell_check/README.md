## Description

Spell_check is using the python program [`PySpelling`](https://github.com/facelessuser/pyspelling/){:target="_blank"} to fetch your files (by default `Markdown` files)
 and retrieve spelling errors in it, but it won't look for **grammar errors**.

PySpelling has **two alternative** spell checker to verify your files, using [`aspell`](http://aspell.net/) or [`hunspell`](https://hunspell.github.io/){:target="_blank"},
see [configuration](https://facelessuser.github.io/pyspelling/configuration/){:target="_blank"} to learn more.

!!! info
    PySpelling needs, by default, to have a configuration file. But this job will include a default configuration
    for check spelling of `Markdown` files if no configuration is given.

## How to use it

1. (Optional) Configure your PySpelling config file (see [here](#configuration))
2. (Optional) According to your PySpelling config, define `PYSPELLING_SPELLER` and `PYSPELLING_LANGUAGE`
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
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
[`python:3.10-buster`](https://hub.docker.com/_/python/){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PYSPELLING_LANGUAGE` <img width=100/> | Languages dictionnaries to use (separate each language by a space) <img width=175/>| `en` <img width=100/>|
| `PYSPELLING_SPELLER`  | Speller program to use | `aspell=0.60.7~20110707-6+deb10u1` |
| `PYSPELLING_CONFIG`  | Path to your custom `.pyspelling.yml` | ` ` |
| `PYSPELLING_OPTIONS`  | Additional options for PySpelling | ` ` |
| `SNIPPET_VERSION` | Snippet commit tag | `4cc2af8e840aff6f599a894351de62c9b29ddc69` |

!!! info
    Spell_Check is also using [`allow_failure`](https://docs.gitlab.com/ee/ci/yaml/#allow_failure){:target="_blank"} Gitlab's variable,
    which is by default true.
    You can change this option to make the pipeline fails if any spelling error is detected. See [jobs customization](/use-the-hub/#jobs-customization).

!!! info
    This job use scripts and default config files in order to be plug and play. These scripts are fetched
    using the commit tag in `SNIPPET_VERSION`.

### Configuration

#### Default configuration


^^PySpelling can be used:^^

- [x] With a default configuration (provided by the job)
In this case, you have nothing to do, we handle everything 🤝! To do that, we use a GitLab snippet, the source code is available [here](https://gitlab.com/r2devops/hub/-/snippets/2078950){:target="_blank"}.

- [x] With a custom one (local `.pyspelling` file in the project)
In this case you can have your custom configuration file. **Don't know how to do it ?
See [here](https://facelessuser.github.io/pyspelling/configuration/){:target="_blank"}** and you can start from our
[snippet](https://gitlab.com/r2devops/hub/-/snippets/2078950/raw/master/.pyspelling.yml){:target="_blank"}.

#### 📖 Example to add a dictionary and personal wordlists
This configuration allows you to have a dictionary, in order to improve the dictionary of PySpelling.
You have to choose the option 2 above to do that.

^^Then, follow these steps:^^

1. If not already, download this configuration sample [here](https://gitlab.com/r2devops/hub/-/snippets/2078950/raw/master/.pyspelling.yml){:target="_blank"} or create your own.
1. Move it into your project
1. Update the variable `PYSPELLING_CONFIG` with the path to your config file
1. Create a `dictionary.txt` file containing a list of words separated by newlines, it will define your dictionary
1. Add this block below in the configuration file and replace `path/to/dictionary` by the location of your dictionary.

```yaml
  aspell:
    lang: en
    d: en_US
  dictionary:
    wordlists:
    - path/to/dictionary.txt
    output: dictionary.dic
  pipeline:
  - pyspelling.filters.context:
```
1. Ready to run 🚀

!!! info
    If you want to custom even more your dictionary, take a look on the [official documentation](https://facelessuser.github.io/pyspelling/configuration/#dictionaries-and-personal-wordlists){:target="_blank"}



### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.
The report defined as `spelling_junit.xml` is also available directly in the artifacts.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)