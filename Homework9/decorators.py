import functools
import requests
from collections import OrderedDict
from memory_profiler import memory_usage
import time


def time_deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = memory_usage()[0]

        result = func(*args, **kwargs)
        end_memory = memory_usage()[0]
        end_time = time.time()

        print(f'Time to perform function {func.__name__}: {end_time - start_time} seconds, Memory Used: {end_memory-start_memory} MB')
        return result
    return wrapper


def cache_deco(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))

            if cache_key in deco._cache:
                deco._cache_count[cache_key] += 1
                # Переносимо в кінець списку
                deco._cache.move_to_end(cache_key, last=True)

                return deco._cache[cache_key]
            result = f(*args, **kwargs)

            if len(deco._cache) >= max_limit:
                # Шукаємо сайт з найменшою кількістю запитів та видаляэмо його якщо досягли ліміту у словнику
                min_count_key = min(deco._cache_count, key=deco._cache_count.get)
                deco._cache_count.pop(min_count_key)
                deco._cache.pop(min_count_key)

            # Додаємо результат роботи нашоі функціі у відповідні словники
            deco._cache[cache_key] = result
            deco._cache_count[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        deco._cache_count = dict()
        return deco
    return internal

@cache_deco(max_limit=1)
@time_deco
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url('https://google.com/')
fetch_url('https://google.com/')
print(fetch_url._cache)
