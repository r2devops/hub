## Objective

This job will deploy your YAML files to a Kubernetes cluster, the cluster can be linked with Gitlab or provided using a `KUBECONFIG` variable

## How to use it

1. Make sure that you have a Kubernetes cluster, you have two options:
      1. Use a linked cluster with your Gitlab project, get more info [here](https://docs.gitlab.com/ee/user/project/clusters/){:target="_blank"}
      1. Provide a kubeconfig file through the variable `KUBECONFIG`, check [THIS](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} guide to see how
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/kubectl_deploy.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `kubectl_deploy`
* Docker image:
[`nekottyo/kustomize-kubeval:latest`](https://hub.docker.com/r/nekottyo/kustomize-kubeval)
* Default stage: `deploy`
* When: `manual`, only when running on default branch (`$CI_DEFAULT_BRANCH`).  
  To update this behavior, see [job customization](https://r2devops.io/use-the-hub/#global) to override [`rules`](https://docs.gitlab.com/ee/ci/yaml/#rulesif)

### Variables

!!! important
    If you want to provide a kubeconfig file, please create a file variable named `$KUBECONFIG`, you can do that by passing them as [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} so that your data can stay confidential.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `FILES_LOCATION` | Folder name or file name that contains the manifests | ` ` |
| `KUBECTL_OPTIONS` | Additional options for the command kubectl | ` ` |
