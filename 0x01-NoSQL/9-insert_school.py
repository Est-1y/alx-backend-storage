#!/usr/bin/env python3
"""
Inserting a doc in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserting docs in a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
