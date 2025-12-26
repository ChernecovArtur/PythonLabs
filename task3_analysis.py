import time
from functools import lru_cache, wraps


def timing_decorator(func):


    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"{func.__name__} executed in {end - start:.4f} seconds"
        )
        return result

    return wrapper


@lru_cache(maxsize=None)
@timing_decorator
def heavy_computation(n: int) -> int:

    if n < 2:
        return n
    return heavy_computation(n - 1) + heavy_computation(n - 2)
