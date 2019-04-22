from time import sleep
from retry import retry

def retry_when(errors):
  return retry(errors, 3,
               lambda cnt, err: (
                 print("sleep 10s"),
                 sleep(10)
               )
              )

@retry_when((ZeroDivisionError, IndexError,))
def _():
  0/0
  print([1, 2, 3, 4][0xff])

_()
