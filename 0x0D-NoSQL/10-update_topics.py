#!/usr/bin/env python3
"""change all topics of a school document based on the name"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
        name ([type]): [description]
        topics ([type]): [description]
    """
    new_key = {"name": name}
    new_value = {"$set": {"topics": topics}}
    mongo_collection.update_many(new_key, new_value)
