# 🔎 Super-linter

## Description

This job uses the [github super-linter](https://github.com/github/super-linter)
which is a Simple combination of various linters to help validate the quality
of your source code. This job permit to fully integrate it in Gitlab
(super-linter is originally made for Github Actions).

More than 36 languages are supported :

| _Language_                       | _Linter_                                                                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ansible**                      | [ansible-lint](https://github.com/ansible/ansible-lint)                                                                                                                        |
| **Azure Resource Manager (ARM)** | [arm-ttk](https://github.com/azure/arm-ttk)                                                                                                                                    |
| **AWS CloudFormation templates** | [cfn-lint](https://github.com/aws-cloudformation/cfn-python-lint/)                                                                                                             |
| **C#**                           | [dotnet-format](https://github.com/dotnet/format)                                                                                                                              |
| **CSS**                          | [stylelint](https://stylelint.io/)                                                                                                                                             |
| **Clojure**                      | [clj-kondo](https://github.com/borkdude/clj-kondo)                                                                                                                             |
| **CoffeeScript**                 | [coffeelint](https://coffeelint.github.io/)                                                                                                                                    |
| **Dart**                         | [dartanalyzer](https://dart.dev/guides/language/analysis-options)                                                                                                              |
| **Dockerfile**                   | [dockerfilelint](https://github.com/replicatedhq/dockerfilelint.git) / [hadolint](https://github.com/hadolint/hadolint)                                                        |
| **EDITORCONFIG**                 | [editorconfig-checker](https://github.com/editorconfig-checker/editorconfig-checker)                                                                                           |
| **ENV**                          | [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter)                                                                                                                |
| **Golang**                       | [golangci-lint](https://github.com/golangci/golangci-lint)                                                                                                                     |
| **Groovy**                       | [npm-groovy-lint](https://github.com/nvuillam/npm-groovy-lint)                                                                                                                 |
| **HTML**                         | [HTMLHint](https://github.com/htmlhint/HTMLHint)                                                                                                                               |
| **Java**                         | [checkstyle](https://checkstyle.org)                                                                                                                                           |
| **JavaScript**                   | [eslint](https://eslint.org/) / [standard js](https://standardjs.com/)                                                                                                         |
| **JSON**                         | [jsonlint](https://github.com/zaach/jsonlint)                                                                                                                                  |
| **Kubeval**                      | [kubeval](https://github.com/instrumenta/kubeval)                                                                                                                              |
| **Kotlin**                       | [ktlint](https://github.com/pinterest/ktlint)                                                                                                                                  |
| **LaTeX**                        | [ChkTex](https://www.nongnu.org/chktex/)                                                                                                                                       |
| **Lua**                          | [luacheck](https://github.com/luarocks/luacheck)                                                                                                                               |
| **Markdown**                     | [markdownlint](https://github.com/igorshubovych/markdownlint-cli#readme)                                                                                                       |
| **OpenAPI**                      | [spectral](https://github.com/stoplightio/spectral)                                                                                                                            |
| **Perl**                         | [perlcritic](https://metacpan.org/pod/Perl::Critic)                                                                                                                            |
| **PHP**                          | [PHP built-in linter](https://www.php.net/) / [PHP CodeSniffer](https://github.com/squizlabs/PHP_CodeSniffer) / [PHPStan](https://phpstan.org/) / [Psalm](https://psalm.dev/) |
| **PowerShell**                   | [PSScriptAnalyzer](https://github.com/PowerShell/Psscriptanalyzer)                                                                                                             |
| **Protocol Buffers**             | [protolint](https://github.com/yoheimuta/protolint)                                                                                                                            |
| **Python3**                      | [pylint](https://www.pylint.org/) / [flake8](https://flake8.pycqa.org/en/latest/) / [black](https://github.com/psf/black)                                                      |
| **R**                            | [lintr](https://github.com/jimhester/lintr)                                                                                                                                    |
| **Raku**                         | [Raku](https://raku.org)                                                                                                                                                       |
| **Ruby**                         | [RuboCop](https://github.com/rubocop-hq/rubocop)                                                                                                                               |
| **Shell**                        | [Shellcheck](https://github.com/koalaman/shellcheck) / [executable bit check] / [shfmt](https://github.com/mvdan/sh)                                                           |
| **Snakemake**                    | [snakefmt](https://github.com/snakemake/snakefmt/) / [snakemake --lint](https://snakemake.readthedocs.io/en/stable/snakefiles/writing_snakefiles.html#best-practices)          |
| **SQL**                          | [sql-lint](https://github.com/joereynolds/sql-lint)                                                                                                                            |
| **Tekton**                       | [tekton-lint](https://github.com/IBM/tekton-lint)                                                                                                                              |
| **Terraform**                    | [tflint](https://github.com/terraform-linters/tflint) / [terrascan](https://github.com/accurics/terrascan)                                                                     |
| **Terragrunt**                   | [terragrunt](https://github.com/gruntwork-io/terragrunt)                                                                                                                       |
| **TypeScript**                   | [eslint](https://eslint.org/) / [standard js](https://standardjs.com/)                                                                                                         |
| **XML**                          | [LibXML](http://xmlsoft.org/)                                                                                                                                                  |
| **YAML**                         | [YamlLint](https://github.com/adrienverge/yamllint)                                                                                                                            |

## How to use it

1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/super_linter.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `super_linter`
* Docker image:
[`github/super-linter`](https://hub.docker.com/r/github/super-linter)
* Default stage: `static_tests`
* When: `always`

### Variables

!!! info
    This section describes the most significant variables [from this full
    list](https://github.com/github/super-linter#environment-variables).

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

#### Linters configuration

| Name | Description | Default |
| --------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ANSIBLE_DIRECTORY**             | Flag to set the root directory for Ansible file location(s), relative to `DEFAULT_WORKSPACE`.                                                                              | `/ansible`           |
| **CSS_FILE_NAME**                 | Filename for [Stylelint configuration](https://github.com/stylelint/stylelint) (ex: `.stylelintrc.yml`, `.stylelintrc.yaml`)                                               | `.stylelintrc.json`  |
| **DOCKERFILE_HADOLINT_FILE_NAME** | Filename for [hadolint configuration](https://github.com/hadolint/hadolint) (ex: `.hadolintlintrc.yaml`)                                                                   | `.hadolint.yml`      |
| **ERROR_ON_MISSING_EXEC_BIT**     | If set to `false`, the `bash-exec` linter will report a warning if a shell script is not executable. If set to `true`, the `bash-exec` linter will report an arror instead.| `false`              |
| **JAVASCRIPT_ES_CONFIG_FILE**     | Filename for [eslint configuration](https://eslint.org/docs/user-guide/configuring#configuration-file-formats) (ex: `.eslintrc.yml`, `.eslintrc.json`)                     | `.eslintrc.yml`      |
| **LINTER_RULES_PATH**             | Directory for all linter configuration rules.                                                                                                                              | `.github/linters`    |
| **MARKDOWN_CONFIG_FILE**          | Filename for [Markdownlint configuration](https://github.com/DavidAnson/markdownlint#optionsconfig) (ex: `.markdown-lint.yml`, `.markdownlint.json`, `.markdownlint.yaml`) | `.markdown-lint.yml` |
| **PYTHON_PYLINT_CONFIG_FILE**     | Filename for [pylint configuration](https://pylint.pycqa.org/en/latest/user_guide/run.html?highlight=rcfile#command-line-options) (ex: `.python-lint`, `.pylintrc`)        | `.python-lint`       |
| **PYTHON_FLAKE8_CONFIG_FILE**     | Filename for [flake8 configuration](https://flake8.pycqa.org/en/latest/user/configuration.html) (ex: `.flake8`, `tox.ini`)                                                 | `.flake8`            |
| **PYTHON_BLACK_CONFIG_FILE**      | Filename for [black configuration](https://github.com/psf/black/blob/master/docs/compatible_configs.md) (ex: `.isort.cfg`, `pyproject.toml`)                               | `.python-black`      |
| **RUBY_CONFIG_FILE**              | Filename for [rubocop configuration](https://docs.rubocop.org/rubocop/configuration.html) (ex: `.ruby-lint.yml`, `.rubocop.yml`)                                           | `.ruby-lint.yml`     |
| **SNAKEMAKE_SNAKEFMT_CONFIG_FILE**| Filename for [Snakemake configuration](https://github.com/snakemake/snakefmt#configuration) (ex: `pyproject.toml`, `.snakefmt.toml`)                                       | `.snakefmt.toml`     |
| **TYPESCRIPT_ES_CONFIG_FILE**     | Filename for [eslint configuration](https://eslint.org/docs/user-guide/configuring#configuration-file-formats) (ex: `.eslintrc.yml`, `.eslintrc.json`)                     | `.eslintrc.yml`      |
| **YAML_CONFIG_FILE**              | Filename for [Yamllint configuration](https://yamllint.readthedocs.io/en/stable/configuration.html) (ex: `.yaml-lint.yml`, `.yamllint.yml`)                                | `.yaml-lint.yml`     |

#### Enable or disable linters

!!! info "Note about `VALIDATE_[LANGUAGE]` variables from super-linter [README](https://github.com/github/super-linter#environment-variables)"
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

!!! warning
    Currently, the report in merge request widget doesn't display details on
    issues found, they are only described in the job output log.

We use [Junit](https://junit.org/junit5/)'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.
