## Objective

[Gitleaks](https://github.com/zricethezav/gitleaks/wiki/Scanning){:target="_blank"} is a tool made to detect hardcoded
secrets like passwords, api keys and tokens in git repository. As it written in go, it is much faster than most of the
[alternatives](https://github.com/zricethezav/gitleaks/wiki/Comparison-with-other-tools){:target="_blank"}.

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of
   your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can
   specify [a fixed version](/versioning/) instead of `latest`.
2. Well done, your job is ready to work ! 😀

## Job details

* Job name: `gitleaks`
* Docker image:
[`zricethezav/gitleaks:v8.6.0`](https://hub.docker.com/r/zricethezav/gitleaks)
* Default stage: `tests`
* When: `always`

## Allowing Failure

If you want for this job not to fail upon discovering a secret in the commits of the repository, you can do that by
adding this to your `.gitlab-ci.yml`

```yaml
gitleaks:
  allow_failure: true
```

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)