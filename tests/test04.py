#!/usr/bin/env python3
from time import sleep
from random import random
from retry import retry

def retry_when(errors):
    def handler(err, cnt):
        print("Error: retry wait 3s..")
        sleep(3 * random())

    return retry(errors, 3, handler)


class Klass(object):
    def __init__(self):
        super(Klass, self).__init__()
        # Dynamic decorate
        self.touch = retry_when(Exception)(self.touch)

    def touch(self):
        0 / 0

Klass().touch()

