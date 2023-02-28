## Objective

This job will deploy manifests to your cluster using Kustomize and set a new image for the deployment, the cluster can be either linked to Gitlab or no.

## How to use it

1. Make sure that you have a Kubernetes cluster, you have two options:
      1. Use a linked cluster with your Gitlab project, get more info [here](https://docs.gitlab.com/ee/user/project/clusters/){:target="_blank"}
      1. Provide a kubeconfig file through the variable `KUBECONFIG`, check [THIS](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} guide to see how
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Set the mandatory variables for your job, check [**Variables**](#variables)
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀


## Variables

!!! important
    There are some mandatory variables that **you have to provide**, the most important one being `$KUBECONFIG`, you can do that by passing them as [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} so that your data can stay confidential.

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `PROJECT_ROOT` | path to the root of the project | no | `.`
| `KUBECONFIG` | the config file for kubectl | yes | ` `
| `KUSTOMIZATION_DIR` | the folder that contains the `kustomization.yaml` file | yes | ` `
| `CHANGE_IMAGE` | ability to change image of deployment | no | `true`
| `NAMESPACE` | The namespace to use for deployment | no | `$KUBE_NAMESPACE`
| `POD_NAME` | name of the pods to update | yes, only if `CHANGE_IMAGE` is `true` | ` `
| `POD_IMAGE_NAME` | name of the new image to use | yes, only if `CHANGE_IMAGE` is `true` | `$CI_REGISTRY_IMAGE`
| `POD_IMAGE_TAG` | the tag to use for the new image | yes, only if `CHANGE_IMAGE` is `true` | ` `
| `KUSTOMIZE_OPTIONS` | Additional options for `kubectl` command | no | ` `
| `IMAGE_TAG` | The default tag for the docker image | `1.21.1-4.1.3`  |

## Artifacts

* If the job is successful, the output of the commands will be available as an artifact exposed as `Kustomize job output`


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
