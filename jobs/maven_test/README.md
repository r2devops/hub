## Objective

Test your Java project using [Apache Maven](http://maven.apache.org/) JDK 11, JaCoCo and Surefire Maven plugins for code coverage and tests report directly in your merge requests.

## How to use it

1. Make sure your Java project is set up to use Maven. You can refer to the [Maven quick start guide](http://maven.apache.org/guides/getting-started/index.html)
2. Use the provided `pom.xml` in the example below to get you started. You are then free to customize your `pom.xml`
depending on your needs. You can also use this job along with the `maven_build` job on the R2DevOps hub for a completely
automated Java pipeline.
3. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
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

<properties>
  <junit.version>4.12</junit.version>
</properties>

<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>${junit.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <directory>${artifactsDirectory}</directory>
  <pluginManagement>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
      </plugin>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.6</version>
      </plugin>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.0.0-M5</version>
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
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>prepare-agent</id>
          <goals>
            <goal>prepare-agent</goal>
          </goals>
        </execution>
        <execution>
          <id>generate-code-coverage-report</id>
          <phase>test</phase>
          <goals>
            <goal>report</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
</project>
```

## Job details

* Job name: `maven_test`
* Docker image: [maven:3.8.4-jdk-11](https://hub.docker.com/_/maven)
* Default stage: `static_tests`
* When: `always`

### Variables
| Name | Description | Default |
| ---- | ------------| ------- |
| `ARTIFACTS_DIR` | Customize the path where the artifacts will be created | `${CI_PROJECT_DIR}/artifacts` |

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget. It's also available directly in the artifacts.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@alexlevy](https://gitlab.com/alexlevy)