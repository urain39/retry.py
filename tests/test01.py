from time import sleep
from retry import retry

def retry_when(errors):
  return retry(errors, 3,
               lambda cnt, err: (
                 print("sleep 10s"),
                 sleep(10)
               )
              )

@retry_when(ZeroDivisionError)
def _():
  print("Pass")

_()
