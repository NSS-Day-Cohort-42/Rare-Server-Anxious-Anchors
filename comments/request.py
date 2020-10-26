
from models import Comment
import sqlite3
import json


def get_all_comments():	

    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
       

	    SELECT
            c.id,
            c.commentBody,
            c.userId,
            c.postId
        FROM Comment c
        """)
        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'], row['commentBody'],row['userId'], row['postId'])
            comments.append(comment.__dict__)

    return json.dumps(comments)






      




       
