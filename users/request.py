import sqlite3
import json
from models import User

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Use the Black Box
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Wright the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            u.id,
            u.email,
            u.password,
            u.firstName,
            u.lastName,
            u.displayName,
            u.photo,
            u.profileCreation,
            u.profileType
        FROM User u
        """)

        # initializa an empty list to hold all user representaiton
        users = []

        # convert rows of data into a list
        dataset = db_cursor.fetchall()

        for row in dataset:

            # create an user instance from the current row.
            # database fields are specified in exact order
            # refer to the User class above
            user = User(row['id'], row['email'], row['password'], row['firstName'], 
                        row['lastName'], row['displayName'], row['photo'], 
                        row['profileCreation'], row['profileType'])

            users.append(user.__dict__)

    return json.dumps(users)

def get_single_user(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.email,
            u.password,
            u.firstName,
            u.lastName,
            u.displayName,
            u.photo,
            u.profileCreation,
            u.profileType
        FROM User u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], data['email'], data['password'], 
                    data['firstName'], data['lastName'], data['displayName'], data['photo'],
                    data['profileCreation'], data['profileType'])

    return json.dumps(user.__dict__)