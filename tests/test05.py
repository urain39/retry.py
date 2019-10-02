#!/usr/bin/env python3
from time import sleep
from random import random
from retry import retry

def retry_when(errors):
    def handler(err, cnt):
        print("Error: retry wait 3s..(cnt: {0} / 3)".format(cnt))
        sleep(3 * random())

    return retry(errors, 3, handler)


@retry_when((Exception,))
def touch():
    0 / 0

touch()

