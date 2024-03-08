## Objective

This job will install pnpm packages based on pnpm-lock.yaml file. Here the [doc of pnpm install](https://pnpm.io/cli/install). `pnpm` is so crazy faster than `npm` or `yarn`. You can check the [benchmark here](https://pnpm.io/benchmarks).

## How to use it

!!! warning
    You should have `pnpm-lock.yaml` otherwise you have to create and fulfill the `.npmrc` with the following content:
    ``` 
    auto-install-peers=true
    strict-peer-dependencies=false
    ```

1. Ensure that your project has `pnpm-lock.yaml` file and up to date with `package.json`.
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Relative path to the directory containing `pnpm-lock.yaml` and `package.json` (**see warning below**)  | `.` |
| `PNPM_INSTALL_OPTIONS` | Additional options for `pnpm install` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `20-buster`  |

!!! warning
    In the case you are updating `PROJECT_ROOT` and you want to have a properly working cache,
    consider making this variable a global variable in the root of your `.gitlab-ci.yml`. Learn how
    easy it is [here](https://docs.gitlab.com/ee/ci/variables/#create-a-custom-cicd-variable-in-the-gitlab-ciyml-file).

## Cache

This job creates a global cache configuration. Regarding the configuration
applied, cache behavior is the following:

* Each branch has its own version
* Cached directory is `$PROJECT_ROOT/node_modules`
* If `package.json` or `pnpm-lock.yaml` is edited, the cache is updated

More information on Gitlab caching mechanism in [Gitlab CI/CD caching
documentation](https://docs.gitlab.com/ee/ci/caching/index.html).

## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)