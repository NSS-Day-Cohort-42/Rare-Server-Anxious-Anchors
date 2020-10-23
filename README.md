Future code to consider __________

    def parse_url(self, path):
        # Splits path at forward slash storing each item in a list.
        url_segments = path.split("/")
        # Initialized as an empty string
        query_params = ""
        # Initialized as an empty list
        parameters = []
        # Id variable initialized as empty
        id = None
        # Initialized as an empty dictionary
        request = {}
        # The empty dictionary of request is being set to resource as the key with the value being the first postition of url_segments
        request["resource"] = url_segments[1]
        # If length of url_segments variable is greater than 2 
        if len(url_segments) > 2:
            # The variable params is equal to the third item in the list which is currently one
            params = url_segments[2]
            # url does not contain "?" also known as query string parameter, append the request dictionary to contain a key value pair.
            if not "?" in params:
                request["id"] = params 
            # url does have "?" or a query string parameter
            if "?" in params:
                [request["id"], query_params] = params.split("?")
                parameters = query_params.split("&")
        else:
            if "?" in url_segments[1]:
                [request["resource"], query_params] = url_segments[1].split("?")
                parameters = query_params.split("&")
        request["query_params"] = []
        for param in parameters:
            [ key, value ] = param.split("=")
            request["query_params"].append({ key: value })
        return request