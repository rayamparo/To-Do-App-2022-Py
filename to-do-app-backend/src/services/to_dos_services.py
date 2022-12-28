import src.dao.to_dos_daos as dao
from src.models.to_dos_model import ToDo

#Gets all notes
def get_notes(user_id):
    notes_dict = {}
    notes = dao.get_notes(user_id)
    for note in notes:
        notes_dict[note[0]] = ToDo(note[0], note[1])
    return notes_dict

#Posts new note
def post_note(note):
    dao.post_note(note)

#Put updates note
def update_note(note_id, note):
    dao.update_note(note_id, note)

#Delete a single note
def delete_note(note_id):
    dao.delete_note(note_id)

#Delete all notes
def delete_all_notes():
    dao.delete_all_notes()