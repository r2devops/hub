# Release notes

Pipelines and Jobs are versionned using git tag following this format: `YYYY-MM-DD_RELEASE`

!!! note
    `RELEASE` is a number started from 1

Each jobs can be used independently with different version date.

Example in `.gitlab-ci.yml`:

```yaml
include:
  # Go2Scale DevSecOps
  - remote: https://gitlab.com/go2scale/jobs/raw/2020-02-28_1/jobs/quality_check.gitlab-ci.yml
  - remote: https://gitlab.com/go2scale/jobs/raw/2020-03-05_1/jobs/documentation.gitlab-ci.yml
  - remote: https://gitlab.com/go2scale/jobs/raw/2020-02-29_3/jobs/helm.gitlab-ci.yml
```

Release notes are described in each [pipelines](#pipelines) and [jobs](#jobs) dedicated sections.
