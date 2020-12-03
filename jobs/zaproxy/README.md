# 🔎 Zaproxy

## Description

Run a Dynamic Application Security Testing (DAST) in a docker image
using [Zaproxy](https://www.zaproxy.org/), the OWASP web app scanner.

## How to use it

!!! warning
    Zaproxy is mainly used to scan web applications and web frontend. You can use the tool to try and discover
    API vulnerabilities, but this job is focused on a quick scan for a frontend service (with or without authentication)

1. Build a docker image of your web application so that this job can
use it as a service (we recommend using our [Docker](https://r2deveops.io/jobs/build/docker_build/) job for it)
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)) and add a `services` section. Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/zaproxy.yml'

    zaproxy:
      services:
         - name: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
           alias: app
    ```

    * You need the `services` part because you need to be able to reach your web application
    * The `name` option must contain your image name and tag
    * The `alias` option permits to Zaproxy to reach your application using a name. This name must be the same that the one specified inside [variable `ZAP_TARGET`](#variables)
    * You may also run some other services like a database depending on your application needs

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `zaproxy`
* Docker image:
[`owasp/zap2docker-stable:2.9.0`](https://hub.docker.com/r/owasp/zap2docker-stable)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `ZAP_SCANNERS` <img width=100/> | Enable, disable, or list a set of scanners <img width=175/> | ` ` <img width=100/> |
| `ZAP_CONTEXT` | Path for the [context](https://www.zaproxy.org/docs/desktop/ui/dialogs/session/contexts/) file for authenticated scans | ` ` |
| `ZAP_TARGET` | Target for Zaproxy to scan, default using alias of the docker image used as a service | `http://app` |
| `ZAP_REPORT_FILE` | Filename for the zaproxy report | `zap-report` |
| `ZAP_REPORT_FORMAT` | Format for the zaproxy report (html, xml, or json) | `html` |
