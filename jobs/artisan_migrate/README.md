## Objective

!!! error "This job is deprecated 🚨"
    The job is no more maintained and is now deprecated. Despites it still exists to keep working on pipelines.

This job will allow you to migrate the database using a migration file that you already have in `database/migrations`, and it provides an artifact with all the logs at the end

## How to use it

!!! info
    You can use this job with all Data Base Management Systems (MySQL, PostgreSQL ...), you just need to link your remote database in the environment variables file, so make sure that you are using the correct database credentials.


1. Ensure that your project has a pre-made environment file such as `.env.testing` in example, which contains the variables that will be used by the project.
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀


## Variables

!!! info
    If you have setup Gitlab's CI/CD variables, they will be used instead of the ones defined in `.env`, just make sure to name them exactly the same.

| Name | Default | Description |
| ---- | ------- | --------------- |
| `PROJECT_ROOT` | `.` | Path to the directory containing environment variables |
| `ENV_NAME` | `.env.testing` | Name of the environment variables file to use |
| `ARTISAN_MIGRATE_OPTIONS` | ` ` | Options for command `php artisan migrate` |
| `ARTISAN_OUTPUT` | `artisan_migration.log` | Name for logs file |
| `IMAGE_TAG` | The default tag for the docker image | `7.3`  |

## Artifacts

When the job is done, the command's output will be available under the file name `ARTISAN_OUTPUT` as an artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Artisan migration` in merge requests.  Exposition of artifact currently works
    only if you keep `ARTISAN_OUTPUT` default value because of [this issue
    from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.


## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
