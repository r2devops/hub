# Changelog
All notable changes to this job will be documented in this file.

## [1.6.0] - 2022-11-22
* Bump megalinter version to v6.13.0

## [1.5.0] - 2022-10-03
* Add `GITLAB_COMMENT_REPORTER` variable to displays errors in the comments section of merge requests
* Remove the `tap-junit` output conversion and use `sarif` by default
* Bump megalinter version to `v6.11.1`
* Remove `OUTPUT_FORMAT` and `OUTPUT_DETAIL` variables
* Activate `CSPELL` lint
* Remove default value of `FILTER_REGEX_EXCLUDE` variable
* Change the default value of `REPORT_OUTPUT_FOLDER` variable into `megalinter-reports`

## [1.4.0] - 2022-09-28
* Default output format is now `sarif` instead of `tap`(deprecated)
* Add CodeClimate output format for `sarif` output
* Bump megalinter version to `v6.8.0`

## [1.3.0] - 2022-08-25
* Bump megalinter version to `v6.6.0`

## [1.2.0] - 2022-08-16
* Use new image: `oxsecurity/megalinter`
* Bump megalinter version to `v6.3.0`
* Bump tap-junit version to `v5.0.2`

## [1.1.0] - 2022-06-13
* Add docker image tag in variable

## [1.0.0] - 2022-04-14
* Change the default stage into `tests`

## [0.1.1] - 2021-12-27
* Set correct return value for GitLab CI/CD pipeline if job succeeds

## [0.1.0] - 2021-07-23
* Initial version
