# Versioning

Each job of the hub are versioned using git tags.

!!! note
    Version follows the [Semantic Versioning](https://semver.org/){:target="_blank"}.

You can also use the latest version using `latest` instead of a tag. Using
this, you will retrieve the latest version of jobs at each run. Note that if
you don't set any tag, `latest` is used by default.

Each jobs can be used independently with a different version.

Example in `.gitlab-ci.yml`:

```yaml
include:
  - remote: 'https://jobs.r2devops.io/latest/docker.yml'
  - remote: 'https://jobs.r2devops.io/0.1.0/mkdocs.yml'
  - remote: 'https://jobs.r2devops.io/0.1.0/apidoc.yml'
```

Available tags and release note for each job are available in [Jobs
section](/jobs/).
