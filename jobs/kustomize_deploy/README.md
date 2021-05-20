## Objective

This job will deploy manifests to your cluster using Kustomize and set a new image for the deployment, the cluster can be either linked to Gitlab or no.

## How to use it

1. Make sure that you have a Kubernetes cluster, you have two options:
      1. Use a linked cluster with your Gitlab project, get more info [here](https://docs.gitlab.com/ee/user/project/clusters/){:target="_blank"}
      1. Provide a kubeconfig file through the variable `KUBECONFIG`, check [THIS](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} guide to see how
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/kustomize_deploy.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `kustomize_deploy`
* Docker image:
[`nekottyo/kustomize-kubeval:latest`](https://hub.docker.com/r/nekottyo/kustomize-kubeval)
* Default stage: `deploy`
* When: `manual`, only when running on default branch (`$CI_DEFAULT_BRANCH`).  
  To update this behavior, see [job customization](https://r2devops.io/use-the-hub/#global) to override [`rules`](https://docs.gitlab.com/ee/ci/yaml/#rulesif)

### Variables

!!! important
    There are some mandatory variables that **you have to provide**, the most important one being `$KUBECONFIG`, you can do that by passing them as [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} so that your data can stay confidential.

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `PROJECT_ROOT` | path to the root of the project | no | `.`
| `KUBECONFIG` | the config file for kubectl | yes | ` `
| `KUSTOMIZATION_DIR` | the folder that contains the `kustomization.yaml` file | yes | ` `
| `NAMESPACE` | The namespace to use for deployment | yes | `$KUBE_NAMESPACE`
| `DEPLOYMENT_NAME` | name of deployment to use | yes | ` `
| `CONTAINER_NAME` | name of the containers to update | yes | ` `
| `IMAGE_NAME` | name of the new image to use | yes | ` `
| `IMAGE_TAG` | the tag to use for the new image | yes | ` `
| `KUSTOMIZE_OPTIONS` | Additional options for `kubectl` command | no | ` `

### Artifacts

* If the job is successful, the output of the commands will be available as an artifact exposed as `Kustomize job output`