## Objective

[Gitleaks](https://github.com/zricethezav/gitleaks/wiki/Scanning){:target="_blank"} is a tool
made to detect hardcoded secrets like passwords, api keys and tokens in git
repository. As it written in go, it is much faster than most of the
[alternatives](https://github.com/zricethezav/gitleaks/wiki/Comparison-with-other-tools){:target="_blank"}.

## How to use it


1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/gitleaks.yml'
    ```
2. Well done, your job is ready to work ! 😀

## Job details

* Job name: `gitleaks`
* Docker image:
[`zricethezav/gitleaks:v6.1.2`](https://hub.docker.com/r/_/zricethezav/gitleaks){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

## Allowing Failure

If you want for this job not to fail upon discovering a secret in the commits
of the repository, you can do that by adding this to your `.gitlab-ci.yml`

```
gitleaks:
  allow_failure: true
```
