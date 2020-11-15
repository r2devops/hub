# 🌐 .NET Build

## Description

Builds a .NET Core project with the different versions available, and makes it ready to run.
It is using the scripted installation provided from Microsoft, see [here](https://docs.microsoft.com/en-us/dotnet/core/install/linux-alpine#scripted-install).

## How to use it

1. Prepare your project in your repository with its `.csproj` file.
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/dotnet_build.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)

4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `dotnet_build`
* Docker image: [`alpine:3.12.1`](https://hub.docker.com/_/alpine)
* Default stage: `build`

### Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
|:-|:-|:-
| `DOTNET_OUTPUT` <img width=230/> | Path to the output build (used as artifact) <img width=175/>| `/build` <img width=100/>|
| `DOTNET_VERSION` | .NET version used to build. You have the choice between multiples versions (see [versions](https://github.com/dotnet/installer#installers-and-binaries)). | `3.1` |
| `DOTNET_VERBOSITY` | Prints more or less logs (*Types available*: `q[uiet]`, `m[inimal]`, `n[ormal]`, `d[etailed]` and `diag[nostic]`) | `m` |
| `DOTNET_CONFIG` | Configuration profile used to build | `Debug` |
| `DOTNET_READY_TO_RUN` | Compiles the application as R2R (see [Ready to Run](https://docs.microsoft.com/en-us/dotnet/core/deploying/ready-to-run)) | `false`
| `DOTNET_SINGLE_FILE` | Publish as single file (more [info](https://github.com/dotnet/designs/blob/master/accepted/2020/single-file/design.md)) | `false`
| `DOTNET_TRIMMED` | Remove unused libraries when publishing, must be used with `DOTNET_SELF_CONTAINED`. Available from 3.0 (more [info](https://docs.microsoft.com/en-us/dotnet/core/deploying/trim-self-contained)). |  `false`
| `DOTNET_SELF_CONTAINED` | Publish the .NET Core runtime along with the build | `false`
| `DOTNET_OPTIONS` | Additional options from user | ` `
| `PROJECT_ROOT` | The location of the .NET project in your repository | `/` |

!!! warning
    Since **version 5.0** of .NET is still in **release-candidate** at this time, the format of `DOTNET_VERSION` is slightly different from just `3.1` or `2.1`. See [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script#options) (*argument `-Channel`*) to see how to specify this new version.

### Artifacts

When the job is successful, the build of your project is available in an artifact. The artifact is `exposed_as` (see [expose](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as)) `dotNET Build` in your merge request.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129). As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.