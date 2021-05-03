#!/usr/bin/env python3
"""function that lists all documents in a collection"""

import pymongo


def list_all(mongo_collection):
    """[summary]

    Args:
        mongo_collection ([type]): [description]

    Returns:
        [type]: [description]
    """
    docs = []
    documents = mongo_collection.find()
    for doc in documents:
        docs.append(doc)
    return docs
