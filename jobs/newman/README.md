## Objective

Launch a Postman collection of requests to test your API using [newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

## How to use it

1. Add a Postman collection to your project and a globals file to use your
   variables
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)):
   ```yaml
   include:
        - remote: 'https://jobs.r2devops.io/newman.yml'
   ```
3. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    * Option 1: external service

    Add the IP address or the domain name of the service in your Postman collection
    or in your globals and use [Postman variables](https://learning.postman.com/docs/sending-requests/variables/)
    like this in the request:
    ```
    https://{{my_domain}}
    ```
    You can also use that syntax anywhere in the request, the tests...

    *  Option 2: container instance

    To use this option, you must have access to a container image of your
    software. For example, if you are using our
    [docker_build](https://r2devops.io/jobs/build/docker_build/) job, just
    add the following configuration in your `.gitlab-ci.yml` file:
    ```
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

## Job details

* Job name: `newman`
* Docker image:
[`node:15.0.4`](https://hub.docker.com/r/_/node)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NEWMAN_COLLECTION` <img width=100/> | Name of the Postman collection <img width=175/> | `postman_collection.json` <img width=100/> |
| `NEWMAN_GLOBALS_FILE` | Name of the Postman globals file for [variables](https://learning.postman.com/docs/sending-requests/variables/) | ` ` |
| `NEWMAN_ADDITIONAL_OPTIONS` | Other [options](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/) you may want to use with Newman | ` ` |
| `NEWMAN_FAIL_ON_ERROR` | Fail job on a request/test error | `true` |
| `NEWMAN_ITERATIONS_NUMBER` | Number of Newman iterations to run (see [documentation](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/#misc)) | `2` |
| `NEWMAN_VERSION` | Newman version | `5.2.2` |
| `NEWMAN_JUNIT_VERSION` | Newman JUnit reporter tool's version | `1.1.1` |
### Artifact

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to
display error report directly in pipeline `Test` tab and in merge request
widget.
