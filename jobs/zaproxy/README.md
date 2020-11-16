# 🔎 Zaproxy

## Description

Run a Dynamic Application Security Testing (DAST) in a docker image
using [Zaproxy](https://www.zaproxy.org/), the OWASP web app scanner.

## How to use it

1. Build a docker image of your web application so that this job can
use it as a service (we reccomend using our [Docker](https://hub.go2scale.io/jobs/build/docker_build/) job for it)
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.go2scale.io/zaproxy.yml'

    zaproxy:
      services:
         - name: {{ your image }}
           alias: app
    ```
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
| `ZAP_PORT` | Custom port if you have one for your project (zap will try 80/443 by default) | ` ` |
