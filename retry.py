from functools import wraps

def retry(error, max_count=3, callback=None):
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
  # NOTE: This is a bug on CPython closure,
  #       the name of the variable in the sub
  #       function is just a value, so we can
  #       only use it as a pointer(list)...

  # count = 0
  count = [0]
  # pylint: disable=invalid-name
  def fn_wrapper(fn):
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
      result = None

      while True:
        try:
          # count += 1
          count[0] += 1
          result = fn(*args, **kwargs)
          break
        # pylint: disable=invalid-name
        except error as e:
          if count[0] <= max_count:
            if callable(callback):
              callback(count[0])
            continue
          else:
            raise e

      return result
    return wrapped_fn
  return fn_wrapper
