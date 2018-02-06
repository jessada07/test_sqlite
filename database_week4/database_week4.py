import sqlite3
import csv
import math
con = sqlite3.connect('test.db')
cur = con.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS grade(subject TEXT, credit INTEGER, section INTEGER, grade TEXT, term INTEGER, number_id TEXT,\
     FOREIGN KEY (number_id) REFERENCES data(number_id))")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS data(number_id TEXT Primary Key, name TEXT, surename TEXT)")
    con.commit()
    con.close

def insert_grade(subject, credit, section, grade, term, number_id):
    cur.execute("INSERT INTO grade VALUES(?,?,?,?,?,?)", (subject, credit, section, grade, term, number_id))
    con.commit()
    con.close
    
def insert_data(number_id, name, surename):
    cur.execute("INSERT INTO data VALUES(?,?,?)", (number_id, name, surename))
    con.commit()
    con.close

def view():
    #cur.execute("SELECT * FROM grade WHERE grade = 'A'")
    cur.execute("SELECT * FROM data ")
    records = cur.fetchall()
    con.close
    return records

def get_data():
    list_csv = ["5801012630033.csv", "5801012630106.csv", "5801012620011.csv", "5701012620101.csv", "5801012620097.csv"]
    insert_data("5801012630033", "Jessada", "Weeradetkumpon")
    insert_data("5801012630106", "Titi", "Rungruang")
    insert_data("5801012620011", "Kunasin", "Tongmanee")
    insert_data("5701012620101", "Banthita", "Limwilai")
    insert_data("5801012620097", "Supitcha", "Srisirikulwattana")
    for i in range(len(list_csv)):
        with open(list_csv[i]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                insert_grade(row["Subject"], row["Credit"], row["Section"], row["Grade"], row["Term"], row["Number_id"])
        print(list_csv[i],": success")
create_table()
get_data()
#print(view())