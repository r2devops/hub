# Jobs

## 🔍 Quality

Auto-detect file in repo and run all [coala](https://coala.io) relevant linters on it.

**How to use it**

* Variables:
  * **TODO:** put variables from https://gitlab.com/go2scale/dockerfiles/quality-check here

**Specifications**

* File: https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/quality_check.gitlab-ci.yml
* Publications:
    * Full report as artifact
    * Short report in merge request and job logs
* Image:
    * Repository: https://gitlab.com/go2scale/dockerfiles/quality-check
    * Documentation: https://go2scale.gitlab.io/dockerfiles/quality-check

## 📗 Documentation

Build HTML documentation form Markdown source and deploy it on Gitlab pages

* Build is done in all pipeline, exposed as artifact
* Publication on page is done only on master branch

**Specifications**

* File: https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/documentation.gitlab-ci.yml
* Publications in MR: `Documentation` artifact
* Image:
    * Repository: https://hub.docker.com/r/squidfunk/mkdocs-material

**How to use it**

* Variables:
    * `DOCUMENTATION_DISABLE`: disable build ans publication
    * `PAGES_DISABLE`: disable publication on stage

## 📥 Build

*Work in progress...*

## 🚀 Helm

Deploy on your kubernetes cluster using Helm charts.

* In issue branch: review environment
* In master branch: staging environment
* In master branch: production environment (manual)

**Specifications**

* File: https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/helm.gitlab-ci.yml
* Publications: *TODO*
* Image:
    * Repository: https://gitlab.com/go2scale/dockerfiles/helm
    * Documentation: https://go2scale.gitlab.io/dockerfiles/helm

**How to use it**

* Chart and values files must be in repo, see Variables section
* Use [helm secrets](https://github.com/futuresimple/helm-secrets) to encrypt/decrypt secrets values files
* Values files must be named like `<ENV>.yaml` for clear text and `secrets.<ENV>.yaml` for encrypted
* Variables:
    * `REVIEW_DISABLE`: disable review deployment
    * `S2020-03-05_1ING_DISABLE`: disable staging deployment
    * `PRODUCTION_DISABLE`: disable production deployment
    * `CHART_PATH`: path of helm chart to use. Default: `/charts/$CI_PROJECT_NAME`
    * `VALUES_PATH`: path of values files to use. Default: `./conf/values`
* Secret variables:
    * `PGP_PUBLIC`: public PGP key to decrypt secrets values. Use `file` type.
    * `PGP_PRIVATE`: private PGP key to decrypt secrets values. Use `file` type.
