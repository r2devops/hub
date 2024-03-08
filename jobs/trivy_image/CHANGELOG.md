# Changelog
All notable changes to this job will be documented in this file.

## [1.3.2] - 2024-03-08
* New release required by the R2Devops upgrade to 1.33

## [1.3.1] - 2023-02-28
* Fix broken documentation links

## [1.3.0] - 2022-11-22
* Update trivy and docker images versions

## [1.2.0] - 2022-10-10
* Update trivy and docker images versions

## [1.1.0] - 2022-06-13
* Add docker image tag in variable 

## [1.0.0] - 2022-04-14
* Change the default stage into `tests`

## [0.4.0] - 2021-05-28
* Output all vulnerabilities even if severities are provided
* Change default value for `TRIVY_EXIT_CODE`

## [0.3.0] - 2021-05-11
* Add ability to exit on a particular severity
* Add possibility to append options for command `trivy`

## [0.2.0] - 2020-12-07
* Trivy image is now usable natively with docker_build job
* Merge both previous jobs (commit and tags) in only one
* Add variables to specify custom registry or tag

## [0.1.0] - 2020-10-02
* Initial version
