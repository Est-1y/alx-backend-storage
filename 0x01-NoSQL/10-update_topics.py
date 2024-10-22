#!/usr/bin/env python3
"""
Changing all topics of a school doc based on their name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
