## Objective

Build your Java project using [Apache Maven](http://maven.apache.org/) and JDK 11.

## How to use it

1. Make sure your Java project is set up to use Maven. You can refer to the [Maven quick start guide](http://maven.apache.org/guides/getting-started/index.html)
2. _(Recommended)_ Use the provided `pom.xml` in the example section below to get started. You are then free to customize your `pom.xml`
as you wish. For instance you can choose to use the [Spring Boot](https://spring.io/projects/spring-boot) framework that will
package your jar a different way and the job will still work and expose your shiny jars.
3. Add the job URL inside the `include` list of your `.gitlab-ci.yml` file  (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/maven_build.yml'`
    ```
4. If you need to customize the job (stage, variables, ...) check the [jobs-customization](/use-the-hub/#jobs-customization)
5. Grab a ☕ while the job is running !

## Example pom.xml
```xml
<project xmlns = "http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation = "http://maven.apache.org/POM/4.0.0 
  http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.myorg.myproject</groupId>
<artifactId>myartifact</artifactId>
<packaging>jar</packaging>
<version>1.0-SNAPSHOT</version>

<build>
  <directory>${artifactsDirectory}</directory> <!-- This is mandatory for the job to work -->
  <pluginManagement>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
      </plugin>
    </plugins>
  </pluginManagement>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <configuration>
        <source>11</source>
        <target>11</target>
      </configuration>
    </plugin>
  </plugins>
</build>
</project>
```

## Job details

* Job name: `maven_build`
* Docker image: [maven:3.6.3-jdk-11](https://hub.docker.com/_/maven)
* Default stage: `build`
* When: `always`

## Variables
| Name | Description | Default |
| ---- | ------------| ------- |
| `ARTIFACTS_DIR` | Customize the path where the artifacts will be created | `${CI_PROJECT_DIR}/artifacts` |