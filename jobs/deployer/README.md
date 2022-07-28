## Objective

Deploy your PHP project using [Deployer](https://deployer.org/){:target="_blank"}

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. Set the secret variable `SSH_PRIVATE_KEY` and `SSH_KNOWN_HOSTS`as CI/CD variables in [your Gitlab project](https://docs.gitlab.com/ee/ci/variables/README.html#project-cicd-variables){:target="_blank"}
   if you need encrypted variables.

    !!! info
        `SSH_KNOWN_HOSTS` needs to contain the same data that we find in the file `.ssh/known_hosts`, this step is needed so that the SSH connection doesn't ask to add the server to `.ssh/known_hosts` as you wouldn't be able to interact with the terminal.

1. Make sure that you have the deployer config file (`deploy.php` or `deploy.yaml`) in the root folder of your project, More info in [this guide](https://deployer.org/docs/getting-started.html){:target="_blank"}
1. If you need to customize other part of the job (stage, variables, ...) 👉
   check the [jobs customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Example of `deploy.php` file

```php
<?php

namespace Deployer;

// Include the Laravel recipe
require 'recipe/laravel.php';

set('application', getenv('CI_PROJECT_NAME')); // Configure from gitlab's env vars
set('ssh_multiplexing', true); // Speed up deployment

// Hosts
host('production.app.com') // Name of the server
    ->hostname('165.22.242.104') // Hostname or IP address
    ->stage('production') // Deployment stage (production, staging, etc)
    ->user('deploy') // SSH user
    ->set('deploy_path', '/var/www'); // Deploy path

// Tasks

desc('Deploy the application');
task('deploy', [
    'deploy:info',
    'deploy:prepare',
    'deploy:lock',
    'deploy:release',
    'deploy:shared',
    'deploy:vendors',
    'deploy:writable',
    'artisan:storage:link', // |
    'artisan:view:cache',   // |
    'artisan:config:cache', // | Laravel specific steps
    'artisan:optimize',     // |
    'artisan:migrate',      // |
    'deploy:symlink',
    'deploy:unlock',
    'cleanup',
]);
```

## Variables

!!! info
    All variables can be set using [Gitlab CI/CD
    variables](https://docs.gitlab.com/ee/ci/variables/README.html#project-cicd-variables) to
    avoid exposing them in clear text in your `.gitlab-ci.yml`. This is recommended
    for sensitive parameters such as `SSH_KNOWN_HOSTS` and it's **HIGHLY**
    recommended for secret variable `SSH_PRIVATE_KEY`.

| Name | Description | Mandatory | Default |
| ---- | ----------- | --------- | ------- |
| `SSH_PRIVATE_KEY` | Private SSH key to login on the `host` server | yes | ` `
| `SSH_KNOWN_HOSTS` | List of known_hosts for a seamless deployment | yes | ` `
| `PROJECT_ROOT` | Path to the directory containing `deploy.php` or `deploy.yaml` | no | `.` |
| `DEPLOY_OPTIONS` | Additional options for command `dep deploy` | no | ` ` |
| `DEPLOYER_OUTPUT` | Name for logs file | no | `deployer_output.txt` |
| `IMAGE_TAG` | The default tag for the docker image | `7.3-alpine`  |

## Artifacts

* If deployment succeeds: the job succeeds with the output as artifact
* If deployment fails: the job fails with the output as artifact

`dep deploy`'s output is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Deployer output` in merge requests.  Exposition of artifact currently works
    only if you keep `DEPLOYER_OUTPUT` default value because of [this issue
    from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.

## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@moha-s](https://gitlab.com/moha-s)
