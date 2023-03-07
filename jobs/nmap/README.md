## Objective

!!! error "This job is deprecated 🚨"
    The job is no more maintained and is now deprecated. Despites it still exists to keep working on pipelines.

[Nmap](https://nmap.org) is a tool designed to discover networks, map them, and
information that they could offer by being reachable on the internet. Its
powerful [scripting engine](https://nmap.org/book/nse.html) is very
flexible to retrieve this information.

This `nmap` job allows you to scan automatically your deployed server or the
new version you want to deploy. It is able to list every ports opened and check
if one of them should not be.

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick use](https://docs.r2devops.io/get-started/use-templates/#use-a-template)). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    - Option 1: external service

    Add the IP address or the domain name of the service in `NMAP_TARGET`
    (see [jobs customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization))

    - Option 2: container instance

    Add the target container instance as a service (see
    [Container instance as Service]((https://docs.r2devops.io/get-started/use-templates/#use-a-template))/#container-instance-as-service))
    and set `NMAP_TARGET` as the name of your container.

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NMAP_TARGET` <img width=100/> | The target server, its IP or domain name <img width=175/>| `app` <img width=100/>|
| `NMAP_SCRIPTS` | Comma separated list of lua [scripts](https://nmap.org/book/nse.html) to run | ` ` |
| `NMAP_OPTIONS` | Additional options you may want for the scan (`man nmap`) | ` ` |
| `NMAP_OUTPUT` | Name for the XML output file for nmap | `nmap-report.xml` |
| `HTML_OUTPUT` | Name for the html file for the Merge Request Widget for this job | `nmap-report.html` |
| `LIBXSLT_VERSION` | Tool's version of LibXslt | `1.1.34-r1` |
| `IMAGE_TAG` | The default tag for the docker image | `7.92`  |

## Artifacts

Nmap result is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `Nmap report` in merge requests.  Exposition of artifact currently works
    only if you keep `HTML_OUTPUT` default value because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)
