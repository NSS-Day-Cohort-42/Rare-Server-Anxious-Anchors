import sqlite3
import json
from models import Post
from models import User



def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            p.id,
            p.postBody,
            p.postDate,
            p.title,
            p.userId,
            p.categoryId
        FROM Post p
        """)

        # Initialize an empty list to hold all animal representations
        posts = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            post = Post(row['id'], row['postBody'], row['postDate'], row['title'], row['userId'], row['categoryId'])

            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.postBody,
            p.postDate,
            p.title,
            p.userId,
            p.categoryId,
            u.displayName
        FROM Post p
        JOIN User u ON u.id = p.userId
        WHERE p.id = ?
        """, (id,))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        post = Post(data['id'], data['postBody'], data['postDate'], data['title'], data['userId'], data['categoryId'])

        user = User("", "", "", "", "", data['displayName'], "", "", "")
        post.user = user.__dict__

    return json.dumps(post.__dict__)