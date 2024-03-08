## Objective

This job allows you to run the unit tests of 🐘 Gradle project.

You can easily have a badge configure on your 🦊 Gitlab project with this regex `([0-9]{1,3}.[0-9]*).%.covered` configured in `settings/ci_cd` section. See gallery for example.

## How to use it

1. Ensure that your project have
   [`build.gradle.kts`](https://docs.gradle.org/current/samples/sample_building_java_applications.html){:target="_blank"}
   file
1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
1. Well done, your job is ready to work ! 😀

🔗 Here is an example of a complete pipeline using this step : [fun_with_gitlab-ci](https://gitlab.com/fun_with/fun-with-gitlab-ci/-/blob/master/.gitlab-ci.yml)


## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| JACOCO_CSV_LOCATION | Path to CSV file containing report | ${CI_PROJECT_DIR}/reports/jacoco/csv/jacoco.csv |
| JACOCO_HTML_LOCATION | Folder containing report as a HTML website | ${CI_PROJECT_DIR}/reports/jacoco/html |
| JACOCO_XML_LOCATION | Folder containing report as XML file | ${CI_PROJECT_DIR}/reports/jacoco/xml |
| `IMAGE_TAG` | The default tag for the docker image | `jdk11`  |

⚠️ These paths are defined within `build.gradle` file.

## Example of build.gradle.kts file

Following example of `build.gradle.kts` file describes a very simple example of project configuration.
This can easily be generated with the `gradle init` command.

***For a Java project***

```kotlin
import org.gradle.api.JavaVersion.VERSION_11

plugins {
    java
    // Analyze coverage
    jacoco
}

group = "io.r2devops"
version = "1.0.0-SNAPSHOT"
java.sourceCompatibility = VERSION_11
java.targetCompatibility = VERSION_11

repositories {
    jcenter()
    mavenCentral()
}

dependencies {
    // Use JUnit Jupiter API for testing.
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.6.2")

    // Use JUnit Jupiter Engine for testing.
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.6.2")
}

tasks.test {
    // Report is always generated after tests run
    finalizedBy(tasks.jacocoTestReport)
    // Use junit platform for unit tests
    useJUnitPlatform()
}

tasks.jacocoTestReport {
    // Tests are required to run before generating the report
    dependsOn(tasks.test)

    // Enable CSV for badge on project
    csv.isEnabled = true
    csv.destination = file("${buildDir}/reports/jacoco/csv/jacoco.csv")

    // Enable XML to convert to cobertura format for MR display
    xml.isEnabled = true
    xml.destination = file("${buildDir}/reports/jacoco/xml/jacoco.xml")

    // Enable HTML to publish on Pages
    html.destination = file("${buildDir}/reports/jacoco/html")
}

```

***For a Kotlin project***

```kotlin
import org.gradle.api.JavaVersion.VERSION_11

plugins {
    id("org.jetbrains.kotlin.jvm") version "1.4.21"
    // Analyze coverage
    jacoco
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

    // Use the Kotlin test library.
    testImplementation("org.jetbrains.kotlin:kotlin-test")

    // Use the Kotlin JUnit integration.
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit")
}

tasks.test {
    finalizedBy(tasks.jacocoTestReport) // report is always generated after tests run
}

tasks.jacocoTestReport {
    dependsOn(tasks.test) // tests are required to run before generating the report

    // Enable CSV for badge on project
    csv.isEnabled = true
    csv.destination = file("${buildDir}/reports/jacoco/csv/jacoco.csv")

    // Enable XML to convert to cobertura format for MR display
    xml.isEnabled = true
    xml.destination = file("${buildDir}/reports/jacoco/xml/jacoco.xml")

    // Enable HTML to publish on Pages
    html.destination = file("${buildDir}/reports/jacoco/html")
}

```

## Example to deploy HTML report to pages

```yaml
stages:
  - tests
  - deploy

include:
  - remote: 'https://api.r2devops.io/job/r/gitlab/r2devops/hub/gradle_test'

# Test deployment to Gitlab pages
pages:
  stage: deploy
  image: alpine:latest
  script:
    - mkdir public
    - mv $JACOCO_HTML_LOCATION public
  needs:
    - job: gradle_test
      artifacts: true
  cache: {}
  artifacts:
    paths:
      - public

```



## Author
This resource is an **[official job](https://docs.r2devops.io/get-started/faq/#use-a-template)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@yodamad](https://gitlab.com/yodamad)
