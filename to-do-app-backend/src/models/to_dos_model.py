from json import JSONEncoder

class ToDo:

    def __init__(self, owner_id, to_do_id, to_do_note, to_do_end_date, to_do_completed, to_do_priority):
        self._owner_id = owner_id
        self._to_do_id = to_do_id
        self._to_do_note = to_do_note
        self._to_do_end_date = to_do_end_date
        self._to_do_completed = to_do_completed
        self._to_do_priority = to_do_priority

class ToDoEncoder(JSONEncoder):
    def default(self, class_obj):
        if isinstance(class_obj, ToDo):
            return class_obj.__dict__
        else:
            return super().default(self, class_obj)