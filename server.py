#!/usr/bin/env python3

import threading
import queue
import datetime
import time


q = queue.Queue()


def thread_start():
    t = threading.Thread(target = serverMain, args = (q,))
    t.setDaemon(True)
    t.start()


def serverMain(q:queue.Queue):
    ls = [0] * 2
    while True:
        while not q.empty():
            msg = q.get()
            ls[msg[0]] = msg[1]
            now = datetime.datetime.now()
            print('[server]get:{0},{1}'.format(ls, now))
        time.sleep(1)


def msg_send(msg):
    ls = []
    for i in msg:
        ls.append(i)
    q.put(ls)
