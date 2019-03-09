#!/usr/bin/python3
import os
import sys
import datetime
from influxdb import InfluxDBClient
from pprint import pprint
host = '127.0.0.1'
username = 'admin'
password = 'yourpssword'

client = InfluxDBClient(host=host, port=8086, username=username, password=password)
client.switch_database('stats')

date = os.popen("date +%s").read().split('\n')
time = ((int(date[0])) * 1000000000 - 10000000000)
hn = os.popen("hostname").read().split('\n')
mem_info = os.popen("cat /proc/meminfo | awk \'{print $1\" \"$2}\'").readlines()
mem_info = [i.rstrip('\n') for i in mem_info]
mem = {}
for i in mem_info:
    mem.update({(i.split(':')[0]): (i.split(':')[1])})
influx_data = []
influx_data.append(
        {
                "measurement": "memory",
                "tags": {
                        "hostname" : hn[0]
                },
                "time": time,
                "fields": mem
                }
        )
client.write_points(influx_data)
#pprint (influx_data)
