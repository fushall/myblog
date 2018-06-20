import markdown


def markdown2html(md):
    return markdown.markdown(md, extensions=['fenced_code', 'codehilite(css_class=highlight)', 'tables'])
