#!/usr/bin/env python3
"""
Listing all docs in a collection
"""
import pymongo


def list_all(mongo_collection):
    """
    Listing documents
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
