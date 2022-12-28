from src.utils.db import db_connection

#Create new user
def create_user(email, password, name):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('insert into user_info values (default, %s, %s, %s)', (email, password, name))
        con.commit()
    finally:
        con.close()

#Email check
def email_check(email):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('select * from user_info where (user_info_email = %s)', (email,))
        query_rows = cur.fetchall()
        return query_rows
    finally:
        con.close()