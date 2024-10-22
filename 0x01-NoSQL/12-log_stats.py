#!/usr/bin/env python3

from pymongo import MongoClient

client = MongoClient()
db = client.logs
collection = db.nginx

log_count = collection.count_documents({})
print(f"{log_count} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    method_count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {method_count}")

status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")
