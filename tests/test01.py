#!/usr/bin/env python3
from time import sleep
from retry import retry

def retry_when(errors):
  return retry(errors, 3,
               lambda err, cnt: (
                 print("sleep 3s"),
                 sleep(3)
               )
              )

@retry_when(ZeroDivisionError)
def _():
  print("Pass")

_()
