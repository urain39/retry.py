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
  print("Pass")

_()
