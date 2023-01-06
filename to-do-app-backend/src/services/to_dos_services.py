import src.dao.to_dos_daos as dao
from src.models.to_dos_model import ToDo

#Gets all notes
def get_notes(user_id):
    notes_dict = {}
    notes = dao.get_notes(user_id)
    count = 1
    for note in notes:
        notes_dict[count] = ToDo(note[0], note[1], note[2], str(note[3]), note[4], note[5])
        print(notes_dict)
        count + 1
    return notes_dict

#Posts new note
def post_note(user_id, note, end_date, priority):
    dao.post_note(user_id, note, end_date, priority)

#Put updates note
def update_note(user_id, note_id, note, end_date, completed, priority):
    dao.update_note(user_id, note_id, note, end_date, completed, priority)

#Delete a single note
def delete_note(user_id, note_id):
    dao.delete_note(user_id, note_id)

#Delete all notes
def delete_all_notes(user_id):
    dao.delete_all_notes(user_id)