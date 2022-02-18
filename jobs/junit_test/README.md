## Objective

**This job has been moved to [`maven_test`](/jobs/static_tests/maven_test/).
This version is kept to avoid breaking users pipelines but it's now deprecated
and it will no longer be maintained.  Use
[`maven_test`](/jobs/static_tests/maven_test/) instead.**

Test your Java project using [Apache Maven](http://maven.apache.org/) JDK 11, JaCoCo and Surefire Maven plugins for code coverage and tests report directly in your merge requests.

## Job details

* Job name: `junit_test`
* Docker image: [maven:3.6.3-jdk-11](https://hub.docker.com/_/maven)
* Default stage: `static_tests`
* When: `always`

### Variables
| Name | Description | Default |
| ---- | ------------| ------- |
| `ARTIFACTS_DIR` | Customize the path where the artifacts will be created | `${CI_PROJECT_DIR}/artifacts` |

This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexlevy](https://gitlab.com/alexlevy)