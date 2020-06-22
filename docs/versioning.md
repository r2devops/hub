# Versioning

Jobs are versioned using git tag following this format: `YYYY-MM-DD_RELEASE`.

!!! note
    `RELEASE` is a number started from 1

You can also use the latest version using `master` instead of a tag. Using
this, you will retrieve the latest version of jobs at each run.


Each jobs can be used independently with different version date.

Example in `.gitlab-ci.yml`:

```yaml
include:
  - remote: https://gitlab.com/go2scale/jobs/-/raw/2020-02-28_1/Jobs/coala/coala.yml
  - remote: https://gitlab.com/go2scale/jobs/-/raw/2020-03-05_1/Jobs/mkdocs/mkdocs.yml
  - remote: https://gitlab.com/go2scale/jobs/-/raw/master/Jobs/helm/helm.yml
```

Available tags and release note for each jobs are available in [Jobs
section](/Jobs/).
