## Objective

This job will run a predefined `lint` script in your `package.json` which will check your code quality.


## How to use it

1. Make sure that your project has 
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the required `lint` command in the `scripts` object
2. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](/versioning/) instead of `latest`, use the version selector at the top right of the page.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. You are done, the job is ready to use ! 😉


## Job details

* Job name: `yarn_lint`
* Default stage: `tests`
* Docker image: [`node:17.8.0-buster-slim`](https://hub.docker.com/_/node){:target="_blank"}
* When: `always`


## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative path to the directory containing `package.json` (**see warning below**)  | ` ` |
| `YARN_INSTALL_OPTIONS` | Additional options for `yarn install` | ` ` |
| `YARN_LINT_OPTIONS` | Additional options for `yarn run lint` | ` ` |

!!! warning
    In the case you are updating `PROJECT_ROOT` and you want to have a properly working cache,
    consider making this variable a global variable in the root of your `.gitlab-ci.yml`. Learn how
    easy it is [here](https://docs.gitlab.com/ee/ci/variables/#create-a-custom-cicd-variable-in-the-gitlab-ciyml-file).
    

### Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Each branch has its own version
* Cached directory is `$PROJECT_ROOT/node_modules`
* If `package.json` or `yarn.json` is edited, the cache is updated

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).