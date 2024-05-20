# 0x13-Firewall
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.[1][2] A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the Internet.

### More Info

Telnet is a powerful tool for checking if sockets are open, particularly useful in debugging scenarios where two pieces of software need to communicate over sockets. For example, to verify if port 22 is open on a server named web-02, you can use the following command:

```
telnet web-02.holberton.online 22
```

If the connection is successful, you will see a message indicating that you are connected to the server. Otherwise, you may see an error message indicating a failed connection attempt.

Keep in mind that the school network may filter outgoing connections using a network-based firewall, which could limit your ability to interact with certain ports on servers outside the school network. To test your work on a server named web-01, it's recommended to perform the test from outside the school network, such as from your web-02 server. By SSHing into your web-02 server, the traffic will originate from web-02, bypassing the school's network firewall.

**Warning:** Containers on demand cannot be used for this project due to Docker container limitations.

When working with firewall rules, exercise caution to avoid unintended consequences. For instance, if you deny port 22/TCP and log out of your server, you may lose SSH access, rendering the server inaccessible. Always ensure that necessary ports are unblocked before logging out of your server.

### Quiz Questions

You've completed the quiz successfully! Keep going!

### Your Servers

| Name            | Username | IP             | State   |
|-----------------|----------|----------------|---------|
| 469087-web-01   | ubuntu   | 35.153.98.10   | running |
| 469087-web-02   | ubuntu   | 35.153.79.136  | running |
| 469087-lb-01    | ubuntu   | 100.26.170.70  | running |

### Tasks

#### 0. Block All Incoming Traffic But

Configure the ufw firewall on web-01 to block all incoming traffic except for specific TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP). Share the ufw commands used in your answer file.

#### 1. Port Forwarding

Configure the firewall on web-01 to redirect port 8080/TCP to port 80/TCP. Provide a copy of the ufw configuration file modified to achieve this. 

**Note:** Verify the port forwarding using `netstat` and `curl` commands as shown in the task description.

For more detailed instructions and examples, refer to the specific task files in the GitHub repository: [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)

Directory: 0x13-firewall
File: 0-block_all_incoming_traffic_but, 100-port_forwarding
