| `IMAGE_TAG` | The default tag for the docker image | `3`  |
## Objective

Run a SSH command on a remote host.

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. Set the secret variable `SSH_PRIVATE_KEY` as CI/CD variables (it can be file
   or variable type) in [your Gitlab
   project](https://docs.gitlab.com/12.10/ee/ci/variables/#via-the-ui){:target="_blank"}
   if you need encrypted variables
1. Set the variables `SSH_USER`, `TARGET_HOST` and `SHELL_COMMAND` by
   overriding the job or as Gitlab CI/CD variables. See [variables
   section](#variables)
1. If you need to customize other part of the job (stage, variables, ...) 👉
   check the [jobs customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

### Example of `.gitlab-ci.yml` file

```yaml
include:
  - remote: 'https://jobs.r2devops.io/ssh.yml'

ssh:
  variables:
    SSH_USER: r2devops
    TARGET_HOST: r2devops.io
    SHELL_COMMAND: echo "Hello world !"
```

## Job details

* Job name: `ssh`
* Docker image: [`alpine:3`](https://hub.docker.com/_/alpine){:target="_blank"}
* Default stage: `deploy`
* When: `manual`, only when running on default branch (`$CI_DEFAULT_BRANCH`).
  To update this behavior, see [job customization](https://r2devops.io/use-the-hub/#global) to override [`rules`](https://docs.gitlab.com/ee/ci/yaml/#rulesif)

### Variables

!!! info
    All variables can be set using [Gitlab CI/CD
    variables](https://docs.gitlab.com/12.10/ee/ci/variables/#via-the-ui) to
    avoid exposing them in clear in your `.gitlab-ci.yml`. This is recommended
    for sensible parameters as `SSH_USER` or `TARGET_HOST` and it's **HIGHLY**
    recommended for secret variable `SSH_PRIVATE_KEY`.

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `SSH_PRIVATE_KEY` | Private SSH key to login on the `TARGET_HOST` server | yes | ` `
| `SSH_USER` | User on the target host | yes | ` `
| `TARGET_HOST` | Domain name or IP address of the target host | yes | ` `
| `SHELL_COMMAND` | Shell command to run on `TARGET_HOST` | yes | ` `
| `SSH_PORT` | SSH server port on target host | no | `22`
| `SSH_OUTPUT_FILE` | File that will be used to store SSH output | no | `ssh_output.txt `

### Artifacts

* If remote command success: the job success with the output as artifact
* If remote command fails: the job fails with the output as artifact

Command output is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `SSH output` in merge requests.  Exposition of artifact currently works
    only if you keep `SSH_OUTPUT_FILE` default value because of [this issue
    from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)