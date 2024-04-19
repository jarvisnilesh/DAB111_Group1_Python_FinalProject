import sqlite3 
import csv 
import pandas as pd

def create_db():
    con = sqlite3.connect('movie_gross.db')
    cursor = con.cursor()

    cursor.execute('DROP TABLE moviesdb')

    create_table = """CREATE TABLE if not exists moviesdb(
                        Release TEXT,
                        Opening INT,
                        Total_Gross INT,
                        Pecent_Total DECIMAL(10,2),
                        Theaters INT,
                        Average INT,
                        Release_Date Date,
                        Distributor TEXT
                        );
                """

    cursor.execute(create_table)

    with open("moviedetails.csv") as f:
        data = csv.reader(f)


        for row in data:
            if row[0]=='Release':
                continue
            cursor.execute("INSERT INTO moviesdb VALUES (?,?,?,?,?,?,?,?)", (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7]))
            print('Data Inserted.!')

    con.commit() 
    con.close()      

create_db()
