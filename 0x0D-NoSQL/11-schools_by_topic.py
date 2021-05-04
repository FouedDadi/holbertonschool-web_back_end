#!/usr/bin/env python3
"""return the list of school having a specific topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
        topic ([type]): [description]

    Returns:
        [type]: [description]
    """
    for tpc in mongo_collection.find({"topics": topic}):
    return tpc
