## Objective

Launch a Postman collection of requests to test your API using [newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

## How to use it

1. Add a Postman collection to your project and a globals file to use your
   variables
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
3. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    - Option 1: external service

    Add the IP address or the domain name of the service in your Postman collection
    or in your globals and use [Postman variables](https://learning.postman.com/docs/sending-requests/variables/)
    like this in the request:
    ```
    https://{{my_domain}}
    ```
    You can also use that syntax anywhere in the request, the tests...

    - Option 2: container instance

    To use this option, you must have access to a container image of your
    software. For example, if you are using our
    [docker_build](https://r2devops.io/_/r2devops-bot/docker_build/) job, just
    add the following configuration in your `.gitlab-ci.yml` file:
    ```yaml
    newman:
      services:
      - name: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
        alias: app
    ```
    And specify `app` as your domain in your globals file

    !!! info
        * The `name` option must contain your image name and tag
        * The `alias` option permits to the job to reach your application using a name.
          This name must be the same that the one specified inside the collection or globals file
        * You may also run some other services like a database depending on your application needs

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NEWMAN_COLLECTION` <img width=100/> | Name of the Postman collection <img width=175/> | `postman_collection.json` <img width=100/> |
| `NEWMAN_GLOBALS_FILE` | Name of the Postman globals file for [variables](https://learning.postman.com/docs/sending-requests/variables/) | ` ` |
| `NEWMAN_ENVIRONMENT_FILE` | Name of the Postman environment file for variables | ` ` |
| `NEWMAN_ADDITIONAL_OPTIONS` | Other [options](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/) you may want to use with Newman | ` ` |
| `NEWMAN_FAIL_ON_ERROR` | Fail job on a request/test error | `true` |
| `NEWMAN_ITERATIONS_NUMBER` | Number of Newman iterations to run (see [documentation](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/#misc)) | `2` |
| `NEWMAN_VERSION` | Newman version | `5.2.2` |
| `NEWMAN_JUNIT_VERSION` | Newman JUnit reporter tool's version | `1.1.1` |
| `IMAGE_TAG` | The default tag for the docker image | `18-buster`  |

If you want to use some secret variables for your collection, and want to hide them from the `collection.json` file, you can specify them in a File variable called `NEWMAN_VARIABLE_FILE` inside you're `CI/CD Variables` in GitLab (Settings > CI/CD > Variables). Then add the following script for the job :

```yml

before_script:
  - apk update && apk add gettext
  - source $NEWMAN_VARIABLE_FILE
  - export $(cut -d= -f1 $NEWMAN_VARIABLE_FILE)
  - cp ${NEWMAN_COLLECTION} ${NEWMAN_COLLECTION}.back
  - envsubst < ${NEWMAN_COLLECTION}.back > ${NEWMAN_COLLECTION}
```

This method was inspired by this [website](https://carolinafernandez.github.io/devops/2020/05/12/Environment-variable-substitution-in-Linux).

## Artifact

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to
display error report directly in pipeline `Test` tab and in merge request
widget.



## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@FulcrandG](https://gitlab.com/FulcrandG)
