## Objective

Run a Dynamic Application Security Testing (DAST) in a docker image
using [Zaproxy](https://www.zaproxy.org/), the OWASP web app scanner.

## How to use it

!!! warning
    Zaproxy is mainly used to scan web applications and web frontend. You can use the tool to try and discover
    API vulnerabilities, but this job is focused on a quick scan for a frontend service (with or without authentication)

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    - Option 1: external service

    Add the IP address or the domain name of the service in `ZAP_TARGET`
    (see [jobs customization](http://localhost:8000/use-the-hub/#jobs-customization))

    - Option 2: container instance

    Add the target container instance as a service (see
    [Container instance as Service](/use-the-hub/#container-instance-as-service))
    and set `ZAP_TARGET` as the name of your container.

1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `zaproxy`
* Docker image:
[`owasp/zap2docker-stable:2.9.0`](https://hub.docker.com/r/owasp/zap2docker-stable)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `ZAP_SCANNERS` <img width=100/> | Enable, disable, or list a set of [scanners](https://github.com/Grunny/zap-cli#getting-started-running-a-scan) <img width=175/> | ` ` <img width=100/> |
| `ZAP_CONTEXT` | Path for the [context](https://www.zaproxy.org/docs/desktop/ui/dialogs/session/contexts/) file for authenticated scans | ` ` |
| `ZAP_TARGET` | Target for Zaproxy to scan, default using alias of the docker image used as a service | `http://app` |
| `ZAP_REPORT_FILE` | Filename for the zaproxy report | `zap-report` |
| `ZAP_REPORT_FORMAT` | Format for the zaproxy report (html, xml, or json) | `html` |

### Artifacts

Zaproxy result is available as artifact.

!!! warning
    It's also [exposed as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Zaproxy report` in merge requests.
    Exposition of artifact currently works only if you keep `ZAP_REPORT_FILE`
    and `ZAP_REPORT_FORMAT` default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)