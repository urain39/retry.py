# Retry lib
A simple retry lib for Python.

Usage
```py
from time import sleep
from retry import retry

def retry_when(error):
  return retry(error, 3,
               lambda cnt: (
                 print("sleep 10s"),
                 sleep(10)
               )
              )

@retry_when(ZeroDivisionError)
def _():
  return 0/0

_()
```
