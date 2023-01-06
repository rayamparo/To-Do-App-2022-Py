from src.app import app
from json import dumps
from src.models.to_dos_model import ToDoEncoder
from flask import request, Response
import src.services.to_dos_services as todo_services
import src.services.user_services as user_services

#Gets or Posts a new To Do Note
@app.route('/user/<int:user_id>/notes', methods=['GET', 'POST', 'DELETE'])
def notes(user_id):
    #GET
    if request.method == 'GET':
        notes = todo_services.get_notes(user_id)
        return dumps(notes, cls=ToDoEncoder)
    #POST
    if request.method == 'POST':
        req_body = request.get_json()
        note = req_body['note']
        end_date = req_body['endDate']
        priority = req_body['priority']
        todo_services.post_note(user_id, note, end_date, priority)
        return Response('Successfully posted new note', status=200)
    #DELETE
    if request.method == 'DELETE':
        todo_services.delete_all_notes(user_id)
        return Response('Successfully deleted all notes', status=200)

#Updates and Deletes a To Do Note
@app.route('/user/<int:user_id>/notes/<int:to_do_note_id>', methods=['PUT', 'DELETE'])
def update_delete_note(user_id, to_do_note_id):
    #POST
    if request.method == 'PUT':
        req_body = request.get_json()
        note = req_body['note']
        end_date = req_body['endDate']
        completed = req_body['completed']
        priority = req_body['priority']
        todo_services.update_note(user_id, to_do_note_id, note, end_date, completed, priority)
        return Response('Successfully updated note', status=200)
    #DELETE
    if request.method == 'DELETE':
        note_id = to_do_note_id
        todo_services.delete_note(user_id, note_id)
        return Response('Successfully deleted note', status=200)