# This is a readme file for this folder
commands to take note of:
- Copying your Public SSH Key to a Server Without SSH-Copy-ID:
cat ~/.ssh/id_rsa.pub | ssh username@remote_host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

- Copying your Public SSH Key to a Server Manually:
echo public_key_string >> ~/.ssh/authorized_keys

## To go to the Digital Ocean documentation on setting up ssh
<button>
    <a href="https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys">
    click here
    </a>
</button>

## for youtube tutorial,
<button>
    <a href="https://www.youtube.com/watch?v=hQWRp-FdTpc">
    click here
    </a>
</button>
