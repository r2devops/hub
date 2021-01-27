## Objective

[Gitleaks](https://github.com/zricethezav/gitleaks/wiki/Scanning){:target="_blank"} is a tool
made to detect hardcoded secrets like passwords, api keys and tokens in git
repos. As it written in go, it is much faster than most of the
[alternatives](https://github.com/zricethezav/gitleaks/wiki/Comparison-with-other-tools){:target="_blank"}.

## How to use it


1. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/gitleaks.yml'
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
