import re
from html.parser import HTMLParser


def parse_plugin_tag(html):
    pattern = r'<plugin\s+.*/plugin>'
    tag = re.match(pattern, html)
    attrs = []
    if tag:
        type('', (HTMLParser,), {
            'handle_starttag': lambda *args: attrs.append(dict(args[-1]))  # args = (self, tag, attrs)
        })().feed(tag.string)
    return attrs


if __name__ == '__main__':
    print(parse_plugin_tag('<plugin  url="http://baidu.com" a1=1 a1=2   b="  s"></plugin>' * 2))
