## Objective

Run your [Venom](https://github.com/ovh/venom) tests

## How to use it

1. Write your test suite for Venom and specified the path to the test file with the `VENOM_TESTS` variable. Check the [documentation](https://github.com/ovh/venom#testsuites){:target="_blank"}.
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](https://docs.r2devops.io/get-started-use-the-hub/#quick-setup)). You can specify a fixed version instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started-use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

### Variables

| Name | Description                                                                                                                                                                       | Default |
| ---- |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| `PROJECT_ROOT` | Relative path in your repository to your project.                                                                                                                       | `.`     |
| `VENOM_VERSION` | The Venom version to install and execute.                                                                                                                              | `1.0.1` |
| `VENOM_TESTS` | Relative path to a single `yml` file which contains your test suite.                                                                                                     | ` `     |
| `REPORT_FORMAT` | Format of the Venom report, available formats are  JUnit (xml), json, yaml and tap.                                                                                    | `xml`   |
| `OUTPUT_DIRECTORY` | Directory path to the Venom reports output.                                                                                                                         | `dist`  |
| `ADDITIONAL_OPTIONS` | Possibility to add [more options](https://github.com/ovh/venom#executors){:target="_blank"} into the Venom command, like changing the default executor and more.  | ` `     |

## Author

This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@valentin.guyon.vg](https://gitlab.com/valentin.guyon.vg)