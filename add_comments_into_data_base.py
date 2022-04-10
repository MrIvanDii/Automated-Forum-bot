import sqlite3

conn = sqlite3.connect('quora_comments_list.sqlite')
cur = conn.cursor()

#cur.executescript('''
#DROP TABLE IF EXISTS Quora_Comments_List''')


conn.commit()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS Quora_Comments_List (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    comment TEXT UNIQUE,
    status BOOLEAN
    );

''')

conn.commit()

data_from_file = open('comments_list.txt').read().split('\n\n')

for comment in data_from_file:
    #print(comment)

    cur.execute("INSERT OR IGNORE INTO Quora_Comments_List (comment, status) VALUES(?,?)", (comment, 1))
    conn.commit()

print('Data was successfully uploaded')