from time import sleep
from random import random
from retry import retry

def retry_when(errors):
    def handler(self, cnt, err):
        print("Error: retry wait 10s..")
        sleep(10 * random())

    return retry(errors, 3, handler)


class Klass(object):
    @retry_when((Exception,))
    def touch(self):
        0 / 0

Klass().touch()

