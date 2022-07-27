## Objective

**This job has been moved to [`maven_test`](https://r2devops.io/_/r2devops-bot/maven_test).
This version is kept to avoid breaking users pipelines but it's now deprecated
and it will no longer be maintained.  Use
[`maven_test`](https://r2devops.io/_/r2devops-bot/maven_test) instead.**

Test your Java project using [Apache Maven](http://maven.apache.org/) JDK 11, JaCoCo and Surefire Maven plugins for code coverage and tests report directly in your merge requests.

## Variables
| Name | Description | Default |
| ---- | ------------| ------- |
| `ARTIFACTS_DIR` | Customize the path where the artifacts will be created | `${CI_PROJECT_DIR}/artifacts` |
| `IMAGE_TAG` | The default tag for the docker image | `3.8.4-jdk-11`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexlevy](https://gitlab.com/alexlevy)
