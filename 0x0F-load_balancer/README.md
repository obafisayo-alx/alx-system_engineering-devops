# Project: Redundancy for Web Servers

## Background Context

You have been provided with 2 additional servers:

- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

The objective is to enhance the web stack to ensure redundancy for the web servers. This entails doubling the number of web servers to accommodate more traffic and enhance infrastructure reliability. Having redundant web servers ensures that if one server fails, there is still another one available to handle requests.

To achieve this, Bash scripts will be utilized to automate the configuration of brand new Ubuntu servers to meet the task requirements.

## Resources

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)
- [Debian/Ubuntu HAProxy packages](http://www.haproxy.org/download/2.0/doc/install.html#debian-ubuntu)

## Requirements

### General

- **Allowed editors:** vi, vim, emacs
- All files interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- Mandatory README.md file at the project root folder
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

### Servers

| Name           | Username | IP              | State   |
|----------------|----------|-----------------|---------|
| 469087-web-01  | ubuntu   | 34.232.70.111   | running |
| 469087-web-02  | ubuntu   | 54.209.252.118  | running |
| 469087-lb-01   | ubuntu   | 100.26.226.178  | running |

---
*This README was generated for the project as per the provided instructions.*