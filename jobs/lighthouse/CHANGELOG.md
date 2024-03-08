# Changelog
All notable changes to this job will be documented in this file.

## [1.2.1] - 2024-03-08
* New release required by the R2Devops upgrade to 1.33

## [1.2.0] - 2023-04-03
* Bump `IMAGE_TAG` from `89-with-node` to `102-with-node-16`
* Bump `LIGHTHOUSE_VERSION` from `7.2.0` to `10.1.0`
* Bump `SERVE_VERSION` from `11.3.2` to `14.2.0`

## [1.1.1] - 2023-02-28
* Fix broken documentation links

## [1.1.0] - 2022-06-13
* Add docker image tag in variable 

## [1.0.0] - 2022-04-14
* Change the default stage into `tests`

## [0.3.1] - 2022-04-06
* Change old link in the job code

## [0.3.0] - 2021-03-16
* Update the docker image used 
* Fix version of lighthouse

## [0.2.2] - 2021-03-04
* Enable `artifact:expose_as` option to display job result in merge request

## [0.2.1] - 2021-03-03
* Set a fixed version for docker image
* Set a fixed version for `serve` tool installed in plug-and-play part of the job

## [0.2.0] - 2021-02-23
* Remove `LIGHTHOUSE_TARGET` default value
* The pipeline will now fail if no target is defined
* New feature to run the job without any configuration

## [0.1.0] - 2020-12-30
* Initial version