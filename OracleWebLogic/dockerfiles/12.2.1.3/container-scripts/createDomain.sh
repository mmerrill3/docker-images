#!/bin/bash

ADD_DOMAIN=1
if [ ! -f ${DOMAIN_HOME}/servers/AdminServer/logs/AdminServer.log ]; then
    ADD_DOMAIN=0
fi

# Create Domain only if 1st execution
if [ $ADD_DOMAIN -eq 0 ]; then

if [ -z $ADMIN_PASSWORD ]; then
   # Auto generate Oracle WebLogic Server admin password
   while true; do
     s=$(cat /dev/urandom | tr -dc "A-Za-z0-9" | fold -w 8 | head -n 1)
     if [[ ${#s} -ge 8 && "$s" == *[A-Z]* && "$s" == *[a-z]* && "$s" == *[0-9]*  ]]; then
         break
     else
         echo "Password does not Match the criteria, re-generating..."
     fi
   done
else
   s=${ADMIN_PASSWORD}
fi 
sed -i -e "s|ADMIN_PASSWORD|$s|g" /u01/oracle/create-wls-domain.py

# Create an empty domain
wlst.sh -skipWLSModuleScanning /u01/oracle/create-wls-domain.py
mkdir -p /u01/oracle/user_projects/domains/$DOMAIN_NAME/servers/AdminServer/security/
mkdir -p /u01/oracle/user_projects/domains/$DOMAIN_NAME/properties
echo "username=${ADMIN_USERNAME}" > /u01/oracle/user_projects/domains/$DOMAIN_NAME/servers/AdminServer/security/boot.properties 
echo "password=$s" >> /u01/oracle/user_projects/domains/$DOMAIN_NAME/servers/AdminServer/security/boot.properties 
ln -s /u01/oracle/wlserver/server/lib/wllog4j.jar /u01/oracle/user_projects/domains/$DOMAIN_NAME/lib/wllog4j.jar
ln -s /u01/oracle/oracle_common/modules/fmwplatform/common/lcmagent/jetty-runner.jar /u01/oracle/user_projects/domains/$DOMAIN_NAME/lib/jetty-runner.jar
curl -s http://central.maven.org/maven2/log4j/log4j/1.2.12/log4j-1.2.12.jar > /u01/oracle/user_projects/domains/$DOMAIN_NAME/lib/log4j-1.2.12.jar
curl -s http://central.maven.org/maven2/velocity/velocity/1.4/velocity-1.4.jar > /u01/oracle/user_projects/domains/$DOMAIN_NAME/lib/velocity-1.4.jar
curl -s http://central.maven.org/maven2/com/jamonapi/jamon/2.4/jamon-2.4.jar > /u01/oracle/user_projects/domains/$DOMAIN_NAME/lib/jamon-2.4.jar
fi


