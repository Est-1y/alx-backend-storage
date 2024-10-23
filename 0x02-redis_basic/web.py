#!/usr/bin/env python3
"""
module
"""
import requests
import redis
from functools import wraps

store = redis.Redis()

def count_url_access(method):
    """url access count"""
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        
        if cached_data:
            return cached_data.decode("utf-8")
        
        count_key = "count:" + url
        try:
            html = method(url)
            store.incr(count_key)
            store.set(cached_key, html, ex=10)
            return html
        except requests.RequestException as e:
            return f"Error fetching {url}: {e}"
    
    return wrapper

@count_url_access
def get_page(url: str) -> str:
    """url content"""
    res = requests.get(url)
    res.raise_for_status()
    return res.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
