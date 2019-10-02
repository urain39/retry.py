from functools import wraps


def retry(errors, max_count=3, callback=None):
    '''
    @param errors: any class which based on `Exception`
    @param max_count: optional, the max retry count
    @param callback: optional, be called with `retry count` and `exception`

    Examples:
        @retry(ZeroDivisionError, 3,
               lambda err, cnt: print(err, cnt))
        def _():
            0/0

        _()
    '''

    # pylint: disable=invalid-name
    def fn_wrapper(fn):
        @wraps(fn)
        def wrapped_fn(*args, **kwargs):
            retval = None

            count = 0
            while True:
                try:
                    count += 1
                    retval = fn(*args, **kwargs)
                    break
                # pylint: disable=invalid-name
                except errors as err:
                    if count <= max_count:
                        if callable(callback):
                            callback(err, count)

                        # continue
                    else:
                        raise err

            return retval

        return wrapped_fn

    return fn_wrapper
