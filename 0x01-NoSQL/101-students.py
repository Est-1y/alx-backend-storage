#!/usr/bin/env python3
"""
Returning all students sorted by average score.
"""


def top_students(mongo_collection):
    """ Top students"""
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
