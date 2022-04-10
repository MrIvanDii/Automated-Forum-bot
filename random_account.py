import sqlite3
import random

conn = sqlite3.connect('quora_accounts.sqlite')
cur = conn.cursor()


def random_pass_acc():
    sqlite_select_query = """SELECT * FROM Quora_Accounts"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    data = []

    for row in records:
        if row[4] != 0:
            data.append(row)

        elif row[4] == 0:
            pass

        else:
            print('ERRooRRR')

    number = random.randint(0, len(data) - 1)

    email = data[number][2]
    password = data[number][3]

    sqlite_change_status = """UPDATE Quora_Accounts SET status = 0 WHERE email = ?"""
    cur.execute(sqlite_change_status, (email,))
    conn.commit()

    return email, password


def upgrade_status():

    sqlite_select_query = """SELECT * FROM Quora_Accounts"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    for row in records:
        status = row[4]
        sqlite_change_status = """UPDATE Quora_Accounts SET status = 1 WHERE status = ?"""
        cur.execute(sqlite_change_status, (status,))
        conn.commit()

        return "account - STATUS UPDATED SUCCESSFULLY"


def get_list_of_acc():
    sqlite_select_query = """SELECT * FROM Quora_Accounts"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    data = []

    for row in records:
        if row[4] != 0:
            data.append(row)

    conn.commit()


    return len(data)