## Objective

Run your [Venom](https://github.com/ovh/venom) tests

## How to use it

1. Write your test suite for Venom and specified the path to the test file with the `VENOM_TESTS` variable. Check the [documentation](https://github.com/ovh/venom#testsuites){:target="_blank"}.
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify a fixed version instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PROJECT_ROOT` <img width=100/> | Relative path in your repository to your project. <img width=175/> | `.` <img width=100/> |
| `VENOM_VERSION` | The Venom version to install and execute. | `1.0.1` |
| `VENOM_TESTS` | Relative path to a single `yml` file which contains your test suite. | ` `     |
| `REPORT_FORMAT` | Format of the Venom report, available formats are  JUnit (xml), json, yaml and tap. | `xml` |
| `OUTPUT_DIRECTORY` | Directory path to the Venom reports. | `dist` |
| `ADDITIONAL_OPTIONS` | Possibility to add [more options](https://github.com/ovh/venom#executors){:target="_blank"} into the Venom command, like changing the default executor and more. | ` ` |

## Author

This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)
