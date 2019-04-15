# Retry lib
A simple retry lib for Python.

Usage
```py
from time import sleep
from retry import retry


"""
  @param error: any class which based on `Exception`
  @param max_count: optional, by default it is 3
  @param callback: optional, be called with `retry count` before retry

  Examples:
    @retry(ZeroDivisionError, 3,
           lambda cnt: print(cnt))
    def _():
      0/0

    _()
"""


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
