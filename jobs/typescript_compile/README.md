## Objective

A job transpiling your typescript code into JavaScript using
[TypeScript compiler](https://www.npmjs.com/package/typescript).

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. Choose an option

    !!! tip "Plug and play available !"
      This job is **plug and play** 🚀, see the Option 1

      Other options need some configuration.

    ??? summary "Option 1: Choose the **plug and play** 🚀 mode"
      You don't have much to do, you can already **go to the next step**!<br/>
      In case you want the transpiler to work on a specific folder, consider
      updating the variable `PROJECT_ROOT` with the target folder path.<br/><br/>
      This job is using the command `tsc --init` as a **default config** file.

    ??? summary "Option 2: Have your own configuration"
      If you already have `tsconfig.json` or `jsconfig.json` at the root of your
      project, you **don't have anything to do**! 🚀 <br/>
      If the location of your configuration file is somewhere else in the project,
      update the variable `PROJECT_ROOT` with the directory containing the config file.

2. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
3. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | The directory containing your project and `tsconfig.json` or `jsconfig.json` <img width=175/>| ` ` <img width=100/>|
| `TARGET_OUTPUT` | The output directory of the transpiled code | `dist` |
| `NODE_VERSION` | The used version of `Node` (see [versions](https://nodejs.org/en/download/releases/)) | `14.16.0-r0` |
| `TYPESCRIPT_VERSION` | The used version of `TypeScript` (see [versions](https://www.npmjs.com/package/typescript)) | `4.2.3` |
| `IMAGE_TAG` | The default tag for the docker image | `3.13`  |

## Artifacts

Typescript compiler results are available as artifact.

!!! warning
    It's also
    [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"} `Typescript compile` in merge requests.
    Exposition of artifact currently works only if you keep `TARGET_OUTPUT` as
    default value because of
    [this issue from Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)
