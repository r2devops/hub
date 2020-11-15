# 🐳 Docker

## Description

Build a [docker](https://www.docker.com/) image of your application
from a Dockerfile at the root of your project, and push it to a
remote registry. The build part is done using
[kaniko](https://github.com/GoogleContainerTools/kaniko).

!!! info
    By default, your images will be pushed to the Gitlab Container
    Registry of your Gitlab instance.

## How to use it

1. Create a
   [Dockerfile](https://docs.docker.com/get-started/part2/#sample-dockerfile) (by default at the root of your project)
   to containerize your application
2. Choose a version in [version list](#changelog)
3. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/getting-started)). Example:
    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/docker_build.yml'
    ```
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/getting-started/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `docker_build`
* Docker image: [`gcr.io/kaniko-project/executor:debug-v0.20.0`](https://github.com/GoogleContainerTools/kaniko)
* Default stage: `build`

### Build behavior

!!! info
    This build will use Gitlab CI predefined [environment variables]
    (https://docs.gitlab.com/ee/ci/variables/predefined_variables.html)
    to know you are in a `commit` context or a `tag` context
    (for example if you are releasing a new version of your project).

The registry and tag of the resulting Docker image follow this behavior:

| `CUSTOM_REGISTRY` used ? <img width=10/> | `CUSTOM_TAG` used ? | Are you pushing git tag ? | Registry where image is pushed | Docker tag applied to the image |
|:-|:-|:-|:-|:-
| No  | No  | No  | Gitlab project registry | Last commit SHA |
| No  | No  | Yes | Gitlab project registry | Git tag name    |
| No  | Yes | No  | Gitlab project registry | `CUSTOM_TAG`    |
| No  | Yes | Yes | Gitlab project registry | `CUSTOM_TAG`    |
| Yes | No  | No  | `CUSTOM_REGISTRY`       | Last commit SHA |
| Yes | No  | Yes | `CUSTOM_REGISTRY`       | Git tag name    |
| Yes | Yes | No  | `CUSTOM_REGISTRY`       | `CUSTOM_TAG`    |
| Yes | Yes | Yes | `CUSTOM_REGISTRY`       | `CUSTOM_TAG`    |

### Variables

| VARIABLE NAME | DESCRIPTION | DEFAULT VALUE |
|:-|:-|:-
| `CUSTOM_REGISTRY` <img width=100/> | If you want to use another registry than the Gitlab one | ` ` |
| `REGISTRY_USER` | To authenticate with the `CUSTOM_REGISTRY` | ` ` |
| `REGISTRY_PASSWORD` | To authenticate with the `CUSTOM_REGISTRY` | ` ` |
| `CUSTOM_TAG` | If you want a specific tag for your image | ` ` |
| `COMMIT_CREATE_LATEST` | In a commit context, also update `latest` tag | `false` |
| `TAG_CREATE_LATEST` | In a tag context, also update `latest` tag | `true` |
| `DOCKERFILE_PATH` | Path to Dockerfile from the repository root | `Dockerfile` |
