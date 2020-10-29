
from models.user import User
from models import Post
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
            c.commentSubject,
            c.commentBody,
            c.userId,
            c.postId,
            u.firstName,
            u.lastName,
            p.title title
        FROM Comment c
        JOIN User u
            ON u.id = c.userId
        JOIN Post p
            ON p.id = c.postId
        """)
        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            comment = Comment(row['id'],row['commentSubject'], row['commentBody'],row['userId'], row['postId'])
            user = User("", "", "",row['firstName'], row['lastName'],"", "", "", "")
            post = Post("", "", "",row['title'], "", "")

            comment.user = (user.__dict__)
            comment.post = (post.__dict__)
            comments.append(comment.__dict__)

    return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
	    SELECT
            c.id,
            c.commentSubject,
            c.commentBody,
            c.userId,
            c.postId
        FROM Comment c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        comment = Comment(data['id'],data['commentSubject'], data['commentBody'],data['userId'], data['postId'])
        
        return json.dumps(comment.__dict__)

def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comment
            ( commentSubject, commentBody, userId, postId )
        VALUES
            ( ?, ?, ?, ? );
        """, ( new_comment['commentSubject'], new_comment['commentBody'], new_comment['userId'], new_comment['postId'] ))

        id = db_cursor.lastrowid
        new_comment['id'] = id
    return json.dumps(new_comment)







      




       
