### Project: 0x14. MySQL

#### Overview
This project focuses on MySQL database administration, setup, and management. You will learn about database replication, backup strategies, and various aspects of MySQL configuration.

#### Concepts
For this project, you'll delve into the following concepts:
- Fresh Reset and Install MySQL 5.7
- Database administration
- Web stack debugging

#### Resources
To get started, make sure to read or watch the following resources:
- What is a primary-replica cluster
- MySQL primary replica setup
- Building a robust database backup strategy

#### Learning Objectives
By the end of this project, you should be able to:
- Explain the main role of a database
- Describe what a database replica is and its purpose
- Understand why database backups need to be stored in different physical locations
- Recognize the operation needed to regularly test and ensure the effectiveness of a database backup strategy

#### Copyright - Plagiarism
Remember, this project requires you to come up with solutions yourself. Copying and pasting someone else’s work is strictly prohibited and will result in removal from the program. Avoid publishing any content related to this project.

#### Requirements
Here are some general guidelines and requirements for this project:
- Use editors like vi, vim, or emacs
- Interpret all your files on Ubuntu 16.04 LTS
- End all files with a new line
- Include a README.md file at the root of the project folder
- Make all your Bash script files executable
- Ensure your Bash scripts pass Shellcheck without any errors
- Start all your Bash scripts with `#!/usr/bin/env bash`
- Document the purpose of each Bash script with a comment on the second line
- Ensure that UFW allows connections on port 3306 (default MySQL port) for replication to work properly

#### Your Servers
Here are the servers you'll be working with for this project:

| Name         | Username | IP              | State   |
|--------------|----------|-----------------|---------|
| 469087-web-01| ubuntu   | 35.153.98.10    | running |
| 469087-web-02| ubuntu   | 35.153.79.136   | running |
| 469087-lb-01 | ubuntu   | 100.26.170.70   | running |

#### Tasks
Here's an overview of the tasks you'll be tackling in this project:

1. **Install MySQL**: Get MySQL installed on both web-01 and web-02 servers.
2. **Let us in!**: Create a MySQL user on both servers to allow access for verification.
3. **If only you could see what I've seen with your eyes**: Set up a database with at least one table and one row in your primary MySQL server.
4. **Quite an experience to live in fear, isn't it?**: Create a new user for the replica server and set up replication between web-01 and web-02.
5. **MySQL backup**: Write a Bash script to generate a MySQL dump and create a compressed archive out of it.

### Project Deadline
- Start Date: May 14, 2024 6:00 AM
- End Date: May 15, 2024 6:00 AM
- Checker Release: May 14, 2024 12:00 PM
- Auto review will be launched at the deadline.

Keep these dates in mind as you work through the tasks and ensure all requirements are met within the specified timeframe. Good luck with your MySQL project!