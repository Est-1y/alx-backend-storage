#!/usr/bin/env python3
"""
Returning list of schools having a specific topics.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Finding school list by topic
    """
    return mongo_collection.find({"topics": topic})
