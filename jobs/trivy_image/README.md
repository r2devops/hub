## Description

Run a security issue detection in a docker image using
[Trivy](https://github.com/aquasecurity/trivy){:target="_blank"}, a Simple and Comprehensive
Vulnerability Scanner for Containers and other Artifacts. More details on Trivy
vulnerability detection capabilities are available in its official
[README](https://github.com/aquasecurity/trivy#vulnerability-detection){:target="_blank"}

!!! warning
    With the default configuration, this job will fail if errors are detected.
    It's the recommended configuration to reduce security risks in your
    software. You can disable this behaviour by setting the value `0` to the
    variable `TRIVY_EXIT_CODE`.

## How to use it

1. Check supported OS and packages
   [here](https://github.com/aquasecurity/trivy#vulnerability-detection){:target="_blank"}
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/trivy_image.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `trivy_image`
* Docker image: [`docker`](https://hub.docker.com/_/docker){:target="_blank"}
* Default stage: `dynamic_tests`

### Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
|:-|:-|:-
| `TRIVY_VERSION` <img width=450/> | Version of trivy to use. Releases version are available [here](https://github.com/aquasecurity/trivy/releases){:target="_blank"} | `0.9.2` |
| `TRIVY_SEVERITY` | Severities of vulnerabilities to be displayed | `UNKNOWN`,`LOW`,`MEDIUM`,`HIGH`,`CRITICAL`|
| `TRIVY_EXIT_CODE` | Exit code when vulnerabilities were found | 1 |
| `TRIVY_VULN_TYPE` | List of vulnerability types | os,library |
| `TRIVY_OUTPUT` | Output file name | junit-report.xml |
| `TRIVY_IGNOREFILE` | Specify .trivyignore file | .trivyignore |
| `TRIVY_CACHE_DIR` | cache directory | .trivycache/
| `TRIVY_FORMAT` | Format (table, json, template) | template |
| `TEMPLATE_NAME` | Name of used template | junit.tpl |
| `TRIVY_CLEAR_CACHE` | Clear image caches without scanning | false |
| `TRIVY_IGNORE_UNFIXED` | Display only fixed vulnerabilities | false |
| `TRIVY_DEBUG` | Debug mode | false |
| `DOCKER_HOST` | Daemon socket to connect to | tcp://docker:2375 |
| `TRIVY_TIMEOUT` | Docker timeout | 2m0s |
| `TRIVY_LIGHT` | Trivy faster without descriptions and refs | false |
| `TRIVY_DOWNLOAD_DB_ONLY` | Download vulnerability database without scan | false |
| `TRIVY_NO_PROGRESS` | Suppress progress bar | false |
| `TRIVY_QUIET` | Suppress progress bar and log output | false |
| `TRIVY_SKIP_UPDATE` | Skip vulnerability database update | false |
| `TRIVY_REMOVED_PKGS` | Detect vulns of Alpine removed packages | false |
| `CUSTOM_REGISTRY` | If you use another registry than your gitlab instance's one | ` ` |
| `REGISTRY_USER` | User to use for authenticating `CUSTOM_REGISTRY` | ` ` |
| `REGISTRY_PASSWORD` | Password to use for authenticating `CUSTOM_REGISTRY` | ` ` |
| `CUSTOM_TAG` | If you want to use another tag beside `CI_COMMIT_SHA` or `CI_COMMIT_TAG` | ` ` |

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget
