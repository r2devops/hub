## Description

Deploy your [helm](https://helm.sh/docs/intro/quickstart/){:target="_blank"} charts as a review environment when a pipeline is run in a merge request

## How to use it

1. To use this job, you have to provide a helm chart to deploy your project. The chart location must be defined in the CHART_PATH variable. If you want to use custom values files, check the `VALUES_FILE` and `VALUES_SECRET_FILE` variables. More information about helm charts in [documentation](https://helm.sh/docs/chart_template_guide/getting_started/){:target="_blank"}
2. Prepare the secret PGP variables (`PGP_PUBLIC` and `PGP_PRIVATE`) in your CI/CD variables (as files and not variables!) in [gitlab](https://docs.gitlab.com/12.10/ee/ci/variables/#via-the-ui){:target="_blank"} if you need encrypted variables
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/helm_review.yml'
    ```

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `helm_review`, `cleanup_helm_review`
* Docker image:
[`lachlanevenson/k8s-helm:v3.4.2`](https://hub.docker.com/r/lachlanevenson/k8s-helm/){:target="_blank"}
* Default stage: `review`
* When: `always`

### Variables

| Name | Description | Default | Mandatory |
| ---- | ----------- | ------- | --------- |
| `CHART_PATH` <img width=250/> | Path to the directory of the chart <img width=400/> | `./charts/$CI_PROJECT_NAME` | Yes |
| `VALUES_PATH` | Path to value files | `./conf/values` | Yes |
| `VALUES_FILE` | Name of the review configuration yaml file | `review.yaml` | Yes |
| `VALUES_SECRET_FILE` | Name of the secrets review configuration yaml file | `secrets.review.yaml` | Only if the secret file `VALUES_SECRET_FILE` exists |
| `REGISTRY` | Registry from where to pull container image | `${CI_REGISTRY_IMAGE}` |  Yes |
| `KUBECTL_URL` | Url to get kubectl binary | `https://storage.googleapis.com/kubernetes-release/release/v1.20.1/bin/linux/amd64/kubectl` | Yes |
| `HELMSECRETS_URL` | Url to get kubectl secrets plugin | `https://github.com/jkroepke/helm-secrets` | Yes |
| `HELMSECRETS_VERSION` | Version of kubectl secrets plugin | `v3.4.0` | Only if the secret file `VALUES_SECRET_FILE` exists |
| `STABLE_REPO_URL` | Url of stable repo to add to helm | `https://charts.helm.sh/stable` | Yes |
| `HELM_ADDITIONAL_OPTIONS` | Additional settings to give to helm for deployment | ` ` | No |

**Gitlab CI/CD variables:**

| Name | Description | Type | Mandatory |
| ---- | ----------- | ---- | --------- |
| `PGP_PUBLIC` | PGP public key used to encrypt secret file | File | Only if the secret file `VALUES_SECRET_FILE` exists |
| `PGP_PRIVATE` | PGP private key used to encrypt secret file | File | Only if the secret file `VALUES_SECRET_FILE` exists |

### Secrets

Secrets files are encrypted with the helm plugin [secrets](https://github.com/zendesk/helm-secrets){:target="_blank"}.
It will allow encrypting or decrypting any yaml files that you have in your `${VALUES_PATH}` so you can push values that will be decrypted at runtime but not seen from the source code.
For example, you can `helm secrets enc review.yaml` to encrypt it to a `secret.review.yaml`, so you will have some public variables in a `review.yalm` file and a password for example in `secrets.review.yaml`.
