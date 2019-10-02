#!/usr/bin/env python3
from time import sleep
from random import random
from retry import retry

def retry_when(errors, callback=None):
    return retry(errors, 3, callback)


class Klass(object):
    def __init__(self):
        self._mantra = 'DO NOT TOUCH!'

        super(Klass, self).__init__()
        # Dynamic decorate due to private
        self.touch = retry_when(
                    Exception,
                    lambda err, cnt: print(
                        self._mantra.format(
                                sleep(3)
                            )
                        )
                    )(self.touch)

    def touch(self):
        0 / 0

Klass().touch()

