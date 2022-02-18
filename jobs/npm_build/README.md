## Objective

This job allows you to build your project using a script (`build` by default)
from your `package.json` file.

## How to use it

1. Ensure that your project have
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the script required to build (`build` by default)
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/npm_build.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀


## Job details

* Job name: `npm_build`
* Default stage: `build`
* Docker image: [`node:15.7-buster`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json` (path relative from the root of the repository) | `.` |
| `NPM_INSTALL_OPTIONS` | Additional options for `npm install` | ` ` |
| `NPM_BUILD_SCRIPT_NAME` | The build script in the `package.json` that you want to run | `build` |
| `NPM_BUILD_OPTIONS` | Options passed to your build script | ` ` |
| `NPM_BUILD_OUTPUT_FOLDER` | Path to the output produced by the `npm` build script used (path relative from the `PROJECT_ROOT`) | `build` |
| `PAGES_DEPLOY` | Prepare your build result to be deployed on pages (require [pages job](jobs/deploy/pages/)) | `false` |
| `PAGES_FOLDER` | Path where to copy the output to be exposed for deployment on [pages](jobs/deploy/pages/) (path relative from the root of the repository) | `./website_build` |

### Example to deploy on pages

Following example of `.gitlab-ci.yml` file describes how to enable Gitlab pages
deployment using this job:

```yaml
stages:
  - build
  - deploy

include:
  - remote: 'https://jobs.r2devops.io/npm_build.yml'
  - remote: 'https://jobs.r2devops.io/pages.yml'

npm_build:
  variables:
    PAGES_DEPLOY: "true"
```

### Artifact

When the job is successful, the build result is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `npm build` in merge requests.  Exposition of artifact currently works only
    if you keep `NPM_BUILD_OUTPUT_FOLDER` default value because of [this issue
    from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.

This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)