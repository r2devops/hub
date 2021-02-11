## Objective

Creates an interactive version of an API documentation (see [demo](https://petstore.swagger.io/){:target="_blank"})
with [Swagger UI](https://swagger.io/tools/swagger-ui/){:target="_blank"}. It uses a [OpenAPI specifications](https://swagger.io/specification/){:target="_blank"}
(or [Swagger](https://swagger.io/docs/specification/2-0/basic-structure/){:target="_blank"}) file to be generated.

The version of SwaggerUI used is compatible with OpenAPI Specification 3.0 and 2.0 (fka Swagger).
This job let you the possibility to change SwaggerUI version (see [versions](https://github.com/swagger-api/swagger-ui#compatibility){:target="_blank"}) to match with older specifications versions.

## How to use it

1. Have a [compatible](#description) API specification file you can use in the job
2. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub/)). Example:

    ```yaml
    include:
      - remote: 'https://jobs.r2devops.io/openapi.yml'
    ```

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `openapi`
* Docker image: [`alpine:3.12.1`](https://hub.docker.com/_/alpine/){:target="_blank"}
* Default stage: `build`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `API_DEF_LOCATION` <img width=250/> | Path to your OpenAPI file in your repository <img width=400/> | `openapi.json` |
| `SWAGGER_OUTPUT` | Output directory path | `website_build/` |
| `SWAGGERUI_VERSION` | Version of SwaggerUI (see [versions](https://github.com/swagger-api/swagger-ui#compatibility){:target="_blank"}) | `v3.37.0` |

### Artifacts

Result of documentation build is [exposed
as](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as){:target="_blank"} `OpenAPI Build` in
merge requests.

!!! warning
    Exposition of artifact doesn't work currently because of [this issue from
    Gitlab](https://gitlab.com/gitlab-org/gitlab/-/issues/37129){:target="_blank"}. As soon as
    the issue will be fixed, exposed artifacts will be available in merge
    requests.
