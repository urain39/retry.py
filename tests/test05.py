from time import sleep
from random import random
from retry import retry

def retry_when(errors):
    def handler(cnt, err):
        print("Error: retry wait 10s..(cnt: {0} / 3)".format(cnt))
        sleep(10 * random())

    return retry(errors, 3, handler)



@retry_when((Exception,))
def touch(self):
    0 / 0

touch()

