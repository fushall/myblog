import markdown


def parse_post(markdown_stream):
    tags = ''
    title = ''

    maintext = []
    summary = []

    over_summary = False

    for line in markdown_stream.readlines():
        line = line.decode()

        if tags and title:
            maintext.append(line)
            if over_summary is not True:
                summary.append(line)

        if line.startswith('tags:'):
            tags = line[len('tags:'):].strip()

        elif line.startswith('title:'):
            title = line[len('title:'):].strip()

        elif line.startswith('#'):
            over_summary = True

    summary = ''.join(summary[:-1])
    maintext = ''.join(maintext)

    return title, tags, summary, maintext


def markdown2html(md):
    return markdown.markdown(md, extensions=['fenced_code', 'codehilite(css_class=highlight)'])
