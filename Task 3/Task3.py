import functools
import time
from random import random
from random import seed
import null
from self import self


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(cache_key: int = 0, *args, **kwargs):
        wrapper_decorator.cache = []
        wrapper_decorator.num_calls += 1
        toc = time.perf_counter()
        if wrapper_decorator.num_calls == 1 or wrapper_decorator.num_calls > 10:
            tic = time.perf_counter()
            if tic - toc < 5 * 60:
                wrapper_decorator.num_calls = 0
                seed((time.perf_counter()-time.perf_counter())*1000)
                cache_key += int(random())
                if cache_key not in wrapper_decorator.cache:
                    wrapper_decorator.cache[cache_key] = func(*args, **kwargs)
        else:
            return wrapper_decorator.cache[cache_key]

    wrapper_decorator.num_calls = 0
    return wrapper_decorator

