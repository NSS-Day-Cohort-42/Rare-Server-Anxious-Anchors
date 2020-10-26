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
            pt.tagId,
        FROM Posttags pt
         WHERE a.id = ?
        """, ( id, ))

  
        data = db_cursor.fetchone()

        posttags = Posttags(row['id'], row['postId'], row['tagId'])

        return json.dumps(posttags.__dict__)