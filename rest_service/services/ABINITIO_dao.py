import sys
import re
import pymongo
from   pymongo import MongoClient

connection = MongoClient('localhost',27017) #Connect to MongoClient
db         = connection.test                #Connect to Database
handle     = db.abinitio


def searchByKey(key):

    items    = list(handle.find({"$or":[{"JOB":{'$regex':key,'$options':'i'}},{"APPLICATION":{'$regex':key}},{"SOURCE":{'$regex':key}},{"TARGET":{'$regex':key}}]}))
    # items    = list(handle.find({"$or":[{"FINAL_TBL":{"regex":key}},{"DRIVING_TBL":{"regex":key}},{"AGG_TBL":{"regex":key}},{"SOURCE":{"regex":key}},
    # {"JOB":{"regex":key}},{"APPLN":{"regex":key}},{"DESCRIPTION":{"regex":key}}]}))
    #find Operation returns a Cursor which is a pointer to the result set of the find operation.
    response = []
    for item in items:
        post = {
        "JOB"   : item["JOB"],
        "APPLICATION" : item["APPLICATION"],
        "SOURCE"     : item["SOURCE"],
        "TARGET"      : item["TARGET"]
        }
        response.append(post)
    print  response
    return response


################################################################################
if __name__ == "__main__":
    if len(sys.argv) > 1:
        searchByKey(sys.argv[1])
    else:
        print "Enter a value!!"  