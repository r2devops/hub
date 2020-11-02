# New Job

## Objectives

(Summarize concisely the objectives expected by this job)

(Identify clearly the benefits will help the community to contribute on your job)

## Use case

(Explain how the job could work)

## Artifacts & Return status

(List the artifacts expected by this job and the return status in these case)
- **When success:**
- **When failed:**

(Describe how artifacts will be integrated on platform)
(Relevant screenshots or logs can be provided - please use code blocks (```) to format console output,
logs, and code as it's very hard to read otherwise.)

## Possibles stages or label to this jobs

(Identify Stages and Labels available by checking [the documenation](https://hub.go2scale.io/jobs/))

# ❓ Help - (You can erase that part below before submitting) 🧽

## Example to add a Doxygen job

### Objectives

Provide a job to build automatically documenation using [the Doxygen syntax](https://www.doxygen.nl/index.html) for 10 langages.

Generate the documenation in [more than 10 output formats](https://www.doxygen.nl/manual/output.html) such as HTML, LaTeX, XML,...

#### List of supported langage

- C++
- C
- Objective-C
- C#
- PHP
- Java
- Python
- IDL (Corba, Microsoft, and UNO/OpenOffice flavors)
- Fortran
- VHDL

### Use case

The job will browse your source code and generate the documenation in the output format choosen.

Your source code must be completed with the Doxygen syntax before running this jobs.

- As a developper
- I want a job to build my documentation with Doxygen syntax in the support langage
- So that the documentation will be up-to-date with no effort


### Artifacts && Return status

(List the artifacts expected by this job)

**When success:** 
  - Generate a html folder with the documentation generated
  - The generated documentation artifact will be integrated in Gitlab Merge Request using `expose_as`

**When failed:** 
  - Generate nothing, the report of the execution will be available in the runner output console.
  - When it fails, the job must be marked as failed on the platform and error log must be available in job output

