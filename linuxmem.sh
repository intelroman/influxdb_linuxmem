#!/bin/bash

influx_ip="123.123.123.123"
influx_user="user"
influx_pass="pass"
influx_db="stats"


data=`cat /proc/meminfo | awk '{print $1$2}' | sed -e 's/:/=/g' | tr '\n' ','`
host=`hostname`
t=($(date +%s%N))
feed="mem_info,host=$host $data $t"
eval curl -u $influx_user:$influx_pass -i -XPOST 'http://$influx_ip:8086/write?db=$influx_db' --data-binary \' $feed \'

