module.exports = [
    {
      name: "Job folder creation",
      templatePath: "tools/job_template/r2_jobname/",
      outputPath: "jobs/",
      fields: [
        {
          templateVariable: "r2_jobname",
          question: "What is the name of your job?"
        },
        {
          templateVariable: "r2_jobdescription",
          question: "Give a short description of your job"
        },
        {
          templateVariable: "r2_stage",
          question: "What is the default stage of your job?",
          choices: ["static_tests", "build", "dynamic_tests", "provision", "review", "release", "deploy", "others"]
        },
        {
          templateVariable: "r2_maintainer",
          question: "What is your Gitlab username?"
        },
        {
          templateVariable: "r2_license",
          question: "What license do you want to use?",
          choices: ["MIT", "Apache-2.0"]
        },
        {
          templateVariable: "r2_imagename",
          question: "What is the Docker image that you will use? (just the name)"
        },
        {
          templateVariable: "r2_imagetag",
          question: "What is the tag of this image?",
          errorMessage: "Must be a specific tag",
          isValid(val) {
            return val !== "latest";
          }
        },
        {
          templateVariable: "r2_icon",
          question: "Finally, paste an emoji that represents your job"
        }
      ]
    }
  ];