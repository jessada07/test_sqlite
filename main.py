import sqlite3
from time import time
import math
import random
con = sqlite3.connect('transcript.db')
cur = con.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS transcript(subject TEXT, credit INTEGER, section INTEGER, grade TEXT, term INTEGER, number_id TEXT,\
     FOREIGN KEY (number_id) REFERENCES student(number_id))")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(number_id TEXT Primary Key, name TEXT, surename TEXT)")
    con.commit()
    con.close

def insert_grade(subject, credit, section, grade, term, number_id):
    cur.execute("INSERT INTO transcript VALUES(?,?,?,?,?,?)", (subject, credit, section, grade, term, number_id))
    
def insert_data(number_id, name, surename):
    cur.execute("INSERT INTO student VALUES(?,?,?)", (number_id, name, surename))


def get_data():
    n = 5801100000000
    list_subject = ["010123101   INTRODUCTION TO COMPUTER", "010123102   PROGRAMMING FUNDAMENTALS",\
     "040203111   ENGINEERING MATHEMATICS", "040313005   PHYSICS"]
    list_grade = ["A", "B", "C", "D"]
    for i in range(8000000):
    	insert_data(n, "Jessada", "Weeradetkumpon")
    	for j in range(40):
    		k = random.randint(0,3)
    		insert_grade(list_subject[k],"1", "1", list_grade[k], 1, n)
    	print(i,": success")
    	n+=1
    con.commit()    	
    con.close

create_table()
start = time()
get_data()
end = time()
elapsed = end - start
print(elapsed, "s")