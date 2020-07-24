# 🛡️ Trivy

## Description

[Trivy](https://github.com/aquasecurity/trivy) is a Simple and Comprehensive Vulnerability Scanner for Containers and other Artifacts, Suitable for CI

##### By default, this job

 - Is avaible for any edition of GitLab

 - Is 100% autonom - you don't have any updates or config to do, but obviously you can change the values of the variables or configure your own script

 - Analysis with [Trivy](https://github.com/aquasecurity/trivy) the GitLab's repo (image or/and filesystem) at every commit to detect vulnerabilities

 - Displays a report in pipeline window and merge request (junit.xml format)


## How to use it

 1. Please check supported OS and packages (see list below)
 2. Please check variables config (see list below)
 3. Add the corresponding url to your `.gitlab-ci.yml` file

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/trivy'
    ```

4. Well done, it's finished ! 😀


### Variables Description


#### Main Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
| ------------- | ----------- | ------------- |
| `IMAGE` | Target name or target path | `$CI_REGISTRY_IMAGE:$CI_COMMIT_SHA` or `$CI_REGISTRY_IMAGE:$CI_COMMIT_TAG` if the pipeline is run following a tag creation |
| `TRIVY_VERSION` | Version of trivy to use. Releases version are available [here](https://github.com/aquasecurity/trivy/releases) | `0.9.2` |
| `TRIVY_SEVERITY` | Severities of vulnerabilities to be displayed | UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL |
| `TRIVY_EXIT_CODE` | Exit code when vulnerabilities were found | 0 |
| `TRIVY_VULN_TYPE` | List of vulnerability types | os,library |
| `TRIVY_OUTPUT` | Output file name | junit-report.xml |
| `TRIVY_IGNOREFILE` | Specify .trivyignore file | .trivyignore |
| `TRIVY_CACHE_DIR` | cache directory | .trivycache/
| `TRIVY_FORMAT` | Format (table, json, template) | template |
| `TEMPLATE_NAME` | Name of used template | junit.tpl |
| `TRIVY_CLEAR_CACHE` | Clear image caches without scanning | false |


#### Secondary Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
| ------------- | ----------- | ------------- |
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


### Reports

By default we use [Junit](https://junit.org/junit5/)'s xml report

1. When you launch this Trivy job, a `junit.tpl` file is downloaded from [Trivy](https://github.com/aquasecurity/trivy)'s repo in current directory
2. This template is used to display report in pipeline window and merge request

##### Default reporting config

```yaml
  artifacts:
    reports:
      junit: junit-report.xml
    expire_in: 30 days
    when: always
```


### OS Packages Vulnerabilities Detection

| OS Packages                  | Supported Versions                       | Target Packages               | Detection of unfixed vulnerabilities |
| ---------------------------- | ---------------------------------------- | ----------------------------- | :----------------------------------: |
| `Alpine Linux`                | 2.2 - 2.7, 3.0 - 3.12                    |   apk                         |                  NO                  |
| `Red Hat Universal Base Image` | 7, 8                                     |   yum/rpm                     |                 YES                  |
| `Red Hat Enterprise Linux`     | 6, 7, 8                                  |   yum/rpm                     |                 YES                  |
| `CentOS`                       | 6, 7                                     |   yum/rpm                     |                 YES                  |
| `Oracle Linux`                 | 5, 6, 7, 8                               |   yum/rpm                     |                  NO                  |
| `Amazon Linux`                 | 1, 2                                     |   yum/rpm                     |                  NO                  |
| `openSUSE Leap`                | 42, 15                                   |   zypper/rpm                  |                  NO                  |
| `SUSE Enterprise Linux`       | 11, 12, 15                               |   zypper/rpm                  |                  NO                  |
| `Photon OS`                    | 1.0, 2.0, 3.0                            |   tdnf/yum/rpm                |                  NO                  |
| `Debian GNU/Linux`             | wheezy, jessie, stretch, buster          |   apt/apt-get/dpkg            |                 YES                  |
| `Ubuntu`                       | 12.04, 14.04, 16.04, 18.04, 18.10, 19.04 |   apt/apt-get/dpkg            |                 YES                  |
| `Distroless`                   | Any                                      |   apt/apt-get/dpkg            |                 YES                  |


### Application Dependencies Vulnerabilities Detection

| Application Dependencies |
|--------------------------|
| `Bundler`                  |
| `Composer`                 |
| `Pipenv`                   |
| `Poetry`                   |
| `npm`                      |
| `yarn`                     |
| `Cargo`                    |


## Version

* **Latest** : `https://jobs.go2scale.io/trivy/latest`
* **Tag `2020-07-22_1`** (initial version) : `https://jobs.go2scale.io/trivy/2020-07-22_1`
