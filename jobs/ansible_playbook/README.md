## Objective

This job will run an [`ansible-playbook`](https://docs.ansible.com/ansible/latest/user_guide/playbooks.html) command to automate deployments. You can install multiple roles from a `requirements.yml` file, see the [documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## How to use it

1. Copy/paste job URL in `include` list of your `.gitlab-ci.yml` (see the **quick use**). You can specify [a fixed version](https://docs.r2devops.io/get-started/use-templates/#versioning) instead of `latest`.
2. If you need to customize the job (stage, variables, ...) 👉 check the [jobs
   customization](https://docs.r2devops.io/get-started/use-templates/#job-templates-customization)
3. Well done, your job is ready to work ! 😀

## Variables

| Name | Description | Default |
| ---- | ----------- | ------- |
| `ANSIBLE_WORKSPACE` <img width=100/> | The path where is located your ansible project <img width=175/> | `.` <img width=100/> |
| `ANSIBLE_INVENTORY_FILE` | The inventory file where are described roles and groups. This variable should be specified in `GitLab > CI/CD Settings` as file.  | ` ` |
| `SSH_PRIVATE_KEY_FILE` | ⚠️ Mandatory variable. The name of your private SSH key. This variable should be specified in `GitLab > CI/CD Settings` as file. | ` ` |
| `ADDITIONAL_OPTIONS` | Other [options](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html#common-options) you may want to use | ` ` |
| `IMAGE_TAG` | The default tag for the docker image | `3.15.1` |