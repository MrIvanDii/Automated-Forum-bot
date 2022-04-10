import sqlite3
import random

conn = sqlite3.connect('quora_comments_list.sqlite')
cur = conn.cursor()

def random_comment():
    sqlite_select_query = """SELECT * FROM Quora_Comments_List"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    data = []

    for row in records:

        if row[2] != 0:
            data.append(row[1])

        elif row[2] == 0:
            pass

        else:
            pass

    number = random.randint(0, len(data) - 1)

    comment = data[number]

    sqlite_change_status = """UPDATE Quora_Comments_List SET status = 0 WHERE comment = ?"""
    cur.execute(sqlite_change_status, (comment,))
    conn.commit()
    print(data)

    return comment


def upgrade_commetns_status():

    sqlite_select_query = """SELECT * FROM Quora_Comments_List"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    for row in records:
        status = row[2]
        sqlite_change_status = """UPDATE Quora_Comments_List SET status = 1 WHERE status = ?"""
        cur.execute(sqlite_change_status, (status,))
        conn.commit()

        return "comments - STATUS UPDATED SUCCESSFULLY"

