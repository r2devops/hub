## Objective

Build a [docker](https://www.docker.com/){:target="_blank"} image of your application
from a Dockerfile at the root of your project, and push it to a remote registry or multiple ones. The build part is done using
[kaniko](https://github.com/GoogleContainerTools/kaniko){:target="_blank"}.

!!! info
    By default, your images will be pushed to the Gitlab Container
    Registry of your Gitlab instance.

## How to use it

1. Create a
   [Dockerfile](https://docs.docker.com/get-started/part2/#sample-dockerfile){:target="_blank"} (by default at the root of your project)
   to containerize your application
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `docker_build`
* Docker image: [`gcr.io/kaniko-project/executor:v1.5.1-debug`](https://github.com/GoogleContainerTools/kaniko){:target="_blank"}
* Default stage: `build`

### Build behavior

!!! info
    This build will use Gitlab CI predefined [environment variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html){:target="_blank"}
    to know you are in a `commit` context or a `tag` context
    (for example if you are releasing a new version of your project).

The registry and tag of the resulting Docker image follow this behavior:

| `CUSTOM_TAG` used ? | Are you pushing git tag ? | Registry where image is pushed | Docker tag applied to the image |
|:--------------------|:--------------------------|:-------------------------------|:--------------------------------|
| No                  | No                        | Gitlab project registry        | Last commit SHA                 |
| No                  | Yes                       | Gitlab project registry        | Git tag name                    |
| Yes                 | No                        | Gitlab project registry        | `CUSTOM_TAG`                    |
| Yes                 | Yes                       | Gitlab project registry        | `CUSTOM_TAG`                    |

!!! info
    In order to use custom registries, you need to provide the file `config.json` that contains the auths, you can do that by passing it as a [CI/CD file](https://docs.gitlab.com/ee/ci/variables/#cicd-variable-types){:target="_blank"} named `CONFIG_FILE` (see example below)

### Variables

| VARIABLE NAME                    | DESCRIPTION                                                                                                                                                                          | DEFAULT VALUE |
|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------|
| `CUSTOM_TAG`                     | If you want a specific tag for your image                                                                                                                                            | ` `           |
| `COMMIT_CREATE_LATEST`           | In a commit context, also update `latest` tag                                                                                                                                        | `false`       |
| `TAG_CREATE_LATEST`              | In a tag context, also update `latest` tag                                                                                                                                           | `true`        |
| `DOCKER_CONTEXT_PATH`            | Path of build context from to repository root                                                                                                                                        | ` `           |
| `DOCKERFILE_PATH`                | Path to Dockerfile from the build context (see `DOCKER_CONTEXT_PATH`)                                                                                                                | `Dockerfile`  |
| `DOCKER_USE_CACHE`               | Cache Dockerfile layers. Cached layers are stored in the [container registry](https://docs.gitlab.com/ee/user/packages/container_registry/){:target="_blank"} in `/cache` repository | `false`       |
| `DOCKER_CACHE_TTL`               | Cached layers TTL                                                                                                                                                                    | `336h`        |
| `KANIKO_USE_NEWRUN`              | Enable Kaniko option [`--use-new-run`](https://github.com/GoogleContainerTools/kaniko#--use-new-run)                                                                                 | `true`        |
| `DOCKER_VERBOSITY`               | Set the verbosity of the build in job's log (see [levels](https://github.com/GoogleContainerTools/kaniko#--verbosity){:target="_blank"})                                             | `info`        |
| `DOCKER_OPTIONS`                 | If you want to use additional [options](https://github.com/GoogleContainerTools/kaniko#additional-flags){:target="_blank"}                                                           | ` `           |
| `CUSTOM_REGISTRIES_DESTINATIONS` | the list of your remote registries + image tags (see example below)                                                                                                                  | ` `           |
| `CONFIG_FILE`                    | CI variable file that contains the auths for kaniko                                                                                                                                  | ` `           |
| `IMAGE_TAG`                    | The default tag for the docker image                                                                                                                                  | `1.21.1-4.1.3`           |

* Example of variable `CUSTOM_REGISTRIES_DESTINATIONS`:
    ```
    --destination registry.hub.docker.com/admin/myimages:latest --destination containerregistry.azurecr.io/admin/myimages:1.6.9-lite
    ```


* Example of file `CONFIG_FILE`:
    ```json
    {"auths":
        {
        "registry.hub.docker.com":{"username":"admin","password":"secret"},
        "containerregistry.azurecr.io":{"username":"admin","password":"password"}
        }
    }
    ```




### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)