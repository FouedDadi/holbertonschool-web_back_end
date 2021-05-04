#!/usr/bin/env python3
"""python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
    """
    lst = mongo_collection.find()
    return lst
