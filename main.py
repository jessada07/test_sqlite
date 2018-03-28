import sqlite3
con = sqlite3.connect('grade.db')
cur = con.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS data(subject TEXT, credit INTEGER, grade INTEGER, term INTEGER )")
    con.commit()
    con.close

def insert(subject, credit, grade, term):
    cur.execute("INSERT INTO data VALUES(?,?,?,?)", (subject, credit, grade, term))
    con.commit()
    con.close
    
def view():
    cur.execute("SELECT * FROM data")
    records = cur.fetchall()
    con.close
    return records

def update(subject, credit, grade):
    cur.execute("UPDATE data SET subject=?, credit=?, grade=?, term=?",(subject, credit, grade, term))
    con.commit()
    con.close

def delete(subject):
    cur.execute("DELETE FROM data WHERE subject=?",(subject,))
    con.commit()
    con.close

create_table()
insert("010123101   INTRODUCTION TO COMPUTER", 1, 4, 1)
insert("010123102   PROGRAMMING FUNDAMENTALS", 3, 2, 1)
insert("040203111   ENGINEERING MATHEMATICS I", 3, 3, 1)
insert("040313005   PHYSICS I", 3, 3, 1)
insert("040313006   PHYSICS LABORATORY I", 1, 3.5, 1)
insert("080103001   ENGLISH I", 1, 4, 1)
insert("080203901   MAN AND SOCIETY", 3, 4, 1)
insert("080303505   TABLE TENNIS", 1, 3.5, 1)
#delete("010123101   INTRODUCTION TO COMPUTER")
print(view())
