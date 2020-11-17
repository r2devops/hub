# 🔎 Zaproxy

## Description

Run a Dynamic Application Security Testing (DAST) in a docker image
using [Zaproxy](https://www.zaproxy.org/), the OWASP web app scanner.

## How to use it

!!! warning
    Zaproxy is fisrt used to scan web applications and web frontend. You can use the tool to try and discover
    API vulnerabilities, but this job is focused on a quick scan for a frontend service (with or without authentication)

1. Build a docker image of your web application so that this job can
use it as a service (we reccomend using our [Docker](https://hub.go2scale.io/jobs/build/docker_build/) job for it)
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/zaproxy.yml'

    zaproxy:
      services:
         - name: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
           alias: app
    ```
    You need the `services` part because you need to be able to reach your web application.
    You may also run some other services like a database depending on your application needs.
    The `name` variable is your image name, and the `alias` needs to match the `ZAP_TARGET` variable.
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
| `ZAP_OPTIONS` <img width=100/> | ZAP command line options e.g. `-z "-config aaa=bbb -config ccc=ddd"` <img width=175/>| ` ` <img width=100/>|
| `ZAP_CONTEXT` | Path for the context file for authenticated scans | ` ` |
| `ZAP_TARGET` | Target for zaproxy to scan, default using alias of the docker image used as a service | `http://app` |
