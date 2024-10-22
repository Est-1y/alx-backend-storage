#!/usr/bin/env python3
"""returning Nginx logs stats"""
import pymongo


def collection(db: dict) -> int:
    """retrieving log info"""
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(db)


def main():
    """Returning stats"""

    print(f"{collection({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection({'method': 'GET'})}")
    print(f"\tmethod POST: {collection({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection({'method': 'DELETE'})}")
    print(f"{collection({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
