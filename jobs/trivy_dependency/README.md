| `IMAGE_TAG` | The default tag for the docker image | `0.12.0`  |
## Objective

Run a security issue detection in your local dependencies using
[Trivy](https://github.com/aquasecurity/trivy){:target="_blank"}, a Simple and Comprehensive
Vulnerability Scanner for Containers and other Artifacts. More details on Trivy
vulnerability detection capabilities are available in its official
[README](https://github.com/aquasecurity/trivy#vulnerability-detection){:target="_blank"}

!!! warning
    With the default configuration, this job will fail if detected errors are in severity `MEDIUM`,`HIGH`,`CRITICAL`.
    It's the recommended configuration to reduce security risks in your
    software. You can disable this behaviour by emptying the value of the
    variable `TRIVY_EXIT_ON_SEVERITY`.

## How to use it

1. Ensure that your dependency manager is supported in [dependencies check
   section](#dependencies-check)
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `trivy_dependency`
* Docker image: [`aquasec/trivy`](https://hub.docker.com/r/aquasec/trivy/){:target="_blank"}
* Default stage: `tests`

### Dependencies check

Trivy runs dependencies analysis using the **lock files** of dependency
managers.

!!! info
    A lock file in development is an auto built file by your dependency
    manager which describes **exactly** all dependencies used with their
    precise version. It's complementary with your classical requirement file
    and permits to ensure that every environment get the exact same
    dependencies versions. Goal is to ensure that your application will always
    behave the same way, without any changes that may break a feature.

!!! info
    It is
    [recommended](https://myers.io/2019/01/13/what-is-the-purpose-of-a-lock-file-for-package-managers/){:target="_blank"} to
    have these files in your version control system, to ensure everyone will
    get the same behavior from your dependencies.
    More details about lock files in [this
    post](https://myers.io/2019/01/13/what-is-the-purpose-of-a-lock-file-for-package-managers/){:target="_blank"}

List of supported lock files :

| Language | Lock file |
|:-|:-
| Ruby | `Gemfile.lock` |
| Python | `Pipfile.lock`, `poetry.lock` |
| PHP | `composer.lock` |
| NodeJS | `package-lock.json`, `yarn.lock` |
| Rust | `Cargo.lock` |

To get more information, see [trivy
documentation](https://github.com/aquasecurity/trivy#application-dependencies){:target="_blank"}.

### Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
|:-|:-|:-
| `TRIVY_VERSION` | Version of trivy to use. Releases version are available [here](https://github.com/aquasecurity/trivy/releases){:target="_blank"} | `0.12.0` |
| `TRIVY_SEVERITY` | Severity of vulnerabilities to be displayed | `UNKNOWN`,`LOW`,`MEDIUM`,`HIGH`,`CRITICAL`|
| `TRIVY_EXIT_ON_SEVERITY` | Severities of vulnerabilities for the job to fail at | `MEDIUM`,`HIGH`,`CRITICAL`|
| `TRIVY_EXIT_CODE` | Exit code when vulnerabilities were found | 0 |
| `TRIVY_VULN_TYPE` | List of vulnerability types | os,library |
| `TRIVY_OPTIONS` | Options for command `trivy` | ` ` |
| `TRIVY_OUTPUT` | Output file name | junit-report.xml |
| `TRIVY_IGNOREFILE` | Specify .trivyignore file | .trivyignore |
| `TRIVY_CACHE_DIR` | cache directory | .trivycache/
| `TRIVY_FORMAT` | Format (table, json, template) | template |
| `TEMPLATE_NAME` | Name of used template | junit.tpl |
| `TRIVY_CLEAR_CACHE` | Clear image caches without scanning | false |
| `TRIVY_IGNORE_UNFIXED` | Display only fixed vulnerabilities | false |
| `TRIVY_DEBUG` | Debug mode | false |
| `TRIVY_SKIP_UPDATE` | Skip vulnerability database update | false |
| `TRIVY_REMOVED_PKGS` | Detect vulns of Alpine removed packages | false |

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)