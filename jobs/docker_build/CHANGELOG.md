# Changelog
All notable changes to this job will be documented in this file.

## [2.0.2] - 2024-03-08
* New release required by the R2Devops upgrade to 1.33

## [2.0.1] - 2023-02-28
* Fix broken documentation links

## [2.0.0] - 2022-07-29
* 🚨 **BREAKING CHANGE**
  Variable `DOCKER_TAG` updated to `DOCKER_TAGS` to use multiple tags in image building. 
* Add new variable `DOCKER_SNAPSHOT_MODE` to modify the filesystem's snapshot
* Update kaniko image to `v1.8.1`

## [1.2.0] - 2022-06-13
* Add docker image tag in variable 

## [1.1.0] - 2021-06-21
* Allows context different from root with new variable `DOCKER_CONTEXT_PATH`

## [1.0.0] - 2021-05-07
* Breaking change in the configuration of custom registry, see documentation
* Add support to push in multiple registries
* Add support to authentication in multiple registries

## [0.4.0] - 2021-04-19
* Add new option `--use-new-run` to kaniko executor (enabled by default)
* Update kaniko image to `v1.5.1`

## [0.3.0] - 2020-11-25
* New variable `DOCKER_USE_CACHE` to be able to cache layers of build
* New variable `DOCKER_CACHE_TTL` to define time to live of cache
* New variable `DOCKER_VERBOSITY` to set the verbosity of the build
* New variable `DOCKER_OPTIONS` to be able to add additional options

## [0.2.0] - 2020-11-02
* Add variable `DOCKERFILE_PATH` which permits specifying custom path to
  Dockerfile

## [0.1.0] - 2020-10-21
* Initial version
