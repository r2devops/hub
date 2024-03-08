## Objective

!!! error "This job is deprecated 🚨"
    The job is no more maintained and is now deprecated. Despites it still exists to keep working on pipelines.

Tool to check SSL/TLS related vulnerabilities of an URL

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Set the variable `TESTSSL_URL` with the URL you want to test
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
1. Well done, your job is ready to work ! 😀

## Variables



| Name | Description | Default |
| ---- | ----------- | ------- |
| `TESTSSL_URL` <img width=100/> | URL to test <img width=175/>| ` ` <img width=100/>|
| `TESTSSL_OPTIONS` | List of options to pass to testssl | ` ` |
| `TESTSSL_EXPORT_HTML` | Enable HTML export | `true` |
| `TESTSSL_EXPORT_HTML_FILENAME` | Name of the HTML export | `report.html` |
| `TESTSSL_EXPORT_JSON` | Enable JSON export | `true` |
| `TESTSSL_EXPORT_JSON_FILENAME` | Name of the HTML export | `report.json` |
| `TESTSSL_PARALLEL_MODE` | By default, all mass tests are done in serial mode, you can enable parallel testing (--parallel) | `true`|
| `TESTSSL_CHECK_LOCAL_CIPHER_REMOTELY` | Checks each local cipher remotely (-e) | `true`|
| `TESTSSL_FAST` | omits some checks: using openssl for all ciphers (-e), show only first preferred cipher (--fast) | `true`|
| `TESTSSL_TLS_SSL` | Checks TLS/SSL protocols (including SPDY/HTTP2) (-p) | `true`|
| `TESTSSL_VULNERABILITY` | Test all the vulnerabilities (-U) | `true`|
| `IMAGE_TAG` | The default tag for the docker image | `3.0`  |



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)
