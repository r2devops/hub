## Objective

Using this job you will be able to detect most (see [here](#types-of-link-verified)) broken links in your **Markdown** or **HTML** files.

It uses the tool [`Liche`](https://github.com/raviqqe/liche){:target="_blank"} in [Go](https://golang.org/){:target="_blank"}
to test and find the links in your documents.
In its default state, this job will analyze your whole project for eligible files to verify.

!!! warning
    This job may generate a lot of errors about local broken links in your document if you are using **absolute paths** or **rewriting URLs**.
    See [Absolute paths and rewriting URLs](#absolute-paths-and-rewriting-urls)

## How to use it

1. Have `.md`, `.html` or `.htm` files in your project
1. Add this job URL inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
    ```yaml
      - remote: 'https://jobs.r2devops.io/latest/links_checker.yml'
    ```
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `links_checker`
* Docker image:
[`peterevans/liche:1.1.1`](https://hub.docker.com/r/peterevans/liche){:target="_blank"}
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `LICHE_DIRECTORY` <img width=450/> | Path to the directory to be scanned | ` ` |
| `LICHE_FILES` | A list of files (separated with spaces) to scan. It can be used with `LICHE_DIRECTORY` | ` ` |
| `LICHE_EXCLUDE` | A [regular expression](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"} to exclude a pattern of link | ` ` |
| `LICHE_PRINT_OK` | In addition to broken links, it will add not-broken links in the report (see [artifacts](#artifacts)) | `false` |
| `LICHE_RECURSIVE` | When `LICHE_DIRECTORY` is filled it will search for files recursively  | `true` |
| `FAIL_ON_BROKEN` | Make your pipeline fails when a broken link is found | `false` |
| `ROOT_DIRECTORY` | Used for absolute paths, it defines the root of HTML projects | ` ` |
| `LICHE_OPTIONS` | Additional options (see [options](https://github.com/raviqqe/liche){:target="_blank"}) | ` ` |
| `REPORT_OUTPUT` | Report file's name | `junit-report.xml` |

### Types of link verified

This tool will check for links in a specific context, and so in your project some link formats may not be checked. However,
here is (a non-exhaustive) list of what `Liche` can or can't identify:

**In HTML files (`.html`, `.htm`):**
```HTML
Can identify:

* <a href="https://www.google.com"></a>
* <a href="portfolio.html"></a>
* <a href="mailto:contact@google.com"></a>
* <img src="../images/logo.png"/>
* <img src="logo.png"/>

Can't identify:

* <div onClick="redirect('https://www.google.com')"></div>
* <script type="text/javascript">
      window.location.href = "https://www.google.com"
  </script>
...
```

**In Markdown files (`.md`):**
```md

Can identify:

* [Gitlab](https://gitlab.com)
* [R2DevOps](https://r2devops.io){:target="_blank"}
* # New post [posts](https://pastebin.com)
* # My title link : https://www.google.com
* **See here a search engine: https://www.google.com**
```

### Absolute paths and rewriting urls

If you are using absolute paths in your HTML documents, be sure to fill the variable `ROOT_DIRECTORY`. If you don't, by default, the variable will be filled with the same path as `LICHE_DIRECTORY`.

If you use URL rewriting in your static website, using this job, most of the internal links will be considered as broken. To avoid that, you can define that you
only want to check external links, by using `LICHE_EXCLUDE: "^[^http]"` (see [regex](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"})

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole)