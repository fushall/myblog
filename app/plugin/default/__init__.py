import re

import requests


class LinkPlugin:
    __type__ = 'default'

    def __init__(self, url):
        self.url = url

    def render(self):
        # look up cache for the plugin
        html = requests.get(self.url).text
        title = re.search('<title>(?P<title>.*)</title>', html).group('title')
        return '''
(function(){



}());
'''