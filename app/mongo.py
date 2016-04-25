# -*- coding:utf-8 -*-
__author__ = 'Van'

import os
import pymongo
import datetime
# from bson import ObjectId

MONGODB_HOST = os.getenv("MONGODB_HOST", '127.0.0.1')
MONGODB_PORT = os.getenv("MONGODB_PORT", 27017)
mongodb_client = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
db_tabengying = mongodb_client.tabenying


def max_id(obj):
    """
    :param obj: article名
    :return: 最大的id
    """
    rs = mongodb_client.club[obj].find().sort("id", -1).limit(1)
    if rs.count() > 0:
        return int(rs[0].get("id"))
    else:
        return 1

