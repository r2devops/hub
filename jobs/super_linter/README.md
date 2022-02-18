## Objective

This job uses the [github super-linter](https://github.com/github/super-linter){:target="_blank"}
which is a Simple combination of various linters to help validate the quality
of your source code. This job permit to fully integrate it in Gitlab
(super-linter is originally made for Github Actions).

More than 36 languages are supported :

| _Language_                       | _Linter_                                                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ansible**                      | [ansible-lint](https://github.com/ansible/ansible-lint){:target="_blank"}                                                                                                                        |
| **Azure Resource Manager (ARM)** | [arm-ttk](https://github.com/azure/arm-ttk){:target="_blank"}                                                                                                                                    |
| **AWS CloudFormation templates** | [cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint/){:target="_blank"}                                                                                                             |
| **C#**                           | [dotnet-format](https://github.com/dotnet/format){:target="_blank"}                                                                                                                              |
| **CSS**                          | [stylelint](https://stylelint.io/){:target="_blank"}                                                                                                                                             |
| **Clojure**                      | [clj-kondo](https://github.com/borkdude/clj-kondo){:target="_blank"}                                                                                                                             |
| **CoffeeScript**                 | [coffeelint](https://coffeelint.github.io/){:target="_blank"}                                                                                                                                    |
| **Dart**                         | [dartanalyzer](https://dart.dev/guides/language/analysis-options){:target="_blank"}                                                                                                              |
| **Dockerfile**                   | [dockerfilelint](https://github.com/replicatedhq/dockerfilelint.git){:target="_blank"}  / [hadolint](https://github.com/hadolint/hadolint){:target="_blank"}                                                        |
| **EDITORCONFIG**                 | [editorconfig-checker](https://github.com/editorconfig-checker/editorconfig-checker){:target="_blank"}                                                                                           |
| **ENV**                          | [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter){:target="_blank"}                                                                                                                |
| **Golang**                       | [golangci-lint](https://github.com/golangci/golangci-lint){:target="_blank"}                                                                                                                     |
| **Groovy**                       | [npm-groovy-lint](https://github.com/nvuillam/npm-groovy-lint){:target="_blank"}                                                                                                                 |
| **HTML**                         | [HTMLHint](https://github.com/htmlhint/HTMLHint){:target="_blank"}                                                                                                                               |
| **Java**                         | [checkstyle](https://checkstyle.org){:target="_blank"}                                                                                                                                           |
| **JavaScript**                   | [eslint](https://eslint.org/){:target="_blank"}  / [standard js](https://standardjs.com/){:target="_blank"}                                                                                                         |
| **JSON**                         | [jsonlint](https://github.com/zaach/jsonlint){:target="_blank"}                                                                                                                                  |
| **Kubeval**                      | [kubeval](https://github.com/instrumenta/kubeval){:target="_blank"}                                                                                                                              |
| **Kotlin**                       | [ktlint](https://github.com/pinterest/ktlint){:target="_blank"}                                                                                                                                  |
| **LaTeX**                        | [ChkTex](https://www.nongnu.org/chktex/){:target="_blank"}                                                                                                                                       |
| **Lua**                          | [luacheck](https://github.com/luarocks/luacheck){:target="_blank"}                                                                                                                               |
| **Markdown**                     | [markdownlint](https://github.com/igorshubovych/markdownlint-cli#readme){:target="_blank"}                                                                                                       |
| **OpenAPI**                      | [spectral](https://github.com/stoplightio/spectral){:target="_blank"}                                                                                                                            |
| **Perl**                         | [perlcritic](https://metacpan.org/pod/Perl::Critic){:target="_blank"}                                                                                                                            |
| **PHP**                          | [PHP built-in linter](https://www.php.net/){:target="_blank"} / [PHP CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer){:target="_blank"} / [PHPStan](https://phpstan.org/){:target="_blank"} / [Psalm](https://psalm.dev/){:target="_blank"} |
| **PowerShell**                   | [PSScriptAnalyzer](https://github.com/PowerShell/Psscriptanalyzer){:target="_blank"}                                                                                                             |
| **Protocol Buffers**             | [protolint](https://github.com/yoheimuta/protolint){:target="_blank"}                                                                                                                            |
| **Python3**                      | [pylint](https://www.pylint.org/){:target="_blank"} / [flake8](https://flake8.pycqa.org/en/latest/){:target="_blank"} / [black](https://github.com/psf/black){:target="_blank"}                                                      |
| **R**                            | [lintr](https://github.com/jimhester/lintr){:target="_blank"}                                                                                                                                    |
| **Raku**                         | [Raku](https://raku.org){:target="_blank"}                                                                                                                                                       |
| **Ruby**                         | [RuboCop](https://github.com/rubocop-hq/rubocop){:target="_blank"}                                                                                                                               |
| **Shell**                        | [Shellcheck](https://github.com/koalaman/shellcheck){:target="_blank"} / [executable bit check] / [shfmt](https://github.com/mvdan/sh){:target="_blank"}                                                           |
| **Snakemake**                    | [snakefmt](https://github.com/snakemake/snakefmt/){:target="_blank"} / [snakemake --lint](https://snakemake.readthedocs.io/en/stable/snakefiles/writing_snakefiles.html#best-practices){:target="_blank"}          |
| **SQL**                          | [sql-lint](https://github.com/joereynolds/sql-lint){:target="_blank"}                                                                                                                            |
| **Tekton**                       | [tekton-lint](https://github.com/IBM/tekton-lint){:target="_blank"}                                                                                                                              |
| **Terraform**                    | [tflint](https://github.com/terraform-linters/tflint){:target="_blank"} / [terrascan](https://github.com/accurics/terrascan){:target="_blank"}                                                                     |
| **Terragrunt**                   | [terragrunt](https://github.com/gruntwork-io/terragrunt){:target="_blank"}                                                                                                                       |
| **TypeScript**                   | [eslint](https://eslint.org/){:target="_blank"} / [standard js](https://standardjs.com/){:target="_blank"}                                                                                                         |
| **XML**                          | [LibXML](http://xmlsoft.org/){:target="_blank"}                                                                                                                                                  |
| **YAML**                         | [YamlLint](https://github.com/adrienverge/yamllint){:target="_blank"}                                                                                                                            |

## How to use it

1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/super_linter.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `super_linter`
* Docker image:
[`github/super-linter`](https://hub.docker.com/r/github/super-linter){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

!!! info
    This section describes the most significant variables [from this full
    list](https://github.com/github/super-linter#environment-variables){:target="_blank"}.

This job can be used without configuration. By default, it will detect files in
your repository and run relevant linter on them. You can also use variables to
customize its behavior.

* [General configuration](#general-configuration)
* [Use specific configuration for linters](#linters-configuration)
* [Enable or disable some linters](#enable-or-disable-linters)

#### General configuration

| Name | Description | Default |
| --------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ACTIONS_RUNNER_DEBUG**          | Flag to enable additional information about the linter, versions, and additional output.                                                                                   | `false`              |
| **DISABLE_ERRORS**                | Flag to have the linter complete with exit code 0 even if errors were detected.                                                                                            | `false`              |
| **FILTER_REGEX_EXCLUDE**          | Regular expression defining which files will be excluded from linting  (ex: `.*src/test.*`)                                                                                | `none`               |
| **FILTER_REGEX_INCLUDE**          | Regular expression defining which files will be processed by linters (ex: `.*src/.*`)                                                                                      | `all`                |
| **LOG_LEVEL**                     | How much output the script will generate to the console. One of `VERBOSE`, `DEBUG` or `TRACE`.                                                                             | `VERBOSE`            |
| **MULTI_STATUS**                  | A status API is made for each language that is linted to make visual parsing easier.                                                                                       | `true`               |
| **REPORT_SUITE_TEST_NAME**        | Name of test suite inside test report                   | `super_linter`       |

#### Linters configuration

| Name | Description | Default |
| --------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ANSIBLE_DIRECTORY**             | Flag to set the root directory for Ansible file location(s), relative to `DEFAULT_WORKSPACE`.                                                                              | `/ansible`           |
| **CSS_FILE_NAME**                 | Filename for [Stylelint configuration](https://github.com/stylelint/stylelint){:target="_blank"} (ex: `.stylelintrc.yml`, `.stylelintrc.yaml`)                                               | `.stylelintrc.json`  |
| **DOCKERFILE_HADOLINT_FILE_NAME** | Filename for [hadolint configuration](https://github.com/hadolint/hadolint){:target="_blank"} (ex: `.hadolintlintrc.yaml`)                                                                   | `.hadolint.yml`      |
| **ERROR_ON_MISSING_EXEC_BIT**     | If set to `false`, the `bash-exec` linter will report a warning if a shell script is not executable. If set to `true`, the `bash-exec` linter will report an arror instead.| `false`              |
| **JAVASCRIPT_ES_CONFIG_FILE**     | Filename for [eslint configuration](https://eslint.org/docs/user-guide/configuring#configuration-file-formats){:target="_blank"} (ex: `.eslintrc.yml`, `.eslintrc.json`)                     | `.eslintrc.yml`      |
| **LINTER_RULES_PATH**             | Directory for all linter configuration rules.                                                                                                                              | `.linters`    |
| **MARKDOWN_CONFIG_FILE**          | Filename for [Markdownlint configuration](https://github.com/DavidAnson/markdownlint#optionsconfig){:target="_blank"} (ex: `.markdown-lint.yml`, `.markdownlint.json`, `.markdownlint.yaml`) | `.markdown-lint.yml` |
| **PYTHON_PYLINT_CONFIG_FILE**     | Filename for [pylint configuration](https://pylint.pycqa.org/en/latest/user_guide/run.html?highlight=rcfile#command-line-options){:target="_blank"} (ex: `.python-lint`, `.pylintrc`)        | `.python-lint`       |
| **PYTHON_FLAKE8_CONFIG_FILE**     | Filename for [flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html){:target="_blank"} (ex: `.flake8`, `tox.ini`)                                                 | `.flake8`            |
| **PYTHON_BLACK_CONFIG_FILE**      | Filename for [black configuration](https://github.com/psf/black/blob/master/docs/compatible_configs.md){:target="_blank"} (ex: `.isort.cfg`, `pyproject.toml`)                               | `.python-black`      |
| **RUBY_CONFIG_FILE**              | Filename for [rubocop configuration](https://docs.rubocop.org/rubocop/configuration.html){:target="_blank"} (ex: `.ruby-lint.yml`, `.rubocop.yml`)                                           | `.ruby-lint.yml`     |
| **SNAKEMAKE_SNAKEFMT_CONFIG_FILE**| Filename for [Snakemake configuration](https://github.com/snakemake/snakefmt#configuration){:target="_blank"} (ex: `pyproject.toml`, `.snakefmt.toml`)                                       | `.snakefmt.toml`     |
| **TYPESCRIPT_ES_CONFIG_FILE**     | Filename for [eslint configuration](https://eslint.org/docs/user-guide/configuring#configuration-file-formats){:target="_blank"} (ex: `.eslintrc.yml`, `.eslintrc.json`)                     | `.eslintrc.yml`      |
| **YAML_CONFIG_FILE**              | Filename for [Yamllint configuration](https://yamllint.readthedocs.io/en/stable/configuration.html){:target="_blank"} (ex: `.yaml-lint.yml`, `.yamllint.yml`)                                | `.yaml-lint.yml`     |

!!! warning
    Please be aware that any config file specified is relative to `$LINTER_RULES_PATH`, so you have to put **all your
    templating** under the path specified. If you are curious to know what are the *default templates* files for your
    linters, they are all available in the [`TEMPLATES`](https://github.com/github/super-linter/tree/master/TEMPLATES) 
    folder

#### Enable or disable linters

!!! info "Note about `VALIDATE_[LANGUAGE]` variables from super-linter [README](https://github.com/github/super-linter#environment-variables){:target="_blank"}"
    Note: All the `VALIDATE_[LANGUAGE]` variables behave in a very specific way:

    * If none of them are passed, then they all default to true.
    * If any one of the variables are set to true, we default to leaving any unset variable to false (only validate those languages).
    * If any one of the variables are set to false, we default to leaving any unset variable to true (only exclude those languages).
    * If there are VALIDATE_[LANGUAGE] variables set to both true and false. It will fail.

    This means that if you run the linter "out of the box", all languages will be checked. But if you wish to select or exclude specific linters, we give you full control to choose which linters are run, and won't run anything unexpected.


| Name | Description | Default |
| --------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VALIDATE_ANSIBLE**              | Flag to enable or disable the linting process of the Ansible language.                                                                                                     | `true`               |
| **VALIDATE_ARM**                  | Flag to enable or disable the linting process of the ARM language.                                                                                                         | `true`               |
| **VALIDATE_BASH**                 | Flag to enable or disable the linting process of the Bash language.                                                                                                        | `true`               |
| **VALIDATE_BASH_EXEC**            | Flag to enable or disable the linting process of the Bash language to validate if file is stored as executable.                                                            | `true`               |
| **VALIDATE_CLOJURE**              | Flag to enable or disable the linting process of the Clojure language.                                                                                                     | `true`               |
| **VALIDATE_CLOUDFORMATION**       | Flag to enable or disable the linting process of the AWS Cloud Formation language.                                                                                         | `true`               |
| **VALIDATE_COFFEE**               | Flag to enable or disable the linting process of the Coffeescript language.                                                                                                | `true`               |
| **VALIDATE_CSHARP**               | Flag to enable or disable the linting process of the C# language.                                                                                                          | `true`               |
| **VALIDATE_CSS**                  | Flag to enable or disable the linting process of the CSS language.                                                                                                         | `true`               |
| **VALIDATE_DART**                 | Flag to enable or disable the linting process of the Dart language.                                                                                                        | `true`               |
| **VALIDATE_DOCKERFILE**           | Flag to enable or disable the linting process of the Docker language.                                                                                                      | `true`               |
| **VALIDATE_DOCKERFILE_HADOLINT**  | Flag to enable or disable the linting process of the Docker language.                                                                                                      | `true`               |
| **VALIDATE_EDITORCONFIG**         | Flag to enable or disable the linting process with the editorconfig.                                                                                                       | `true`               |
| **VALIDATE_ENV**                  | Flag to enable or disable the linting process of the ENV language.                                                                                                         | `true`               |
| **VALIDATE_GO**                   | Flag to enable or disable the linting process of the Golang language.                                                                                                      | `true`               |
| **VALIDATE_GROOVY**               | Flag to enable or disable the linting process of the language.                                                                                                             | `true`               |
| **VALIDATE_HTML**                 | Flag to enable or disable the linting process of the HTML language.                                                                                                        | `true`               |
| **VALIDATE_JAVA**                 | Flag to enable or disable the linting process of the language.                                                                                                             | `true`               |
| **VALIDATE_JAVASCRIPT_ES**        | Flag to enable or disable the linting process of the Javascript language. (Utilizing: eslint)                                                                              | `true`               |
| **VALIDATE_JAVASCRIPT_STANDARD**  | Flag to enable or disable the linting process of the Javascript language. (Utilizing: standard)                                                                            | `true`               |
| **VALIDATE_JSON**                 | Flag to enable or disable the linting process of the JSON language.                                                                                                        | `true`               |
| **VALIDATE_JSX**                  | Flag to enable or disable the linting process for jsx files (Utilizing: eslint)                                                                                            | `true`               |
| **VALIDATE_KOTLIN**               | Flag to enable or disable the linting process of the Kotlin language.                                                                                                      | `true`               |
| **VALIDATE_KUBERNETES_KUBEVAL**   | Flag to enable or disable the linting process of Kubernetes descriptors with Kubeval                                                                                       | `true`               |
| **VALIDATE_LATEX**                | Flag to enable or disable the linting process of the LaTeX language.                                                                                                       | `true`               |
| **VALIDATE_LUA**                  | Flag to enable or disable the linting process of the language.                                                                                                             | `true`               |
| **VALIDATE_MARKDOWN**             | Flag to enable or disable the linting process of the Markdown language.                                                                                                    | `true`               |
| **VALIDATE_OPENAPI**              | Flag to enable or disable the linting process of the OpenAPI language.                                                                                                     | `true`               |
| **VALIDATE_PERL**                 | Flag to enable or disable the linting process of the Perl language.                                                                                                        | `true`               |
| **VALIDATE_PHP**                  | Flag to enable or disable the linting process of the PHP language. (Utilizing: PHP built-in linter) (keep for backward compatibility)                                      | `true`               |
| **VALIDATE_PHP_BUILTIN**          | Flag to enable or disable the linting process of the PHP language. (Utilizing: PHP built-in linter)                                                                        | `true`               |
| **VALIDATE_PHP_PHPCS**            | Flag to enable or disable the linting process of the PHP language. (Utilizing: PHP CodeSniffer)                                                                            | `true`               |
| **VALIDATE_PHP_PHPSTAN**          | Flag to enable or disable the linting process of the PHP language. (Utilizing: PHPStan)                                                                                    | `true`               |
| **VALIDATE_PHP_PSALM**            | Flag to enable or disable the linting process of the PHP language. (Utilizing: PSalm)                                                                                      | `true`               |
| **VALIDATE_PROTOBUF**             | Flag to enable or disable the linting process of the Protobuf language.                                                                                                    | `true`               |
| **VALIDATE_PYTHON**               | Flag to enable or disable the linting process of the Python language. (Utilizing: pylint) (keep for backward compatibility)                                                | `true`               |
| **VALIDATE_PYTHON_PYLINT**        | Flag to enable or disable the linting process of the Python language. (Utilizing: pylint)                                                                                  | `true`               |
| **VALIDATE_PYTHON_FLAKE8**        | Flag to enable or disable the linting process of the Python language. (Utilizing: flake8)                                                                                  | `true`               |
| **VALIDATE_PYTHON_BLACK**         | Flag to enable or disable the linting process of the Python language. (Utilizing: black)                                                                                   | `true`               |
| **VALIDATE_POWERSHELL**           | Flag to enable or disable the linting process of the Powershell language.                                                                                                  | `true`               |
| **VALIDATE_R**                    | Flag to enable or disable the linting process of the R language.                                                                                                           | `true`               |
| **VALIDATE_RAKU**                 | Flag to enable or disable the linting process of the Raku language.                                                                                                        | `true`               |
| **VALIDATE_RUBY**                 | Flag to enable or disable the linting process of the Ruby language.                                                                                                        | `true`               |
| **VALIDATE_SHELL_SHFMT**          | Flag to enable or disable the linting process of Shell scripts. (Utilizing: shfmt)                                                                                         | `true`               |
| **VALIDATE_SNAKEMAKE_LINT**       | Flag to enable or disable the linting process of Snakefiles. (Utilizing: snakemake --lint)                                                                                 | `true`               |
| **VALIDATE_SNAKEMAKE_SNAKEFMT**   | Flag to enable or disable the linting process of Snakefiles. (Utilizing: snakefmt)                                                                                         | `true`               |
| **VALIDATE_STATES**               | Flag to enable or disable the linting process for AWS States Language.                                                                                                     | `true`               |
| **VALIDATE_SQL**                  | Flag to enable or disable the linting process of the SQL language.                                                                                                         | `true`               |
| **VALIDATE_TERRAFORM**            | Flag to enable or disable the linting process of the Terraform language.                                                                                                   | `true`               |
| **VALIDATE_TERRAFORM_TERRASCAN**  | Flag to enable or disable the linting process of the Terraform language for security related issues.                                                                       | `true`               |
| **VALIDATE_TERRAGRUNT**           | Flag to enable or disable the linting process for Terragrunt files.                                                                                                        | `true`               |
| **VALIDATE_TSX**                  | Flag to enable or disable the linting process for tsx files (Utilizing: eslint)                                                                                            | `true`               |
| **VALIDATE_TYPESCRIPT_ES**        | Flag to enable or disable the linting process of the Typescript language. (Utilizing: eslint)                                                                              | `true`               |
| **VALIDATE_TYPESCRIPT_STANDARD**  | Flag to enable or disable the linting process of the Typescript language. (Utilizing: standard)                                                                            | `true`               |
| **VALIDATE_XML**                  | Flag to enable or disable the linting process of the XML language.                                                                                                         | `true`               |
| **VALIDATE_YAML**                 | Flag to enable or disable the linting process of the YAML language.                                                                                                        | `true`               |


### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.

This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)