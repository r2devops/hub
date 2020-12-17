# New Job
<!-- Title should respect this syntax [New job] - {jobname} -->
<!-- Sample of usage of this template ➡️  https://gitlab.com/r2devops/hub/-/issues/111 -->

## Objective
<!-- Summarize concisely the objective expected by this job -->
<!-- Identify clearly the benefits will help the community to contribute on your job -->

## Use cases

### Scenarios
<!-- Using the Gherkin syntax (see https://cucumber.io/docs/gherkin/reference/)
describe several scenarios of the job working. The scenario must include at
least 3 parts :

* Given: Steps used to describe the initial context of the system.
* When:  Steps used to describe an event, or an action.
* Then:  Steps used to describe an expected outcome, or result.

Example for Gitlab release creation job:

Scenario: With a `CHANGELOG.md` file
* Given there is a `CHANGELOG.md` file in repository
* When the job is run on a pipeline on default branch
* Then a new Gitlab release is created using:
    * `name`, `description`, `milestones`, `assets:links` from `CHANGELOG.md`
    * `tag_name` from `name`
    * `ref` from `$CI_COMMIT_SHA`
-->

### Parameters
<!-- Describe here the parameters of the job. Example for Gitlab release
creation job:

| Name | Mandatory to create release ? | Default | How to get it ? |
| ---- | ----------------------------- | ------- | --------------- |
| `name` | yes | if `CHANGELOG.md` exists: from this file. Else, use the current date and commit SHA | Parse `CHANGELOG.md`. Else, use `YYYY-MM-DD.$CI_COMMIT_SHORT_SHA` |
| `tag_name` | yes | same as `name` | get value set to `name` |
| `ref` | yes | current commit | use Gitlab variable `$CI_COMMIT_SHA` |
| `description` | no | get it from `CHANGELOG.md` if it exists | parse `CHANGELOG.md` |
| `milestones` | no | get it from `CHANGELOG.md` if it exists | parse `CHANGELOG.md` |
| `assets:links` | no | get it from `CHANGELOG.md` if it exists | parse `CHANGELOG.md` |
-->



## Artifacts & Return status
<!--
List the artifacts expected by this job and the return status in these cases
- **When success:**
- **When failed:**

Describe how artifacts will be integrated on platform
Relevant screenshots or logs can be provided - please use code blocks (```) to format console output,
logs, and code as it's very hard to read otherwise.
-->

## Possible stages or labels for this job
<!-- Identify Stages and Labels available by checking [the documentation](https://r2devops.io/jobs/) -->
