## Objective

This job will allow you to migrate the database using a migration file that you already have in `database/migrations`, and it provides an artifact with all the logs at the end

## How to use it

!!! info
    You can use this job with all Data Base Management Systems (MySQL, PostgreSQL ...), you just need to link your remote database in the environment variables file, so make sure that you are using the correct database credentials.
    

1. Ensure that your project has a pre-made environment file such as `.env.testing` in example, which contains the variables that will be used by the project.
2. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/artisan_migrate.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀


## Job details

* Job name: `artisan_migrate`
* Default stage: `deploy`
* Docker image: [`edbizarro/gitlab-ci-pipeline-php:7.3`](https://hub.docker.com/r/edbizarro/gitlab-ci-pipeline-php){:target="_blank"}
* When: `manual`, only when running on default branch (`$CI_DEFAULT_BRANCH`).
  To update this behavior, see [job customization](https://r2devops.io/use-the-hub/#global) to override [`rules`](https://docs.gitlab.com/ee/ci/yaml/#rulesif)

### Variables

!!! info
    If you have setup Gitlab's CI/CD variables, they will be used instead of the ones defined in `.env`, just make sure to name them exactly the same.
    
| Name | Default | Description |
| ---- | ------- | --------------- |
| `PROJECT_ROOT` | `.` | Path to the directory containing environment variables |
| `ENV_NAME` | `.env.testing` | Name of the environment variables file to use | 
| `ARTISAN_MIGRATE_OPTIONS` | ` ` | Options for command `php artisan migrate` |
| `ARTISAN_OUTPUT` | `artisan_migration.log` | Name for logs file |


### Artifacts

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


### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)