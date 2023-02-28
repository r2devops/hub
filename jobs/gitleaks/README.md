## Objective

[Gitleaks](https://github.com/zricethezav/gitleaks/wiki/Scanning){:target="_blank"} is a tool made to detect hardcoded
secrets like passwords, api keys and tokens in git repository. As it written in go, it is much faster than most of the
[alternatives](https://github.com/zricethezav/gitleaks/wiki/Comparison-with-other-tools){:target="_blank"}.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. Well done, your job is ready to work ! 😀

## Allowing Failure

If you want for this job not to fail upon discovering a secret in the commits of the repository, you can do that by
adding this to your `.gitlab-ci.yml`

```yaml
gitleaks:
  allow_failure: true
```

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `IMAGE_TAG` | The default tag for the docker image | `v8.15.0`  |

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)
