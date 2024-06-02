import json

PATH_FAKE_DB = r'src\auth\utils\fake_db.json'

def get_db()->dict:

    """ Get fake DB"""
    with open(PATH_FAKE_DB, "rb") as file:
        content = file.read()

    fake_users_db:dict = json.loads(content)

    return fake_users_db

def update_db(content:dict, fake_users_db:dict)->None:

    """ Update fake DB"""

    if len(fake_users_db) == 0: fake_users_db = content
    else: fake_users_db.update(content)
    
    with open(PATH_FAKE_DB, "w+") as file:
        json.dump(fake_users_db, file)

