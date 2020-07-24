# Versioning

Jobs are versioned using git tag following this format: `YYYY-MM-DD_RELEASE`.

!!! note
    `RELEASE` is a number started from 1

You can also use the latest version using `latest` instead of a tag. Using
this, you will retrieve the latest version of jobs at each run. Note that if
you don't set any tag, `latest` is used by default.


Each jobs can be used independently with different version date.

Example in `.gitlab-ci.yml`:

```yaml
include:
  - remote: 'https://jobs.go2scale.io/latest/docker.yml'
  - remote: 'https://jobs.go2scale.io/2020-06-22_1/mkdocs.yml'
```

Available tags and release note for each jobs are available in [Jobs
section](/Jobs/).
