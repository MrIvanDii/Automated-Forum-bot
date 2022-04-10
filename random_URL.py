import sqlite3

conn = sqlite3.connect('quora_URL_list.sqlite')
cur = conn.cursor()

def get_list_of_url():
    sqlite_select_query = """SELECT * FROM Quora_URL_list"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    data = []

    for row in records:
        if row[2] != 0:
            data.append(row[1])
            sqlite_change_status = """UPDATE Quora_URL_list SET status = 0 WHERE url = ?"""
            cur.execute(sqlite_change_status, (row[1],))
            conn.commit()


    return data


def upgrade_url_status():

    sqlite_select_query = """SELECT * FROM Quora_URL_list"""
    cur.execute(sqlite_select_query)

    records = cur.fetchall()

    for row in records:
        status = row[2]
        sqlite_change_status = """UPDATE Quora_URL_list SET status = 1 WHERE status = ?"""
        cur.execute(sqlite_change_status, (status,))
        conn.commit()

        return "url - STATUS UPDATED SUCCESSFULLY"

