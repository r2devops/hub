## Objective

This job will deploy your YAML files to a Kubernetes cluster, the cluster can be linked with Gitlab or provided using a `KUBECONFIG` variable

## How to use it

!!! important
    If you want to deploy multiple YAML files, you need to provide the name of the folder containing the files in the variable `FILES_LOCATION`.
    If also you have subfolders, you need to add `--recursive` in `$KUBECTL_OPTIONS`

1. Make sure that you have a Kubernetes cluster, you have two options:
      1. Use a linked cluster with your Gitlab project, get more info [here](https://docs.gitlab.com/ee/user/project/clusters/){:target="_blank"}
      1. Provide a kubeconfig file through the variable `KUBECONFIG`, check [THIS](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} guide to see how
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. Provide the value of the variable `FILES_LOCATION`, check **Variables**
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀

## Variables

!!! important
    If you want to provide a kubeconfig file, please create a file variable named `$KUBECONFIG`, you can do that by passing them as [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} so that your data can stay confidential.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `FILES_LOCATION` | Folder name, if multiple .yaml files; Or file name that contains the manifests | ` ` |
| `KUBECTL_OPTIONS` | Additional options for the command kubectl | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `1.19.11`  |

!!! info
    Here is an example of what you can put in `FILES_LOCATION` if you have multiple files but not in the same folder
        ```yaml
        FILES_LOCATION: "myfile1.yaml -f myfile2.yaml -f myfile3.yml"
        ```



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
