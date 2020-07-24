# ☸️  Helm

🚧 *Work in progress*

<!--

Deploy on your kubernetes cluster using Helm charts.

* In issue branch: review environment
* In master branch: staging environment
* In master branch: production environment (manual)

* Chart and values files must be in repo, see Variables section
* Use [helm secrets](https://github.com/futuresimple/helm-secrets) to encrypt/decrypt secrets values files
* Values files must be named like `<ENV>.yaml` for clear text and `secrets.<ENV>.yaml` for encrypted

**Specifications**

* File: https://gitlab.com/go2scale/jobs/raw/2020-03-05_3/jobs/helm.gitlab-ci.yml
* Publications: *TODO*
* Image:
    * Repository: https://gitlab.com/go2scale/dockerfiles/helm
    * Documentation: https://go2scale.gitlab.io/dockerfiles/helm

**Variables**

| Name | Description | Default |
| ---- | ----------- | ------- |
| `REVIEW_DISABLE` | Disable review deployment | |
| `STAGING_DISABLE` | Disable staging deployment | |
| `PRODUCTION_DISABLE` | Disable production deployment | |
| `CHART_PATH` | Path of helm chart to use | `/charts/$CI_PROJECT_NAME` |
| `VALUES_PATH` | Path of values files to use | `./conf/values` |

**Secret variables**

| Name | Description | Type |
| ---- | ----------- | ------- |
| `PGP_PUBLIC` | Public PGP key to decrypt secrets values | `file` |
| `PGP_PRIVATE` | Private PGP key to decrypt secrets values | `file` |

-->
