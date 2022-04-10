import sqlite3

conn = sqlite3.connect('quora_URL_list.sqlite')
cur = conn.cursor()
conn.commit()


#cur.executescript('''DROP TABLE IF EXISTS Quora_URL_list''')
#conn.commit()


cur.executescript('''
    CREATE TABLE IF NOT EXISTS Quora_URL_list (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    url TEXT UNIQUE,
    status BOOLEAN
    );

''')
conn.commit()

data_from_file = open('URL_list.txt').read().split('\n')


for url in data_from_file:
    if url == '':
        pass
    else:
        cur.execute("INSERT OR IGNORE INTO Quora_URL_list (url, status) VALUES(?,?)", (url, 1))
        conn.commit()

print('Data was successfully uploaded')