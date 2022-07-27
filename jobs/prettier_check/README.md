## Objective

This jobs will run a `prettier --check` command. It's an opinionated code formatter with multiple support for JavaScript, TypeScript, JSX and many [others](https://prettier.io/docs/en/index.html). You can customize it to your needs by specifying rules in [specific files](https://prettier.io/docs/en/configuration.html).

## How to use it


1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Path to the root of project <img width=175/>| `.` <img width=100/>|
| `PRETTIER_SOURCE` <img width=100/> | Relative path to the directory to scan <img width=175/>| `./src` <img width=100/>|
| `PRETTIER_VERSION` <img width=100/> | Version of Prettier <img width=175/>| `2.6.2` <img width=100/>|
| `OUTPUT_DIRECTORY` <img width=100/> | Output directory where to save files checked. None if empty <img width=175/>| `prettier-report` <img width=100/>|
| `ADDITIONAL_OPTIONS` <img width=100/> | Additional options for Prettier <img width=175/>| ` ` <img width=100/>|
