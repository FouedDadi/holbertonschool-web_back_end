#!/usr/bin/env python3
"""python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """[summary]

    Args:
        mongo_collection ([type]): [description]
    """
    students = mongo_collection.aggregate([{"$project": {
        "name": '$name', "averageScore": {"$avg": "$topics.score"}}},
                                            {"$sort": {"averageScore": -1}}])
    return students
