#!/usr/bin/env python3

import threading
import datetime
import time
import server
import random

def clientMain():
    msg = [1, 0]
    while True:
        now = datetime.datetime.now()
        msg[1] = int(random.uniform(0,10))
        server.msg_send(msg)
        print('[clientB]send:{0}, {1}'.format(msg, now))
        time.sleep(0.1)

def thread_start():
    t = threading.Thread(target = clientMain,args=())
    t.setDaemon(True)
    t.start()
