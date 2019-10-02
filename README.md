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
>           lambda err, cnt: print(cnt))  
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
               lambda err, cnt: (
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
               lambda err, cnt: (
                 print("sleep 10s"),
                 sleep(10)
               )
              )

@retry_when((ZeroDivisionError, IndexError,))
def _():
  print([1, 2, 3, 4][0xff])

_()
```

## How to decorate a method with private members?

To decorate with private members you must call decorator
manually in `CLASS.__init__`, like following style:

```py

class Dog():
    def __init__(self, name):
	self._name = name

        def print_name():
            print(self._name)

        # Call decorator manually
        self.say = awesome_decorator(callback=print_name)(self.say)

   def say(self):
       print('Woof! Woof! Woof!')

```

