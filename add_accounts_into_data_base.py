import sqlite3

conn = sqlite3.connect('quora_accounts.sqlite')
cur = conn.cursor()

conn.commit()

cur.executescript('''
DROP TABLE IF EXISTS Quora_Accounts;

CREATE TABLE Quora_Accounts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE,
    email TEXT UNIQUE,
    password INTEGER,
    status BOOLEAN
    );

''')

conn.commit()

data_from_file = open('accounts_list.txt').read().split('\n')

for accounts in data_from_file:
    data_list = accounts.split()
    name = data_list[0]
    email = data_list[1]
    password = data_list[2]
    cur.execute("INSERT INTO Quora_Accounts (name, email, password, status) VALUES(?,?,?,?)", (name, email, password, 1))
    conn.commit()

print('Data was successfully uploaded')