## Objective

This job allows you to build your 🐘 Gradle project using a script (`build` by default)
from your `build.gradle.kts` or `build.gradle` file.

## How to use it

1. Ensure that your project have
   [`build.gradle.kts`](https://docs.gradle.org/current/samples/sample_building_java_applications.html){:target="_blank"}
   file
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. Well done, your job is ready to work ! 😀

🔗 Here is an example of a complete pipeline using this step : [fun_with_gitlab-ci](https://gitlab.com/fun_with/fun-with-gitlab-ci/-/blob/master/.gitlab-ci.yml)


## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `IMAGE_TAG` | The default tag for the docker image | `jdk11`  |


## Example of build.gradle.kts file

Following example of `build.gradle.kts` file describes a very simple example of project configuration.
This can easily be generated with the `gradle init` command.

***For a Java project***

```kotlin
import org.gradle.api.JavaVersion.VERSION_11

plugins {
    java
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

```


## Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@yodamad](https://gitlab.com/yodamad)
