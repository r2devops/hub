## Objective

This job tests your final project by using Laravel Dusk, this will run tests that you already created beforehand and stored on the folder `tests/Browser`, all the logs, console output and screenshots, if generated, will be available as an artifact when the job succeeds.


## How to use it

1. Ensure that your project has Laravel Dusk installed (see how to do that [here](https://laravel.com/docs/8.x/dusk#installation){:target="_blank"})
2. Make sure your `DuskTestCase` class in `/tests/DuskTestCase.php` matches all attributes, like drive options, host url, and port, like in this example [DuskTestCase.php](https://github.com/chilio/laravel-dusk-ci/blob/master/examples/DuskTestCase.php){:target="_blank"}

    !!! warning
        There are some modifications which **you need to apply** (especially adding `--no-sandbox` in $options for driver), these changes should not affect your local dev environment, otherwise there might be something else wrong with your project.

3. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀


## Variables

!!! note
    All paths defined in variables are relative and starts from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the project's root directory   | `.` |
| `ENV_NAME` | Name of the environment variables file to use | `.env.testing` |
| `COMPOSER_INSTALL_OPTIONS` | Additional options for `composer install` | ` ` |
| `CHROME_DRIVER_VERSION` | Specific ChromeDriver version to use | `88` |
| `DUSK_OPTIONS` | Additional options for `php artisan dusk` | `--log-junit dusk_junit.xml` |
| `IMAGE_TAG` | The default tag for the docker image | `php-8.0`  |


## Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Shared between all jobs and pipelines on the same branch
* Contains folder `$PROJECT_ROOT/vendor`
* If `composer install` produces different result than the cached content

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).


## Artifact

When the job is done, it will provide an artifact containing the output from Dusk tests under these folders:

* `tests/Browser/console`
* `tests/Browser/screenshots`
* `storage/logs`

We also use Junit's XML report to display error report directly in pipeline `Tests` tab and in merge request widget. The report defined as `dusk_junit.xml` is also available directly in the artifact.


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
