# Changelog
All notable changes to this job will be documented in this file.

## [1.3.0] - 2023-03-02
* Add `GOLINT_VERSION` variable to specify the version of golangci-lint
* Change `IMAGE_TAG` from `v1.50.1` to `alpine3.17`
* Change the default image from `golangci/golangci-lint` to `golang` 

## [1.2.1] - 2023-02-28
* Fix broken documentation links

## [1.2.0] - 2022-10-28
* Add `GOLINT_OUTPUT_FORMAT` variable to export the report as `junit` or `code-climate` artifact
* Fix the Junit report artifact

## [1.1.0] - 2022-06-13
* Add docker image tag in variable 

## [1.0.0] - 2022-04-14
* Change the default stage into `tests`

## [0.1.0] - 2022-04-04
* Initial version
