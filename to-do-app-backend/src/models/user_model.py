from json import JSONEncoder

class User:

    def __init__(self, user_info_id, user_info_email, user_info_password, user_info_name):
        self._user_info_id = user_info_id
        self._user_info_email = user_info_email
        self._user_info_password = user_info_password
        self._user_info_name = user_info_name

class UserEncoder(JSONEncoder):
    def default(self, class_obj):
        if isinstance(class_obj, User):
            return class_obj.__dict__
        else:
            return super().default(self, class_obj)