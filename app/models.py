"""Import flask modules"""
import psycopg2

#connect using psycopg
conn = psycopg2.connect("dbname=stackover user=postgres password=123456 host=localhost")
#Activate connection cursor
cur = conn.cursor()

#create tables
cur.execute('''CREATE TABLE IF NOT EXISTS questions(
    id serial PRIMARY KEY,
    title varchar (50) NOT NULL,
    content varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    username varchar (50) NOT NULL,
    email varchar (100) NOT NULL,
    password varchar (100) NOT NULL,
    password_confirmation varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS answers(
    id serial PRIMARY KEY,
    body varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')

cur.execute('''CREATE TABLE IF NOT EXISTS comments(
    id serial PRIMARY KEY,
    content varchar (100) NOT NULL,
    timestamp timestamp default current_timestamp
) ''')
conn.commit()