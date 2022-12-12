from src.utils.db import db_connection

#Gets all notes
def get_notes():
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute('select * from to_do_note')
        query_row = cur.fetchall()
        return query_row
    finally:
        con.close()

#Posts a new note
def post_note(note):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute(f"""insert into to_do_note values (default,'{note}')""")
        con.commit()
    finally:
        con.close()

#Put updates note
def update_note(note_id, note):
    try:
        con = db_connection()
        cur = con.cursor()
        cur.execute(f'update to_do_note set to_do_note = %s where (to_do_id = %s)', (note, note_id))
        con.commit()
    finally:
        con.close()