# Project Title

This project focuses on configuring the web-01 server according to specific requirements and automating tasks using Bash scripts. Some tasks will be graded based on two aspects:

1. **Configuration of web-01 server**: Ensuring the server is configured as per requirements.
2. **Bash script automation**: Creating Bash scripts that automatically perform commands to configure an Ubuntu machine without any human intervention.

## Example

For instance, if the task involves creating a file `/tmp/test` containing the string "hello world" and modifying the configuration of Nginx to listen on port 8080 instead of 80, manual intervention might involve using a text editor like emacs on the server. However, the answer file would contain a Bash script like:

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

As seen in the example, the task is automated using a Bash script, eliminating the need for manual intervention.

## Importance of Automation

Automating tasks is crucial for efficiency, especially in scenarios with numerous servers to manage. By automating repetitive tasks, one can focus on more impactful and interesting work. 

## Testing

To test your Bash script, you can replicate the checker environment by:

1. Starting a Ubuntu 16.04 sandbox.
2. Running your script on it.
3. Observing how it behaves.

## Resources

This project provides resources such as readings and references on various topics related to web servers, DNS, HTTP requests, and more.

## Learning Objectives

Upon completion of this project, learners are expected to:

- Understand the main role of a web server.
- Comprehend the concept of child processes in the context of web servers.
- Identify the main HTTP requests.
- Gain knowledge about DNS, its role, and different DNS record types.

## Requirements

- **Editors**: Allowed editors include vi, vim, and emacs.
- **Environment**: All files will be interpreted on Ubuntu 16.04 LTS.
- **File Formatting**: All files should end with a new line.
- **README.md**: A README.md file at the root of the project folder is mandatory.
- **Executable Scripts**: All Bash script files must be executable.
- **Shellcheck**: Bash scripts must pass Shellcheck (version 0.3.7) without any error.
- **Shebang**: The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- **Comments**: The second line of all Bash scripts should be a comment explaining the script's purpose.
- **Systemctl**: Use of systemctl for restarting a process is not permitted.

## Quiz Questions

- Completed the quiz successfully? Keep going!

## Servers

- **Web Server**: 469087-web-01
  - **Username**: ubuntu
  - **IP Address**: 34.232.70.111
  - **State**: Running