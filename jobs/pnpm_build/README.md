## Objective

This job allows you to build your project with `pnpm` using a script (`build` by default)
from your `package.json` file. For more information see [the doc]('https://pnpm.io/cli/run')

## How to use it

1. Ensure that your project have
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the script required to build (`build` by default)
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json` (path relative from the root of the repository) | `.` |
| `PNPM_INSTALL_OPTIONS` | Additional options for `pnpm install` | ` ` |
| `PNPM_BUILD_SCRIPT_NAME` | The build script in the `package.json` that you want to run | `build` |
| `PNPM_BUILD_OPTIONS` | Options passed to your build script | ` ` |
| `PNPM_BUILD_OUTPUT_FOLDER` | Path to the output produced by the `pnpm` build script used (path relative from the `PROJECT_ROOT`) | `dist` |
| `PAGES_DEPLOY` | Prepare your build result to be deployed on pages (require [pages job](jobs/deploy/pages/)) | `false` |
| `PAGES_FOLDER` | Path where to copy the output to be exposed for deployment on [pages](jobs/deploy/pages/) (path relative from the root of the repository) | `./website_build` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

### Example to deploy on pages

Following example of `.gitlab-ci.yml` file describes how to enable Gitlab pages
deployment using this job:

```yaml
stages:
  - build
  - deploy

include:
  # It's recommanded to use fixed version of jobs instead of larest. Here is only for example.
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/pnpm_build/latest.yml' 
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/pages/latest.yaml'

pnpm_build:
  variables:
    PAGES_DEPLOY: "true"
```

### Artifact

When the job is successful, the build result is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `pnpm build` in merge requests.  Exposition of artifact currently works only
    if you keep `PNPM_BUILD_OUTPUT_FOLDER` default value because of [this issue
    from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.

### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)