## Definition of Done

📢 In order to ensure a safe :lock: hub, make sure to complete all the tasks related to the type of work you are doing before merging

*Your issue field isn't here ? Feel free to customize your merge request accordingly!*

### Field: Create or update a job

* [ ] Ensure that the job contain all required files in order to fit [the template](https://gitlab.com/r2devops/hub/-/tree/latest/tools/job_template/job_name)
* [ ] Ensure that the jobs is working
* [ ] Create a new change-log file (initial version must be `0.1.0`)
* [ ] Update the documentation (`README.md` file)
* [ ] Check if your job follows our [guidelines](https://r2devops.io/create-update-job/#guidelines-required) and [best practices](https://r2devops.io/create-update-job/#best-practices-optional)
* [ ] Ensure pipeline doesn't fail
* [ ] Update the dictionary if the job `spell_check` fails, and it's not a typo  

### Field: Update the documentation

* [ ] Check the documentation result is rendered properly in pipeline `MkDocs` artifact
* [ ] Check if your job follows our [guidelines](https://r2devops.io/create-update-job/#guidelines-required) and [best practices](https://r2devops.io/create-update-job/#best-practices-optional)
* [ ] Ensure pipeline doesn't fail
* [ ] Update the dictionary if the job `spell_check` fails, and it's not a typo  
* [ ] Fix the broken links if any is prompted by the `links_checker` job

### Field: Update one of the hub tools

* [ ] Check if your job follows our [guidelines](https://r2devops.io/create-update-job/#guidelines-required) and [best practices](https://r2devops.io/create-update-job/#best-practices-optional)
* [ ] Ensure the tool is working properly locally 
* [ ] Ensure the tool is working properly in the pipeline 
* [ ] If needed, update `Pipfile` (and `Pipfile.lock`) dedicated to the tool
* [ ] Ensure pipeline doesn't fail
* [ ] Ensure you respect the tool quality score 
    * If the tool is in python, try to run `pylint` and get a minimum score of `8.0`
    * If the tool is in javascript, try to run `eslint` and get no error

### Field: Update hub's pipeline 

* [ ] Check if it follows our [guidelines](https://r2devops.io/create-update-job/#guidelines-required) and [best practices](https://r2devops.io/create-update-job/#best-practices-optional)
* [ ] Check if the new pipeline is working properly in a fork

## When I'm done

You are already done :100: ? Well, now put in review one of the R2Devops **team member**, so we can review what you've done so far! :rocket: 

*If you are updating or adding a job, we would be grateful if you could comment in your merge request a direct link to a pipeline with the working job*
