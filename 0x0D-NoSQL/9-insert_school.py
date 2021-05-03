#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """[summary]

    Args:
        mongo_collection ([type]): [description]

    Returns:
        [type]: [description]
    """
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
