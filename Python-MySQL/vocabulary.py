#!/usr/bin/python
import MySQLdb
#from datetime import datetime
#import time
db = MySQLdb.connect(host ="127.0.0.1",
                     user="bubu",
                     password="bubububu",
                     db="vocabulary")


# step 1: define request time
request_type = raw_input("insert or select: ")

# step 2: generate insert request
ID = input("ID: ")
new_word = raw_input("word: ")
meaning_of_word = raw_input("meaning of the word: ")
#current_time = time.strftime(r"%d.%m.%Y %H:%M:%S", time.localtime())
#now = datetime.now.strftime('%Y-%m-%d %H:%M')
#now = datetime.now() 


insert_request = "insert into vocabulary (ID, word, meaning, datetime) values (%d, '%s', '%s', %s);" % (ID, new_word, meaning_of_word,"default")
print(insert_request)

# step 3: execute user's request
if request_type == "insert":
    print("bubu")
    cur = db.cursor()
    cur.execute(insert_request)
    db.commit()
db.close()

