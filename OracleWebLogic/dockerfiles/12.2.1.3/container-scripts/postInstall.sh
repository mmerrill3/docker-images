#!/bin/bash

OUTPUT=0
while [ "$OUTPUT" -ne 200 ]
do
echo "Service is not ready yet for more configuration"
sleep 10
OUTPUT="$(curl -s -I -X GET http://localhost:7001/weblogic/ready 2> /dev/null|head -n 1|cut -d$' ' -f2)"
if [ -z "$OUTPUT" ]; then
  OUTPUT=0
fi
done

echo "creating monitor user"
cd /u01/oracle/user_projects/domains/uber
mv /u01/oracle/create-monitor.py .
wlst.sh -skipWLSModuleScanning create-monitor.py
