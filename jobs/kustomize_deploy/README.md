## Objective

This job will deploy your cluster using Kustomize and set a new image for the deployment.

## How to use it

1. Make sure to add a CI/CD file variable containing your [`kubeconfig`](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/){:target="_blank"} file, more info [here](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"}
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
* When: `always`

### Variables

!!! important
    There are some mandatory variables that **you have to provide**, the most important one being `$KUBECONFIG`, you can do that by passing them as [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} so that your data can stay confidential.

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `PROJECT_ROOT` | path to the root of the project | no | `.`
| `KUBECONFIG` | the config file for kubectl | yes | ` `
| `KUSTOMIZATION_DIR` | the folder that contains the `kustomization.yaml` file | yes | ` `
| `NAMESPACE` | The namespace to use for deployment | yes | ` `
| `DEPLOYMENT_NAME` | name of deployment to use | yes | ` `
| `CONTAINER_NAME` | name of the containers to update | yes | ` `
| `IMAGE_NAME` | name of the new image to use | yes | ` `
| `IMAGE_TAG` | the tag to use for the new image | yes | `latest`
| `KUSTOMIZE_OPTIONS` | Additional options for `kubectl` command | no | ` `

### Artifacts

* If the job is successful, the output of the commands will be available as an artifact exposed as `Kustomize job output`