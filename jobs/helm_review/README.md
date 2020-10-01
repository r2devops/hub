# ☸️  Helm Review

## Description

Deploy your [helm](https://helm.sh/docs/intro/quickstart/) charts as a review environment when a pipeline is run in a merge request

## How to use it

1. Prepare your project with the files needed for the [helm chart](https://helm.sh/docs/chart_template_guide/getting_started/)
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/helm_review.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `helm_review`
* Docker image:
[`lachlanevenson/k8s-helm:v3.0.2`](https://hub.docker.com/r/lachlanevenson/k8s-helm/)
* Default stage: `review`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `CHART_PATH` <img width=250/> | Path to the directory of the chart <img width=400/> | `./charts/$CI_PROJECT_NAME` |
| `VALUES_PATH` | Path to value files | `./conf/values` |
| `REGISTRY` | Registry from where to pull container image | `${CI_REGISTRY_IMAGE}` |
| `KUBECTL_URL` | Url to get kubectl binary | `https://storage.googleapis.com/kubernetes-release/release/v1.17.0/bin/linux/amd64/kubectl` |
| `HELMSECRETS_URL` | Url to get kubectl secrets plugin | `https://github.com/futuresimple/helm-secrets` |
| `HELMSECRETS_VERSION` | Version of kubectl secrets plugin | `v2.0.2` |
| `STABLE_REPO_URL` | Url of stable repo to add to helm | `https://kubernetes-charts.storage.googleapis.com/` |
| `HELM_ADDITIONAL_OPTIONS` | Additional settings to give to helm for deployment | ` ` |

### Secrets

Secrets files are encrypted with the helm plugin [secrets](https://github.com/zendesk/helm-secrets).
It will allow to decrypt any secrets.review.yaml that you have in your `${VALUES_PATH}`, like a database password for example.
