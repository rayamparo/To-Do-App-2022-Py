from src.app import app
from json import dumps
from src.models.to_dos_model import ToDoEncoder
from flask import request, Response
import src.services.to_dos_services as services

#Gets or Posts a new To Do Note
@app.route('/notes', methods=['GET', 'POST', 'DELETE'])
def notes():
    #GET
    if request.method == 'GET':
        notes = services.get_notes()
        return dumps(notes, cls=ToDoEncoder)
    #POST
    if request.method == 'POST':
        req_body = request.get_json()
        note = req_body['note']
        services.post_note(note)
        return Response('Successfully posted new note', status=200)
    #DELETE
    if request.method == 'DELETE':
        services.delete_all_notes()
        return Response('Successfully deleted all notes', status=200)

#Updates and Deletes a To Do Note
@app.route('/notes/<int:to_do_note_id>', methods=['PUT', 'DELETE'])
def update_delete_note(to_do_note_id):
    #POST
    if request.method == 'PUT':
        note_id = to_do_note_id
        req_body = request.get_json()
        note = req_body['note']
        services.update_note(note_id, note)
        return Response('Successfully updated note', status=200)
    #DELETE
    if request.method == 'DELETE':
        note_id = to_do_note_id
        services.delete_note(note_id)
        return Response('Successfully deleted note', status=200)