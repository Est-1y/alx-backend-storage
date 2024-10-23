#!/usr/bin/env python3
"""Module"""
import redis
import requests
from functools import wraps

data = redis.Redis()


def cached_content_fun(method):
    """html content"""

    @wraps(method)
    def wrapper(url: str):
        cached_content = data.get(f"cached:{url}")
        if cached_content:
            return cached_content.decode('utf-8')

        content = method(url)
        data.setex(f"cached:{url}", 10, content)
        return content

    return wrapper


@cached_content_fun
def get_page(url: str) -> str:
    """number of times url access occured"""

    count = data.incr(f"count:{url}")
    content = requests.get(url).text
    return content


# if __name__ == "__main__":
    # get_page('http://slowwly.robertomurray.co.uk')
    # get_page('http://google.com')
