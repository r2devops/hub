# 📗 Mkdocs

Build HTML documentation form Markdown source and deploy it on Gitlab pages

* Build is done in all pipeline, exposed as artifact
* Publication on page is done only on master branch

**Specifications**

* File: https://gitlab.com/go2scale/jobs/raw/2020-03-05_3/jobs/documentation.gitlab-ci.yml
* Publications in MR: `Documentation` artifact
* Image:
    * Repository: https://hub.docker.com/r/squidfunk/mkdocs-material

**Variables**

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DOCUMENTATION_DISABLE` | Disable build ans publication | |
| `PAGES_DISABLE` | Disable publication on stage | |
