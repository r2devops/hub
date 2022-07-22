## Objective

Deploy a static website using GitLab Pages.  
This job can be used to deploy documentation, a static website or a Single Page Application.  

## How to use it

!!! note "Requirements"
    You have to use a job which build your website in a previous stage. *We recommend you to use a jobs available on the hub in `build`*. They build a static site of your application and publish it as artifact in `website_build/` folder .  
    📗 To generate documentation you could use [mkdocs](https://r2devops.io/_/r2devops-bot/mkdocs)  
    🕸️ To deploy a SPA, you could use [npm_build](https://r2devops.io/_/r2devops-bot/npm_build) or [yarn_build](https://r2devops.io/_/r2devops-bot/yarn_build). 
      
!!! info "How to deploy a SPA ?"
    In case, you want to deploy a SPA, you will only have one root file `index.html`, with your own rooting system. **Therefore, it's important that all requests are rewritten to this file.**  
    To do so create a `_redirects` file inside the root of your repository and set the variable `PAGES_REDIRECTION_FILE` to `_redirects`. Finally add this content inside the file :  
    `/* /index.html 200`   
    For more information, check the [documentation](https://docs.gitlab.com/ee/user/project/pages/redirects.html#rewrite-all-requests-to-a-root-indexhtml).

1. Copy the job URL located in the `Install` part of the right panel and add it inside the `include` list of your `.gitlab-ci.yml` file (see the [quick setup](/use-the-hub/#quick-setup)). You can specify [a fixed version](#changelog) instead of `latest`.
2. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](/use-the-hub/#jobs-customization)
3. Well done, your job is ready to work ! 😀


## Job details

* Job name: `pages`
* Docker image: [`ruby`](https://hub.docker.com/_/ruby){:target="_blank"}
* Stage: `deploy`
* When: only run on `master` branch

| Name | Description | Default |
| ---- | ----------- | ------- |
| `PAGES_BUILD_PATH` | Path to folder which contains the static website files to publish | `website_build/` |
| `PAGES_REDIRECTION_FILE` | Path to file which contains [redirection routes](https://docs.gitlab.com/ee/user/project/pages/redirects.html#create-redirects) for the website. | ` `



### Author
This resource is an **[official job](https://docs.r2devops.io/faq-labels/)** added in [**R2Devops repository**](https://gitlab.com/r2devops/hub) by [@thomasboni](https://gitlab.com/thomasboni)