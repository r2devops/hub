## Objective

This job will run your predefined `test` command which **must** use [jest](https://jestjs.io/) tool, and fails in case one of
your test is failed. You must have **jest** listed in your `package.json` dependencies, else the job won't work.
On top of rolling your tests for you, it will create you a coverage report
[badge](https://docs.gitlab.com/ee/user/project/badges.html).

!!! tip
    If you are using `create-react-app`, your app is using
    [`react-scripts`](https://github.com/facebook/create-react-app/tree/master/packages/react-scripts) and so is already
    using `jest`.

## How to use it

!!! note
    Depending on the lock file found (e.g. `package-lock.json` or `yarn.lock`), this job will use
    the appropriate tool.

1. Make sure that your project has
   [`package.json`](https://docs.npmjs.com/cli/v6/configuring-npm/package-json){:target="_blank"}
   file which contains the required `test` command in the `scripts` object and `jest` listed in your dependencies
2. Ensure the `test` command use  `jest` (or any tool using jest)
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. You are done, the job is ready to use ! 😉


## Variables

!!! note
    All paths defined in variables are relative and start from the root of your
    repository.

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `JEST_INCREMENTAL` | Run tests that only are relevant based on last commit changes | `false` |
| `PASS_WITH_NO_TESTS` | If set to true, the job will not fail if no tests are present | `true` |
| `ADDITIONAL_OPTIONS` | Additional options for your `jest` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `18.1-alpine3.14`  |


## Code coverage

This job implements the code coverage using the default
[coverage provider](https://jestjs.io/docs/cli#--coverageproviderprovider)
given by jest.

The code coverage will create you a badge available at anytime from the below link. You can learn more
about it [here](https://docs.gitlab.com/ee/ci/pipelines/settings.html#pipeline-badges).
```
https://gitlab.com/{YourUsername}/{YourProject}/badges/{YourBranch}/coverage.svg
```

On top of that, the code coverage is also available through
[merge request widgets](https://docs.gitlab.com/ee/ci/pipelines/settings.html#test-coverage-parsing)
to quickly what is your code coverage.
## Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget. It's also available directly in the artifacts.




## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)
