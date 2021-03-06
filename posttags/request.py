import sqlite3
import json
from models import Posttag

def get_all_posttags():
    
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.postId,
            pt.tagId
        FROM Posttag pt
        JOIN Post p
            ON p.id = pt.postId
        JOIN Tag t
            ON t.id = pt.tagId
        """)

        posttags = []

        
        dataset = db_cursor.fetchall()
    
        for row in dataset:

            posttag = Posttag(row['id'], row['postId'], row['tagId'])

            posttags.append(posttag.__dict__)

    return json.dumps(posttags)


def get_single_posttag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
        SELECT
            pt.id,
            pt.postId,
            pt.tagId

        FROM Posttag pt
         WHERE pt.id = ?
        """, ( id, ))

  
        data = db_cursor.fetchone()

        posttags = Posttag(data['id'], data['postId'], data['tagId'])

        return json.dumps(posttags.__dict__)