#!/bin/bash --login
# set -x
computation_name="$(whoami)-$1-$(date +%Y%m%d-%H%M%S)"
boltctrl --folder helloworld/ --name ${computation_name} \
         --executable-name run.sh \
         --client-arguments "--python-file helloworld/$1" \
         --scheduler-address "mesos-1:11217"

separator="######################################"
echo -e "\n\n\n"
echo ${separator}
echo "Congratulations, you've now submitted a correct computation"
echo ${separator}

echo -e "\n\n\n"
echo ${separator}
echo "To kill the computation try this command: "
echo "bolt_scale --name ${computation_name} --instances 0 --scheduler-address mesos-1:11217"
echo ${separator}


echo -e "\n\n\n"
echo ${separator}
echo "To increae the number of instances of the computation try this command: "
echo "bolt_scale --name ${computation_name} --instances 4 --scheduler-address mesos-1:11217"
echo ${separator}
