import json
from urllib.request import urlopen


class ClientAPI(object):
    def request(self, user):
        url = "https://api.github.com/users/%s" % user
        response = urlopen(url)
        print(response)
        raw_data = response.read().decode('utf-8')
        print(raw_data)
        return json.loads(raw_data)
