from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from login import handlelogin
from categories import get_all_categories, get_single_category
from comments import get_all_comments, get_single_comment,create_comment
from posttags import get_all_posttags, get_single_posttag
from tags import get_all_tags, get_single_tag
from posts import get_all_posts, get_single_post, create_post, delete_post
from users import get_all_users, get_single_user
from posttags import get_all_posttags, get_single_posttag


class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()


    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        
        if "?" in resource:
            param = resource.split("?")[1]  
            resource = resource.split("?")[0] 
            pair = param.split("=")  
            key = pair[0]  
            value = pair[1]  
            print(resource, key, value)
            return ( resource, key, value )
        
        else:
            id = None
            try:
                id = int(path_params[2])
            except IndexError:
                pass  
            except ValueError:
                pass  
            return (resource, id)




    def do_GET(self):
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"

            elif resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"

            elif resource == "tags":
                if id is not None:
                    response = f"{get_single_tag(id)}"
                else:
                    response = f"{get_all_tags()}"

            elif resource == "posttags":
                if id is not None:
                    response = f"{get_single_posttag(id)}"
                else:
                    response = f"{get_all_posttags()}"

            elif resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"

            elif resource == "comments":
                if id is not None:
                    response = f"{get_single_comment(id)}"
                else:
                    response = f"{get_all_comments()}"
            


        self.wfile.write(response.encode())
    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        new_item = None
        
        if resource == "posts":
            print(post_body)
            new_item = create_post(post_body)
        
        if resource == "comments":
            new_item = create_comment(post_body)
 
        self.wfile.write(f"{new_item}".encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self.do_POST()

    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "comments":
            delete_comment(id)

        if resource == "posts":
            delete_post(id)

        if resource == "tags":
            delete_tag(id)

        if resource == "post_tags":
            remove_post_tag(id)

        if resource == "categories":
            delete_category(id)

        self.wfile.write("".encode())



# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()