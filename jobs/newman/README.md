# 🚀 Newman

## Description

Launch a Postman collection of requests to test your API using [newman](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)

## How to use it

1. Add a Postman collection to your project and a globals file to use your variables
2. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    * Option 1: external service

    Add the IP address or the domain name of the service in your Postman collection
    or in your globals and use [Postman variables](https://learning.postman.com/docs/sending-requests/variables/)
    like this:
    ```
    https://{{my_domain}}
    ```
    

    *  Option 2: container instance

    To use this option, you must have access to a container image of your
    software. For example, if you are using our
    [docker_build](https://r2devops.io/jobs/build/docker_build/) job, just
    add the following configuration in your `.gitlab-ci.yml` file:

    !!! info
        * The `name` option must contain your image name and tag
        * The `alias` option permits to the job to reach your application using a name.
          This name must be the same that the one specified inside the collection or globals file
        * You may also run some other services like a database depending on your application needs

3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

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
| `NEWMAN_FAIL_ON_ERROR` | Fail job on a request/test error | `false` |
