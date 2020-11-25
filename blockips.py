#!/usr/bin/python

import subprocess
import datetime

accessLog = '/var/log/nginx/access.log'
blockFile = '/etc/nginx/blockips.conf'

f = open(accessLog, 'r')
b = open(blockFile, 'a+')
d = dict()
p = dict()
badSearchs = ["wp-admin.php", "bingbot"]

for line in f:
    head, sep, tail = line.partition(' - ')
    for badSearch in badSearchs:
        if badSearch in tail:
            d[head] = 50
    if head in d:
        d[head] = d[head] + 1
    else:
        d[head] = 1
f.close()

for key in list(d.keys()):
    if d[key] >= 10:
        ipDeny = f"deny {key};"
        b.seek(0)
        if key != 'your-public-ip':
            if key not in b.read():
                b.seek(0)
                data = b.read(100)
                if len(data) > 0:
                    b.write("\n")
                b.write(ipDeny)
                print('Success: ' + str(datetime.datetime.now()) + ' IP: ' + key + ' has been banned.' + "\n")        
b.close()

command = 'sudo systemctl reload nginx'.split()
subproccess.call(command)

    


