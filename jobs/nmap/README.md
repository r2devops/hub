## Objective

[Nmap](https://nmap.org) is a tool designed to discover networks, map them, and
information that they could offer by being reachable on the internet. Its
powerful [scripting engine](https://nmap.org/book/nse.html) is very
flexible to retrieve this information.

This `nmap` job allows you to scan automatically your deployed server or the
new version you want to deploy. It is able to list every ports opened and check
if one of them should not be.

## How to use it

1. Add the corresponding URL to your `.gitlab-ci.yml` file (see [Getting
   started](/use-the-hub)). Example:
   ```yaml
   include:
     - remote: 'https://jobs.r2devops.io/nmap.yml'
   ```
2. Choose a target

    !!! note
        This job can be run on external services or by running a container
        instance of your software. **You need to choose between two following
        options**.

    * Option 1: external service

    Add the IP address or the domain name of the service in `NMAP_TARGET`
    (see [jobs customization](http://localhost:8000/use-the-hub/#jobs-customization))

    *  Option 2: container instance

    Add the target container instance as a service (see
    [Container instance as Service](/use-the-hub/#container-instance-as-service))
    and set `NMAP_TARGET` as the name of your container.

4. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
5. Well done, your job is ready to work ! 😀

## Job details

* Job name: `nmap`
* Docker image:
[`instrumentisto/nmap`](https://hub.docker.com/r/instrumentisto/nmaps)
* Default stage: `dynamic_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `NMAP_TARGET` <img width=100/> | The target server, its IP or domain name <img width=175/>| `app` <img width=100/>|
| `NMAP_SCRIPTS` | Comma separated list of lua [scripts](https://nmap.org/book/nse.html) to run | ` ` |
| `NMAP_OPTIONS` | Additional options you may want for the scan (`man nmap`) | ` ` |
| `NMAP_OUTPUT` | Name for the XML output file for nmap | `nmap-report.xml` |
| `HTML_OUTPUT` | Name for the html file for the Merge Request Widget for this job | `nmap-report.html` |
