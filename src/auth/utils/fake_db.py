import json
import os

PATH_FAKE_DB = os.path.join(os.path.dirname(__file__),'fake_db.json')

def get_db() -> dict:
    """
    Get the fake database.

    Returns:
        dict: The content of the fake database.
    """
    with open(PATH_FAKE_DB, "rb") as file:
        content = file.read()

    fake_users_db: dict = json.loads(content)

    return fake_users_db

def update_db(content: dict, fake_users_db: dict) -> None:
    """
    Update the fake database.

    Args:
        content (dict): The new content to add or update in the fake database.
        fake_users_db (dict): The current state of the fake database.
    """
    if len(fake_users_db) == 0:
        fake_users_db = content
    else:
        fake_users_db.update(content)
    
    with open(PATH_FAKE_DB, "w+") as file:
        json.dump(fake_users_db, file)