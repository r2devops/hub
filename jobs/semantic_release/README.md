## Objective

Using this job, you will have benefits of using
[`semantic-release`](https://github.com/semantic-release/semantic-release){:target="_blank"}
with your own configuration.

**Semantic release** automates your whole versioning & package delivery. Knowing from which version number is needed and
generating GitLab releases to publishing your package. It removes the headache you can have determining which
version of the software is needed, and the content of your release note. Learn more on the
[official documentation](https://semantic-release.gitbook.io/semantic-release/){:target="_blank"}.

## How to use it

!!! info
    [Configuration file](https://semantic-release.gitbook.io/semantic-release/usage/configuration#configuration-file){:target="_blank"}
    can be written through different format, be sure to use a valid one (e.o. in `package.json` or `.releaserc`).

1. Have a valid `semantic-release` configuration stored in a file `./releaserc`  (use `SEMANTIC_CONFIG_PATH` if path is different)
1. Add a [CI/CD variable](https://docs.gitlab.com/ee/ci/variables/#add-a-cicd-variable-to-a-project) named `GITLAB_TOKEN` containing a GitLab access token with `api` access and `Maintainer` role on the project to release
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables

!!! info
    You can run this job in `dry run` mode, so you don't pollute your repository with testing
    tags & releases. All you have to do is setting `SEMANTIC_DRY_RUN` as `true`, and put it right
    back to `false` as soon as you are ready to release 🎉

| Name | Description | Default |
| ---- | ----------- | ------- |
| `SEMANTIC_CONF_PATH` | Direction where `semantic-release` config is available | `.releaserc` |
| `SEMANTIC_DRY_RUN` | Run the tool in [dry run](https://en.wikipedia.org/wiki/Dry_run_(testing)){:target="_blank"} | `false` |
| `GITLAB_TOKEN` | Authentication token to create the release (do not write in in clear, add it as project [CI/CD variable](https://docs.gitlab.com/ee/ci/variables/#add-a-cicd-variable-to-a-project))  | ` ` |
| `SEMANTIC_ADDITIONAL_OPTIONS` | Additional options to run on `semantic-release` command | ` ` |
| `SEMANTIC_ADDITIONAL_PACKAGES` | Additional packages to install needed to match your config (this job already installs all [official plugins](https://github.com/semantic-release/semantic-release/blob/master/docs/extending/plugins-list.md#plugins-list){:target="_blank"}) | ` ` |
| `SEMANTIC_RELEASE_VERSION` | `semantic-release` version | `19.0.5` |
| `SEMANTIC_GITLAB_VERSION` | `@semantic-release/gitlab` version | `9.5.0` |
| `SEMANTIC_GIT_VERSION` | `@semantic-release/git` version | `10.0.1` |
| `SEMANTIC_CHANGELOG_VERSION` | `@semantic-release/changelog` version | `6.0.2` |
| `SEMANTIC_EXEC_VERSION` | `@semantic-release/exec` version | `6.0.2` |
| `SEMANTIC_APM_VERSION` | `@semantic-release/apm` version | `4.0.2`
| `SEMANTIC_CONVENTIONALCOMITS_VERSION` | `conventional-changelog-conventionalcommits` version | `5.0.0`
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

## Cache

This job has the perk to use [cache](https://docs.gitlab.com/ee/ci/caching/){:target="_blank"},
it will be named as `${CI_COMMIT_REF_SLUG}-semantic-release`
and will cache `node_modules` generated by installation of `semantic-release` packages. So this
job will always try to be as fast as possible! 🚀

## Artifacts

This job will expose an artifact will the result from `semantic-release` and is exposed as `semantic-release logs`,
it is also available directly in the job's logs.
It also exposes the `RELEASE_VERSION` variable, containing the version number of the release. This variable can be used in next jobs.

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
