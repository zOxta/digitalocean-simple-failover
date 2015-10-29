# digital ocean PRIMARY server failover script

echo "\nchecking SECONDARY server status"

# digital ocean floating ip
IP='xx.xx.xx.xx'

# digital ocean PRIMARY server droplet id
ID='xxxxxx'

# digital ocean SECONDARY server public ip
SECONDARY_SERVER_PUBLIC_IP='xx.xx.xx.xx'

# digital ocean SECONDARY server health check
SECONDARY_SERVER_STATUS=$(curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://$SECONDARY_SERVER_PUBLIC_IP)

HAS_FLOATING_IP=$(python3 /usr/local/bin/floating-ip-droplet-id)

# if i the floating ip is not pointing to me and the SECONDARY server is down then assign floating ip to me
if [ $HAS_FLOATING_IP != $ID ] && [ $SECONDARY_SERVER_STATUS = 000 ]; then

    echo "\nSECONDARY server is down and has the floating ip"

    n=0
    while [ $n -lt 10 ]
    do
        echo "\nswitching to PRIMARY server $ID"
        python3 /usr/local/bin/assign-ip $IP $ID && break
        n=$((n+1))
        sleep 3
    done
else
    echo "\nno switch necessary\n"
    echo $HAS_FLOATING_IP $SECONDARY_SERVER_STATUS $ID
fi