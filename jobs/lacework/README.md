## Objective

This template runs [lacework-vulnerability-scanner](https://github.com/lacework/lacework-vulnerability-scanner) to scan and assess Docker container image for vulnerabilities.

## How to use it

1. Copy/paste the quick use above in your `.gitlab-ci.yml` file
1. Add `LW_ACCOUNT_NAME` and `LW_ACCESS_TOKEN` variables in your project CI/CD variables
1. If you want to scan a specific image, override variables `IMAGE`, `TAG` and `REGISTRY`
1. If this image come from a private registry, `REGISTRY_USER` and `REGISTRY_PASSWORD` variables in your project CI/CD variables
1. Well done, your job is ready to work ! 😀

## Examples

### Run a Lacework check on an image from `grc.io` without authentication

Prerequisites:
    - Set `LW_ACCOUNT_NAME` variable in your project CI/CD variables
    - Set `LW_ACCESS_TOKEN` variable in your project CI/CD variables

```yaml
stages:
  - tests

include:
  - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/lacework@latest.yaml'

lacework:
  variables:
    REGISTRY: gcr.io
    IMAGE: kaniko-project/executor
    TAG: latest
```

### Run a Lacework check on an image from Docker Hub with authentication

Prerequisites:
    - Set `LW_ACCOUNT_NAME` variable in your project CI/CD variables
    - Set `LW_ACCESS_TOKEN` variable in your project CI/CD variables
    - Set `REGISTRY_PASSWORD` variable in your project CI/CD variables

```yaml
stages:
  - tests

include:
  - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/lacework@latest.yaml'

lacework:
  variables:
    REGISTRY: docker.io
    REGISTRY_USER: <your username>
    IMAGE: <private image>
    TAG: <tag>
```

### Build an image, publish it in GitLab registry and check it with Lacework

Prerequisites:
    - Set `LW_ACCOUNT_NAME` variable in your project CI/CD variables
    - Set `LW_ACCESS_TOKEN` variable in your project CI/CD variables
    - Nothing to do about authentication, it is done automatically

```yaml
stages:
  - build
  - tests

include:
  - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/docker_build@latest.yaml'
  - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/lacework@latest.yaml'
```

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `LW_ACCOUNT_NAME` | (**Mandatory**) Lacework account name. It should be set in GitLab CI/CD variables. | ` ` |
| `LW_ACCESS_TOKEN` | (**Mandatory**) Lacework access token. It should be set in GitLab CI/CD variables. | ` ` |
| `IMAGE` | Image to scan | `$CI_PROJECT_PATH` |
| `TAG` | Tag of image to scan  | `$CI_COMMIT_TAG` or `$CI_COMMIT_SHA` |
| `REGISTRY` | Registry of image to scan | `$CI_REGISTRY` |
| `REGISTRY_USER` | Registry user | `$CI_REGISTRY_USER` if `REGISTRY`==`$CI_REGISTRY` |
| `REGISTRY_PASSWORD` | Registry password. It should be set in GitLab CI/CD variables. | `$CI_REGISTRY_PASSWORD` if `REGISTRY`==`$CI_REGISTRY` |
| `LW_ADDITIONAL_OPTIONS` | Additional option to use in `lacework-inline-scanner` CLI | ` ` |
| `LW_VERSION` | Version of `lacework-inline-scanner` | `0.20.0` |
| `DIND_VERSION` | Version of `docker-in-docker` | `20.10.16-dind` |

