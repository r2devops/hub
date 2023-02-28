# Changelog
All notable changes to this job will be documented in this file.

## [1.7.1] - 2023-02-28
* Fix broken documentation links

## [1.7.0] - 2022-11-22
* Update docker image tag

## [1.6.1] - 2022-06-13
* Add docker image tag in variable 

## [1.5.1] - 2022-04-06
* Change old link in the job code

## [1.5.0] - 2022-01-11
* Update `material for mkdocs` image version to 8.1.4
* Remove `mkdocs-awesome-pages-plugin`,`mkdocs-git-revision-date-localized-plugin`, `mkdocs-macros-plugin` plugins
* Add `MKDOCS_ADDITIONAL_PLUGINS` variable and execute a loop to install each plugins

## [1.4.1] - 2021-03-04
* Enable `artifact:expose_as` option to display job result in merge request

## [1.4.0] - 2021-01-29
* Update default output location from `documentation_build/` to `website_build/`

## [1.3.0] - 2020-12-08
* Update material for mkdocs version to 6.1.7
* Add mkdocs-awesome-pages plugin

## [1.2.0] - 2020-12-01
* Add mkdocs-macros-plugin to be able to use {{variable}} in the documentation

## [1.1.0] - 2020-11-16
* Update material for mkdocs version to 6.1.5
* Fix the current title tab name on navigation

## [1.0.0] - 2020-10-20
* Update material for mkdocs version to 6.0.2
* Manually install mkdocs-git-revision-date-localized-plugin since it's no more included in material for mkdocs docker image

## [0.1.0] - 2020-10-02
* Initial version
