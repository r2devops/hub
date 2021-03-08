---
title: R2bulary | DevOps dictionary   
description: Find here the useful vocabulary linked to R2Devops’ hub. All the technical terms are explained in simple and clear words!
---

# R2bulary

![r2bulary](images/r2bulary.png){: .center .small_r2bulary }


## R2Devops platform

___
### Hub


___
### Job configuration

This is the configuration settings of the job.

___
### Job ready to use

Job is ready to use when you just have to include it into your project in order to Contributing.
Even job is ready to use, it's always customizable for your specific usage.

___
### Mono repo
All job are manage in the same repository.
In comparison to multi repository where each job has his own repository and his own git project url.

---

## DevOps

___
### Pipeline

Set of jobs launched in the same sequence. Pipeline can be run manually, after a commit or a merge into a branch.
We consider the pipeline as succeeded if all jobs in the pipeline success.

___
### Job

**A job is a script hosted in R2Devops Hub that can be included in CI/CD pipeline to do a unitary work.**

- 🆕 The job must be considered like a "disposable treatment" and not like something persistent.
- 🖇️The job is included in a stage in a pipeline. 1 job belongs to 1 stage (and 1 stage may contain several jobs 1:N)
- 🔫 Job is triggered by an action (either a merge on branch, or a manual triggering, or a previous job success).
- 🎁 Job may produce an artifact.
- 📄 Job always produces logs.
- ✋If a job failed, it can stop the pipeline (block the run of next stages or in case of [DAG](https://docs.gitlab.com/ee/ci/directed_acyclic_graph/) the next jobs of the graph).
- ⚠️ If a job failed, it can just throw a non-blocking warning.
- 📝 Once the pipeline is finished, jobs inside the pipeline are considered as finished too. The results (logs, artifacts, output) as for them are persistent.
- ⚙️ The Job can be customized by setting up the variables.
- 🧬A job instance in a pipeline is unique but a "job definition" can be implemented multiple time in a pipeline as multiple jobs instances.

___
### CI

Continuous integration is a coding philosophy and set of practices that drive development teams to implement small changes and check in code to version control repositories frequently.
This will ensure that your application meets your criteria of quality, security, performance, after each modification of your code.
___
### CD

Continuous delivery starts where continuous integration ends. CD philosophy is to automate the delivery of applications to the selected infrastructure environments.
___
### Stage

--8<-- "includes/abbreviations.md"
