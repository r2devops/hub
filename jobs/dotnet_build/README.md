## Objective

Builds a .NET Core project with the different versions available, and makes it ready to run.
It is using the scripted installation provided from Microsoft, see [here](https://docs.microsoft.com/en-us/dotnet/core/install/linux-alpine#scripted-install){:target="_blank"}.

## How to use it

1. Prepare your project in your repository with its `.csproj` file.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)

4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DOTNET_OUTPUT` <img width=100/> | Path to the output build (used as artifact) <img width=175/>| `/build` <img width=100/>|
| `DOTNET_VERSION` | .NET version used to build. You have the choice between multiples versions (see [versions](https://github.com/dotnet/installer#installers-and-binaries){:target="_blank"}). | `3.1` |
| `DOTNET_VERBOSITY` | Prints more or less logs (*Types available*: `q[uiet]`, `m[inimal]`, `n[ormal]`, `d[etailed]` and `diag[nostic]`) | `m` |
| `DOTNET_CONFIG` | Configuration profile used to build | `Debug` |
| `DOTNET_READY_TO_RUN` | Compiles the application as R2R (see [Ready to Run](https://docs.microsoft.com/en-us/dotnet/core/deploying/ready-to-run){:target="_blank"}) | `false`
| `DOTNET_SINGLE_FILE` | Publish as single file (more [info](https://github.com/dotnet/designs/blob/master/accepted/2020/single-file/design.md){:target="_blank"}) | `false`
| `DOTNET_TRIMMED` | Remove unused libraries when publishing, must be used with `DOTNET_SELF_CONTAINED`. Available from 3.0 (more [info](https://docs.microsoft.com/en-us/dotnet/core/deploying/trim-self-contained){:target="_blank"}). |  `false`
| `DOTNET_SELF_CONTAINED` | Publish the .NET Core runtime along with the build | `false`
| `DOTNET_OPTIONS` | Additional options from user | ` `
| `PROJECT_ROOT` | The location of the .NET project in your repository | `/` |
| `IMAGE_TAG` | The default tag for the docker image | `3.12.1`  |

!!! warning
    Since **version 5.0** of .NET is still in **release-candidate** at this time, the format of `DOTNET_VERSION` is slightly different from just `3.1` or `2.1`. See [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script#options){:target="_blank"} (*argument `-Channel`*) to see how to specify this new version.

## Artifacts

When the job is successful, the build of your project is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `dotNET Build` in merge requests.
    Exposition of artifact currently works only if you keep `DOTNET_OUTPUT`
    default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)
