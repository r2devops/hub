## Objective

This job will search for security issues in your dependencies, using the tool [Dependency-Check](https://github.com/jeremylong/DependencyCheck){:target="_blank"} powered by [OWASP](https://owasp.org/){:target="_blank"}.
It will be able to scan multiple sources of files, also file from package managers.

The complete list is available [here](https://jeremylong.github.io/DependencyCheck/analyzers/index.html){:target="_blank"}.

## How to use it

1. Ensure that your package manager and/or files are handled in [File Type Analyzers](#file-type-analyzers)
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/owasp_dependency_check.yml'
    ```
3. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
4. Well done, your job is ready to work ! 😀

## Job details

* Job name: `owasp_dependency_check`
* Docker image:
[`owasp/dependency-check:6.1.1`](https://hub.docker.com/r/owasp/dependency-check){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### File Type Analyzers

OWASP dependency-check has several file type analyzers that can detect security issues in your project.

| Analyzer | File Types Scanned |
| - | - |
| Archive | Zip archive format, Tar archive, Gzip archive, Bzip2 archive |
| Assembly | .NET Assemblies (*.exe, *.dll) |
| CMake | CMake project files (CMakeLists.txt) & scripts (*.cmake) |
| Jar | Java archive files (*.jar), Web application archive (*.war)
| RetireJS | Javascript files
| Node.js | NPM packages file (package.json)
| Node Audit | Uses `npm audit` API
| Nugetconf | Nuget `packages.config` file
| Nuspec | Nuget package specification file (*.nuspec)
| OpenSSL | OpenSSL Version Source Header File (opensslv.h)
| OSS Index | Uses the [OSS Index](https://ossindex.sonatype.org/){:target="_blank"} APIs to report security issues not found in the NVD (needs an internet connection).
| Ruby bundler-audit | Ruby `Gemfile.lock` files

!!! info
    OWASP Dependency-Check has some experimental analyzers that can be enabled by setting `true` to the variable `DEPCHECK_EXPERIMENTALS`. Be aware that these analyzers can still have some false positive alerts.

    To know the list of experimental analyzers click [here](https://jeremylong.github.io/DependencyCheck/analyzers/index.html){:target="_blank"}.

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `DEPCHECK_CVSS_SCORE_FAIL` <img width=100/> | Minimum CVSS Score for a vulnerability to make the job fails [See documentation](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System){:target="_blank"})<img width=175/>| `11` <img width=100/>|
| `DEPCHECK_JUNIT_CVSS_FAIL` | Minimum CVSS Score to be shown as vulnerability in the report | `0` |
| `DEPCHECK_OPTIONS` | User customizable options | ` ` |
| `DEPCHECK_EXPERIMENTALS` | Uses experimental analyzers | `false` |
| `DOTNET_DLL_ANALYZE` | Enable the analyzer for *.DLL and *.exe files | `false` |
| `DOTNET_VERSION` | If `DOTNET_DLL_ANALYZE` is enabled, sets the version of .NET Core (It uses script in [.NET Build](https://r2devops.io/jobs/build/dotnet_build/#variables)) | `3.1` |
| `DEPCHECK_NO_UPDATE` | Force `OWASP_dependency_check` to not update its local vulnerabilities database | `false` |
| `PROJECT_ROOT` | Root of the project to scan in your repository | `/` |

!!! warning
    The variable `DEPCHECK_CVSS_SCORE_FAIL` is set to 11 (CVSS Score goes from 0 to 10, see more [here](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System){:target="_blank"}). By default, the job will never fail because of a vulnerability. So it is recommended to customize this variable.

    Also, it is recommended to leave `DEPCHECK_JUNIT_CVSS_FAIL` to `0` to always show the security issues found.

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.

You will be able to directly see all the dependencies analyzed and, when there is security issue the Common Vulnerabilities and Exposures [CVE](https://cve.mitre.org/){:target="_blank"} referenced.

<!--
    `OWASP Dependency-Check` will analyze itself to see if there are any vulnerabilities, so the report will contain the dependencies linked to the tool used.
-->
