## Objective

Retrieve all templates from a repository and create GitLab release (and git tag) for each versions listed in `CHANGELOG.md`

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed
   version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. The job can be run "out of the box". If you need to personalize its
   behavior, check the **variables section**
3. Well done, your job is ready to work and will be execute on your main branch ! 😀


## Jobs files

**Here is an example of a job metadata file:**

```yaml
files: # mandatory
    template: ./jobs/docker_build/docker_build.yml  # mandatory
    documentation: ./jobs/docker_build/README.md # optional
    changelog: ./jobs/docker_build/CHANGELOG.md # mandatory
data: # optional
    description: "A ready-to-use docker job to push the image of your project repository to the GitLab registry"
    public: false
    deprecated: false
    license: MIT
    icon: 🐳
    labels:
      - Lint
      - Security
      - Test

```
A job metadata file is required to create the releases. It should follow these rules:

- The files must be named with an extension defined by the variable `METADATA_FILE_EXTENSION`. By default, it is set to `.r2.yml`
- The entries in this file must have relative paths linking the job metadata file to the job template, documentation, and changelog files.
- The changelog path must be defined and must be a valid file.
- The template path must be defined and must be a valid file.

For more information about job templates, check the [documentation](https://docs.r2devops.io/get-started/manage-templates/#template-r2-file).


**Here's the example structure of a job template folder:**
```
docker_build/
  ├── README.md
  ├── CHANGELOG.md
  └── docker_build.yml (containing a job named docker_build )
```

A `CHANGELOG.md` file as explained in the previous example, is required to create releases. It should follow these rules:

- The structure of the `CHANGELOG.md` is based on [keepachangelog](https://keepachangelog.com/en/1.0.0/) structure.
- You could also checkout the [R2Devops documentation](https://docs.r2devops.io/get-started/manage-templates/#template-changelog) about it

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

## Semantic tagging feature

This job usually create when a new R2 template has been created or modified, a **gitlab release** for the detected R2 template.
This release has the following form :
```
<<R2template_name>>@<<MAJOR>>.<<MINOR>>.<<PATCH>>
```

When the semantic tagging is enabled, in addition, this job will add **git tag** in the form of :
```
<<R2template_name>>@<<MAJOR>>
```
and
```
<<R2template_name>>@<<MAJOR>>.<<MINOR>>
```

This will allow your users to include in their pipelines the latest MAJOR version of a job or the latest MAJOR.MINOR version of a job without to go back in the CI/CD editor each time a PATCH or MINOR version of a R2 template is published reducing the total cost of ownership of the R2DevOps solution


## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `IMAGE_TAG` | The default tag for the docker image [alpine/httpie](https://hub.docker.com/r/alpine/httpie) | `3.2.1` |
| `GITLAB_API_URL` | The domain of GitLab instance | `${CI_SERVER_HOST}` |
| `METADATA_FILE_EXTENSION` | The extension of metadata files | `.r2.yml` |
| `RELEASE_PATH` | The path where releases files are exposed as artifacts | `${CI_PROJECT_DIR}/releases` |
| `RELEASE_ONLY_LATEST_VERSION` | Release only the latest version from changelog files | `true` |
| `SEMANTIC_TAGGING_ENABLED` | Semantic tagging add MAJOR and MAJOR.MINOR tagging of the repo | `false` |
| `PRIVATE_TOKEN` | A personal or repo token required only when `SEMANTIC_TAGGING_ENABLED` is set to true to be able to update git tags | ` ` |
