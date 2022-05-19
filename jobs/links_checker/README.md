## Objective

Using this job you will be able to detect most (see [here](#types-of-link-verified)) broken links in your **Markdown** or **HTML** files.

It uses the tool [`Lychee`](https://github.com/lycheeverse/lychee){:target="_blank"} in [Rust](https://rust-lang.org){:target="_blank"}
to test and find the links in your documents.
In its default state, this job will analyze your whole project for eligible files to verify.

!!! warning
    This job may generate a lot of errors about local broken links in your document if you are using **absolute paths** or **rewriting URLs**.
    See [Absolute paths and rewriting URLs](#absolute-paths-and-rewriting-urls)

## How to use it

1. Have `.md`, `.html` or `.htm` files in your project
1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `links_checker`
* Docker image:
[`lycheeverse/lychee:0.9`](https://hub.docker.com/r/lycheeverse/lychee){:target="_blank"}
* Default stage: `tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `LYCHEE_DIRECTORY` <img width=450/> | Path to the directory to be scanned | ` ` |
| `LYCHEE_FILES` | A list of files (separated with spaces) to scan. It can be used with `LYCHEE_DIRECTORY` | ` ` |
| `LYCHEE_EXCLUDE_LINKS` | A [regular expression](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"} to exclude a pattern of link | ` ` |
| `LYCHEE_EXCLUDE` | A [regular expression](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"} to exclude files or directory matching a pattern | ` ` |
| `LYCHEE_PRINT_OK` | Display in the console the output | `false` |
| `FAIL_ON_BROKEN` | Make your pipeline fails when a broken link is found | `false` |
| `ROOT_DIRECTORY` | Used for absolute paths, it defines the root of HTML projects | ` ` |
| `LYCHEE_OPTIONS` | Additional options (see [options](https://github.com/lycheeverse/lychee#commandline-parameters){:target="_blank"}) | ` ` |
| `ROOT_DIRECTORY` | Used for absolute paths, it defines the root of HTML projects | ` ` |
| `REPORT_OUTPUT` | Report file's name(see [artifacts](#artifacts)). Is not generated if empty (can increase jobs speed) | `junit-report.xml` |

!!! warning
    As this job is still in development, some behavior could be unexpected.
    For example, avoid using `LYCHEE_EXCLUDE` and `--include <link>` options together as include has preference over all excludes and `LYCHEE_EXCLUDE` uses a hand-written  `find` command. 


### Types of link verified

This tool will check for links in a specific context, and so in your project some link formats may not be checked. However,
here is (a non-exhaustive) list of what `Lychee` can identify:

**In HTML files (`.html`, `.htm`):**
```HTML
Can identify:

* <a href="https://www.google.com"></a>
* <a href="portfolio.html"></a>
* <a href="mailto:contact@google.com"></a>
* <img src="../images/logo.png"/>
* <img src="logo.png"/>
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
only want to check external links, by using `LYCHEE_EXCLUDE_LINKS: "^[^https?]"` (see [regex](https://en.wikipedia.org/wiki/Regular_expression){:target="_blank"})

### Filtering status code and authentication 

There are several method to authenticate into website with Lychee. As multiple methods are available, you need to choose your own and override the `LYCHEE_OPTIONS` variable to define it. Here are some case of authentication :
For basic authentication like username:password`, use option `--basic-auth`.
If you need to access an URL that require some Header token to authenticate, like Bearer, you could use this syntax : ` --headers 'Authorization: 'Bearer <token>'`
Last, you can avoid rate limiting on GitHub links by using this syntax : `--github-token <github-token>`.

If you are still issuing some 503 status code which requires authentication, you can ignore them by setting `LYCHEE_OPTIONS` to `-a 503`. 

### Artifacts

We use [Junit](https://junit.org/junit5/){:target="_blank"}'s XML report to display error report
directly in pipeline `Test` tab and in merge request widget.



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@Protocole](https://gitlab.com/Protocole). Was updated by [@GridexX](https://gitlab.com/GridexX) on May 2022 with a better tool.