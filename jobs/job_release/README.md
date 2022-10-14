## Objective

Retrieve all versions of multiple jobs and create release for each entry inside their `CHANGELOG.md` files 

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the
   [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed
   version](#changelog) instead of `latest`.
1. The job can be run "out of the box". If you need to personalize its
   behavior, check the [variables section](#variables)
1. Well done, your job is ready to work and will be execute on your main branch ! 😀

## Behavior

By default, this job will be run on the `jobs` directory located at the root of your project and will create releases for each directory containing jobs files.

## Jobs files

Here's the structure of a job files :

```
jobs 
   |
   job_name 
          |
          CHANGELOG.md
          job_name.yml
          README.md
   |
   job_name 
          |
          CHANGELOG.md
          job_name.yml
          README.md
```


A `CHANGELOG.md` is require for creating git tags release.
The structure of the `CHANGELOG.md` is based on [keepachangelog](https://keepachangelog.com/en/1.0.0/) structure.
You could also checkout the [R2Devops documentation](https://docs.r2devops.io/job-structure/#job-changelogs) about it

Here's an example of a `CHANGELOG.md` :

```
# Changelog
All notable changes to this job will be documented in this file.

## [0.1.0] - 2022-10-14
* Initial version
```

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `JOBS_DIRECTORY` <img width=100/> | The directory containing the jobs folders | `jobs` <img width=100/>|
| `IMAGE_TAG` | The default tag for the docker image [alpine/httpie](https://hub.docker.com/r/alpine/httpie) | `3.2.1` |
| `GITLAB_API_URL` | The url used to call the GitLab API. ⚠️ It should be changed if you using a self-hosted version | `gitlab.com` |


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Totara-thib](https://gitlab.com/Totara-thib)