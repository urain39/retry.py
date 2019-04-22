# Retry lib
A simple retry lib for Python.

> DocString  
>   """  
>  @param errors: any class which based on `Exception`  
>  @param max_count: optional, the max retry count  
>  @param callback: optional, be called with `retry count` before retry  
>  
>  Examples:  
>    @retry(ZeroDivisionError, 3,  
>           lambda cnt, err: print(cnt))  
>    def _():  
>      0/0  
>  
>    _()  
>  """  

## Usage

```py
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
  return 0/0

_()
```

```py
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
  print([1, 2, 3, 4][0xff])

_()
```
