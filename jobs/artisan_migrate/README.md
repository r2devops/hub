## Objective

This job will allow you to migrate the database using a migration file that you already have in `database/migrations`, and it provides an artifact with all the logs at the end

## How to use it

!!! info
    You can use this job with all Data Base Management Systems (MySQL, PostgreSQL ...), you just need to link your remote database in the environment variables file, so make sure that you are using the correct database credentials.
    

1. Ensure that your project has a premade environment file such as `.env.testing` in example, which contains the variables that will be used by the project.
2. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/artisan_migrate.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀


## Job details

* Job name: `artisan_migrate`
* Default stage: `build`
* Docker image: [`edbizarro/gitlab-ci-pipeline-php:7.3`](https://hub.docker.com/r/edbizarro/gitlab-ci-pipeline-php){:target="_blank"}
* When: `always`


### Variables

| Name | Default | Description |
| ---- | ------- | --------------- |
| `PROJECT_ROOT` | `.` | Path to the directory containing environment variables |
| `ENV_NAME` | `.env.testing` | Name of the environment variables file to use | 
| `ARTISAN_MIGRATE_OPTIONS` | ` ` | Options for command `php artisan migrate` |
| `ARTISAN_OUTPUT` | `artisan_migration.log` | Name for logs file |


### Artifact

When the job is done, the command output will be available under the file name `ARTISAN_OUTPUT` as an artifact.