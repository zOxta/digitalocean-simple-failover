# prerequisites

1. Create two DigitalOcean servers in the same data center.
2. Create a floating IP @ DigitalOcean (you can find that in the 'Networking' tab).
3. Point the floating IP to the primary server.

# steps

1. Make sure you python3 is installed, as well as python3-requests `apt-get install python3 python3-requests`

2. Edit `floating-ip-droplet-id.py` and replace `YOU_DIGITAL_OCEAN_API_KEY` by your actual DigitalOcean API key.

3. Move `floating-ip-droplet-id.py` to /usr/local/bin/floating-ip-droplet-id then make it executable `chmod +x /usr/local/bin/floating-ip-droplet-id`

4. Edit `do-assign-floating-ip.py` and replace `YOU_DIGITAL_OCEAN_API_KEY` by your actual DigitalOcean API key.

5. Move `do-assign-floating-ip.py` to /usr/local/bin/do-assign-floating-ip then make it executable `chmod +x /usr/local/bin/do-assign-floating-ip`

# syncing both servers

- You can either deploy your code via git to both servers (can be easily done using Laravel Forge).
- You can setup file syncing between the two servers using rsync, both servers first need to be able to use a public/private key authentication to communicate with each other.