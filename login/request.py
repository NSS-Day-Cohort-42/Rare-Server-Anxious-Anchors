import sqlite3
import json

def handlelogin(logincred):
    with sqlite3.connect("./rare.db") as conn: 
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            u.id,
            u.password,
            u.email
        FROM User u
        WHERE u.email = ?
        """, (logincred['username'], ))
        data = db_cursor.fetchone()

        response = {}

        try: 
            if data['password'] == logincred['password']:
                response['valid'] = True
                response['token'] = data['id']
        except TypeError:
            response['valid'] = False
            pass
    return json.dumps(response)
