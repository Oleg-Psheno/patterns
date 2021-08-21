import quopri


class PostRequests:
    def get_params(self, environ):
        length = int(environ['CONTENT_LENGTH'])
        data = environ['wsgi.input'].read(length)
        params = self.parse_data(data)
        return params

    def parse_data(self, data):
        string_data = data.decode('utf-8')
        list_data = string_data.split('&')
        result = {}
        for el in list_data:
            k, v = el.split('=')
            result[k] = quopri.decodestring(
                bytes(v.replace('%', '=').replace('+', ' '), 'utf-8')).decode('utf-8')
        return result


class GetRequests:
    def get_params(self, environ):
        query_string = environ['QUERY_STRING']
        result = self.parse_params(query_string) if query_string else ''
        return result

    def parse_params(self, string):
        list_params = string.split('&')
        result = {}
        for el in list_params:
            k, v = el.split('=')
            result[k] = v
        return result
