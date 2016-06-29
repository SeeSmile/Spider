import pymongo

conn = pymongo.Connection("203.195.238.137", 27017)
db = conn.tage
db.authenticate("360netnews_test")
