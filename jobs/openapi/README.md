## Objective

Creates an interactive version of an API documentation (see [demo](https://petstore.swagger.io/){:target="_blank"})
with [Swagger UI](https://swagger.io/tools/swagger-ui/){:target="_blank"}. It uses a [OpenAPI specifications](https://swagger.io/specification/){:target="_blank"}
(or [Swagger](https://swagger.io/docs/specification/2-0/basic-structure/){:target="_blank"}) file to be generated.

The version of SwaggerUI used is compatible with OpenAPI Specification 3.0 and 2.0 (fka Swagger).
This job let you the possibility to change SwaggerUI version (see [versions](https://github.com/swagger-api/swagger-ui#compatibility){:target="_blank"}) to match with older specifications versions.

## How to use it

1. Have a [compatible](#description) API specification file you can use in the job
2. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `API_DEF_LOCATION` <img width=250/> | Path to your OpenAPI file in your repository <img width=400/> | `openapi.json` |
| `SWAGGER_OUTPUT` | Output directory path | `website_build/` |
| `SWAGGERUI_VERSION` | Version of SwaggerUI (see [versions](https://github.com/swagger-api/swagger-ui#compatibility){:target="_blank"}) | `v3.37.0` |
| `IMAGE_TAG` | The default tag for the docker image | `3.12.1`  |

## Artifacts

When the job is successful, the documentation build result is available as artifact.

!!! warning
    It's also [exposed
    as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"}
    `OpenAPI Build` in merge requests.  Exposition of artifact in merge request
    currently works only if you keep `SWAGGER_OUTPUT` default value because of
    [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}.
    As soon as the issue will be fixed, exposed artifacts will be available
    with any output location.



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)
