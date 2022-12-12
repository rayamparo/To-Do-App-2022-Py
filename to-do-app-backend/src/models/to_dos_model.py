from json import JSONEncoder

class ToDo:

    def __init__(self, to_do_id, to_do_note):
        self._to_do_id = to_do_id
        self._to_do_note = to_do_note

class ToDoEncoder(JSONEncoder):
    def default(self, class_obj):
        if isinstance(class_obj, ToDo):
            return class_obj.__dict__
        else:
            return super().default(self, class_obj)