## Objective

This job allows you to check your code with SonarQube plugin in a 🐘 Gradle project.

## How to use it

1. Ensure that your project have
   [`build.gradle.kts`](https://docs.gradle.org/current/samples/sample_building_java_applications.html){:target="_blank"}
   file
1. Configure the [SonarQube plugin](https://plugins.gradle.org/plugin/org.sonarqube){:target="_blank"} in your `build.gradle` file
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| SONAR_URL | URL of Sonar instance  | sonarcloud.io |
| SONAR_TOKEN | API token from your Sonar account to be able to publish report | |
| SONAR_ORG | Organization to which project belongs  | |
| SONAR_PROJECT | Project name in Sonar instance | |
| COVERAGE_PLUGIN | Plugin to use for code coverage analysis | jacoco |
| JSON_MODE | Format to publish report to integrated with Gitlab MR for instance | CODECLIMATE |
| `IMAGE_TAG` | The default tag for the docker image | `jdk11`  |

## Example of build.gradle.kts file

Following example of `build.gradle.kts` file describes a very simple example of project configuration.
This can easily be generated with the `gradle init` command.

***For a Java project***

```kotlin
import org.gradle.api.JavaVersion.VERSION_11

plugins {
    java
    // Quality control
    id("org.sonarqube") version "3.1.1"
}

group = "io.r2devops"
version = "1.0.0-SNAPSHOT"
java.sourceCompatibility = VERSION_11
java.targetCompatibility = VERSION_11

repositories {
    jcenter()
    mavenCentral()
}
```

***For a Kotlin project***

```kotlin
import org.gradle.api.JavaVersion.VERSION_11

plugins {
    id("org.jetbrains.kotlin.jvm") version "1.4.21"
    // Quality control
    id("org.sonarqube") version "3.1.1"
}

group = "io.r2devops"
version = "1.0.0-SNAPSHOT"
java.sourceCompatibility = VERSION_11
java.targetCompatibility = VERSION_11
kotlin.target { VERSION_11 }

repositories {
    jcenter()
    mavenCentral()
}

dependencies {
    // Align versions of all Kotlin components
    implementation(platform("org.jetbrains.kotlin:kotlin-bom"))

    // Use the Kotlin JDK 8 standard library.
    implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
}

```



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@yodamad](https://gitlab.com/yodamad)
