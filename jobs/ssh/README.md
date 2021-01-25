## Description

Run a SSH command on a remote host.

## How to use it

1. Choose a version in [version list](#changelog)
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:
    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/ssh.yml'
    ```
3. Set the secret variable `SSH_PRIVATE_KEY` as CI/CD variables (it can be file
   or variable type) in [your Gitlab
   project](https://docs.gitlab.com/12.10/ee/ci/variables/#via-the-ui){:target="_blank"}
   if you need encrypted variables
4. Set the variables `SSH_USER`, `TARGET_HOST` and `SHELL_COMMAND` by
   overriding the job or as Gitlab CI/CD variables. See [variables
   section](#variables)
5. If you need to customize other part of the job (stage, variables, ...) 👉
   check the [jobs customization](/use-the-hub/#jobs-customization)
6. Well done, your job is ready to work ! 😀

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
* Default stage: `deployment`
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

Command output is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
`SSH output` in merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available in
    merge requests.
