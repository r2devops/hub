## Objective

Gofmt formats Go programs. It uses tabs for indentation and blanks for alignment. Alignment assumes that an editor is using a fixed-width font.

⚠️ A golang code must be compliant with go fmt so when job catches something to update, it fails.

## How to use it

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
1. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
1. Well done, your job is ready to work ! 😀

## Job details

* Job name: `gofmt`
* Docker image:
[`golang:1.17-alpine3.14`](https://hub.docker.com/layers/golang/library/golang/1.17-alpine3.14/images/sha256-0bf16905b2757f1dcf6e78b1d14c223a38ade123c97bdd61a5cfcc4e77136040)
* Default stage: `static_tests`
* When: `always`

### Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `GOFMT_OPTIONS` <img width=100/> | List of options to pass to gofmt <img width=175/>| ` ` <img width=100/>|
| `PROJECT_ROOT` <img width=100/> | Path to the directory containing your Go project root| `.` |
| `GOFMT_PRINT_DIFF` <img width=100/> | Print diffs to standard output| `true` |
| `GOFMT_PRINT_FILENAME` <img width=100/> | Print filenames to standard output| `false` |



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@coconux](https://gitlab.com/coconux)