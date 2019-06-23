import re
import unittest
from html.parser import HTMLParser
from xml.dom.minidom import parseString
from bs4 import BeautifulSoup

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
	<div class="container">
		<h1>This is title</h1>
		<plugin a=1></plugin>
		<p>
		    gagaga
			<a href="http://baidu.com">hahhaa</a>
			gagaga
			<code>
				//<a>code/a</a>
			</code>
			<pre><a>pre_a</a></pre>
			<xmp><a>xmp_a</a></xmp>
			<plugin url="http://aaa" show="False"></plugin>
		</p>
	</div>
</body>
</html>
'''


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('start:', tag, attrs)

    def handle_endtag(self, tag):
        print('end:', tag)

    def handle_data(self, data):
        print('data:', data)


class TestHTMLParser(unittest.TestCase):
    # def test_parse_a_tag(self):
    #     pattern = re.compile(r'<plugin(?P<attrs>.*?)>(.*?)</plugin\s*>')
    #     r = re.search(pattern, HTML)
    #     print(r.group('attrs'))
    #
    # def test_alter_html_dom(self):
    #     dom = parseString(HTML)
    #     plugin_ele = dom.getElementsByTagName('plugin')
    #     print(plugin_ele)

    def test_bs4_alter_dom(self):
        soup = BeautifulSoup(HTML)
        result = soup.find_all('plugin')
        tag = result[-1]
        tag.name = 'haha'
        print(tag)
        new_soup = BeautifulSoup('<b>new</b>')
        result = tag.replace_with(new_soup)
        print(tag)
        print(result)


if __name__ == '__main__':
    unittest.main()
