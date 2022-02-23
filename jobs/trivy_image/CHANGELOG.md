# Changelog
All notable changes to this job will be documented in this file.

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