## Objective

Retrieve all job templates from a repository and create GitLab release (and git tag) for each versions listed in `CHANGELOG.md`

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the
   [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed
   version](#changelog) instead of `latest`.
1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Well done, your job is ready to work and will be execute on your main branch ! 😀


## Jobs files

**Here's the example structure of a job template folder:**
```
docker_build/
  ├── README.md
  ├── CHANGELOG.md
  └── docker_build.yaml (containing a job named docker_build )
```

A `CHANGELOG.md` is required to create the releases
- The structure of the `CHANGELOG.md` is based on [keepachangelog](https://keepachangelog.com/en/1.0.0/) structure.
- You could also checkout the [R2Devops documentation](https://docs.r2devops.io/job-structure/#job-changelogs) about it

**Here's an example of a `CHANGELOG.md`:**
```
# Changelog

## [1.1.0] - 2021-06-21
* Allows context different from root with new variable `DOCKER_CONTEXT_PATH`

## [1.0.0] - 2021-05-07
* Breaking change in the configuration of custom registry, see documentation
* Add support to push in multiple registries
* Add support to authentication in multiple registries

## [0.3.0] - 2020-11-25
* New variable `DOCKER_USE_CACHE` to be able to cache layers of build
* New variable `DOCKER_OPTIONS` to be able to add additional options

## [0.1.0] - 2020-10-21
* Initial version
```

!!! question "Can i use a self-hosted GitLab?"
   This job automatically utilize the host specified by the `CI_SERVER_HOST` GitLab predefined CI/CD variable inside the `GITLAB_API_URL` variable
## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `JOBS_DIRECTORY` | The root directory containing the job folders | `.` |
| `IMAGE_TAG` | The default tag for the docker image [alpine/httpie](https://hub.docker.com/r/alpine/httpie) | `3.2.1` |
| `GITLAB_API_URL` | The host name of the GitLab instance | `${CI_SERVER_HOST}` |
| `CHANGELOG_FILE` | The name of changelog files (case insensitive) | `CHANGELOG.md` |

## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Totara-thib](https://gitlab.com/Totara-thib)
