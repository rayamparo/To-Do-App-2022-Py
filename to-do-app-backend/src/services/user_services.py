import src.dao.user_daos as dao
from src.models.user_model import User

#Create new user
def create_user(email, password, name):
    user_check = email_check(email)
    print(len(user_check))
    if(len(user_check) == 0):
        dao.create_user(email, password, name)
    else:
        return 'Email has already been registered'

#Email check
def email_check(email):
     return dao.email_check(email)

#Dict user info
def jsonify_user_info(user_info_row):
    user_dict = {}
    for info in user_info_row:
        user_dict[info[0]] = User(info[0], info[1], info[2], info[3])
    return user_dict

#User login
def user_login(email, password):
    #Checks for user email in DB
    user_info = email_check(email)
    #If email does not exist in DB
    if(len(user_info) == 0):
        return 'No user is associated with this email'
    #If email is in DB
    else:
        #If password does not match in DB
        if(user_info[0][2] != password):
            return 'Password incorrect'
        #Successful login
        else:
            user_dict = jsonify_user_info(user_info)
            print(user_dict)
            return user_dict