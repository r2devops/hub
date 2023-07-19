## Objective

This job will run one or many scripts contained in the package.json through pnpm package manager

## How to use it

1. Make sure that your project has `package.json` file which contains predefined command in the scripts object
2. If you want the job to run scripts make sure to add them inside the variable `PNPM_SCRIPTS` and separate every command with `;`
3. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
5. Well done, your job is ready to work ! 😀

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` | Path to the directory containing `package.json`  | `.` |
| `PNPM_INSTALL_OPTIONS` | Additional options for `pnpm install` | ` ` |
| `PNPM_SCRIPTS` | The names of multiple scripts specified in `package.json` that can be separated by `;` | ` ` |
| `PNPM_OUTPUT` | Path to the output send by script specified in `package.json` | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `20-buster`  |

### Example to use several scripts

Following example of `.gitlab-ci.yml` file describes how to use `pnpm_scripts` job.
deployment using this job:

#### Scripts in Package.json

```yaml
  "scripts": {
    "build": "ng build",
    "lint": "ng lint"
  }
```

#### .gitlab-ci.yml

```yaml
stages:
  - others

include:
  - remote: 'https://api.r2devops.io/job/r/r2devops-bot/pnpm_scripts.yml'

pnpm_scripts:
  variables:
    PNPM_SCRIPTS: "build;lint"
    PNPM_OUTPUT: "dist"
```

### Author

This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@DjNaGuRo](https://gitlab.com/DjNaGuRo)