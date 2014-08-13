import pymongo
import datetime

from pymongo import  Connection
connection = Connection()
db = connection['foodatabase']
posts = db.posts
db.collection()
for post in posts.find():
    post


