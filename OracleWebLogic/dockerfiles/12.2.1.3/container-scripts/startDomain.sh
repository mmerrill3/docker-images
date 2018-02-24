#!/bin/bash
function _term() {
   echo "Stopping container."
   echo "SIGTERM received, shutting down the server!"
   ${DOMAIN_HOME}/bin/stopWebLogic.sh
}

########### SIGKILL handler ############
function _kill() {
   echo "SIGKILL received, shutting down the server!"
   kill -9 $childPID
}

# Set SIGTERM handler
trap _term SIGTERM

# Set SIGKILL handler
trap _kill SIGKILL


# Create datasources, and anything else that is defined at startup (JMS maybe?)
wlst.sh -skipWLSModuleScanning /u01/oracle/create-wls-datasources.py

${DOMAIN_HOME}/bin/setDomainEnv.sh

# Start WLS Server in development mode, i.e. autoDeploy apps
${DOMAIN_HOME}/bin/startWebLogic.sh

childPID=$!
wait $childPID


