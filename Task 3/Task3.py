import functools
import time


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        wrapper_decorator.num_calls += 1

        def wrapper_cache(cache_key=None):
            toc = time.perf_counter()
            if wrapper_decorator.num_calls == 0 or wrapper_decorator.num_calls > 10:
                tic = time.perf_counter()
                if tic - toc < 5 * 60:
                    wrapper_decorator.num_calls = 0
                    cache_key = args + tuple(kwargs.items())
                    if cache_key not in wrapper_cache.cache:
                        wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            else:
                return wrapper_cache.cache[cache_key]

        wrapper_cache.cache = dict()
        return wrapper_cache

    wrapper_decorator.num_calls = 0
    return wrapper_decorator
