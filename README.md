## Simple Server Failover
Sometimes it's very important to plan for the unexpected, actually, downtime for servers is something that is always expected. Whether it is a maintenance downtime, connectivity issue/loss or any other server issue that simply kills access to your website.

**Raison d'etre:**

There are many ways and tools out there that let you achieve the same thing and even more complex results.
I tried to make this configuration as easy as possible by utilizing DigitalOcean API and their Floating IP feature without a lot of moving parts. Any suggesstions/contributions that would even make this simpler are welcome.


**Using this failover configuration:**

1. You will have two servers running at the same time, each one checking the other's availability status.
2. When one server goes down, the other one will automatically take its place.
3. You won't have to deal with DNS or think about DNS propagation after servers switch to each other in case of failover.
4. The healthy server will detect failure of the live server in less than one minute. Which means that your downtime will be around a minute at most.

### Prerequisites

1. Create two DigitalOcean servers in the same data center.
2. Create a floating IP @ DigitalOcean (https://cloud.digitalocean.com/networking).
3. Point the floating IP to the primary server.
4. Grab the floating IP, primary server public IP & droplet ID, secondary server public IP & droplet ID.

### Steps

*The following needs to be executed on both servers.*

**1.** Make sure you have `python3` as well as `python3-requests` installed on both servers:
```sh
sudo apt-get install python3 python3-requests
```
**2.** Edit `floating-ip-droplet-id.py` and replace `DIGITAL_OCEAN_API_KEY_PLACEHOLDER` by your actual DigitalOcean API key, or replace `YOUR_ACTUAL_DO_API_KEY` in the following line then execute:
```sh
sed s/DIGITAL_OCEAN_API_KEY_PLACEHOLDER/YOUR_ACTUAL_DO_API_KEY/g floating-ip-droplet-id.py | tee floating-ip-droplet-id.py 
```
**3.** Move `floating-ip-droplet-id.py` to /usr/local/bin/floating-ip-droplet-id then make it executable: 
```sh
sudo mv floating-ip-droplet-id.py /usr/local/bin/floating-ip-droplet-id
sudo chmod +x /usr/local/bin/floating-ip-droplet-id
```
**4.** Edit `do-assign-floating-ip.py` and replace `DIGITAL_OCEAN_API_KEY_PLACEHOLDER` by your actual DigitalOcean API key, or replace `YOUR_ACTUAL_DO_API_KEY` in the following line then execute:
```sh
sed s/DIGITAL_OCEAN_API_KEY_PLACEHOLDER/YOUR_ACTUAL_DO_API_KEY/g do-assign-floating-ip.py | tee do-assign-floating-ip.py 
```
**5.** Move `do-assign-floating-ip.py` to /usr/local/bin/do-assign-floating-ip then make it executable:
```bash
sudo mv do-assign-floating-ip.py /usr/local/bin/do-assign-floating-ip
sudo chmod +x /usr/local/bin/do-assign-floating-ip
```

### Syncing both servers

- You can either deploy your code via git to both servers (can be easily done using Laravel Forge https://forge.laravel.com).
- You can set up file syncing between the two servers using rsync, both servers first need to be able to use a public/private key authentication to communicate with each other without a password.

### TODO
- Group variables in one place
- Add more instructions about each step
- Add examples for more than two servers
- Add methods for using CloudFlare to allow different data center failover
- Add tutorials and explanations for each prerequisite step
