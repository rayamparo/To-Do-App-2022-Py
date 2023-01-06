from src.utils.db import db_connection

#Gets all notes
def get_notes(user_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('select * from to_do_note where (owner_id = %s)', (user_id,))
        query_row = cur.fetchall()
        return query_row
    finally:
        con.close()

#Posts a new note
def post_note(user_id, note, end_date, priority):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute(f"""insert into to_do_note values (%s, default,'{note}', %s, false, {priority})""", (user_id, end_date))
        con.commit()
    finally:
        con.close()

#Put updates note
def update_note(user_id, note_id, note, end_date, completed, priority):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('update to_do_note set to_do_note = %s, to_do_end_date = %s, to_do_completed = %s, to_do_priority = %s where (to_do_id = %s and owner_id = %s)', (note, end_date, completed, priority, note_id, user_id))
        con.commit()
    finally:
        con.close()

#Delete note
def delete_note(user_id, note_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('delete from to_do_note where (to_do_id = %s and owner_id = %s)', (note_id, user_id))
        con.commit()
    finally:
        con.close()

#Delete all notes
def delete_all_notes(user_id):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('delete from to_do_note where (owner_id = %s)', (user_id,))
        con.commit()
    finally:
        con.close()