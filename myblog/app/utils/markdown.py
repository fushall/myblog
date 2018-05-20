from markdown import markdown
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension
from markdown.util import etree





def markdown_to_html(md):
    return markdown(md, extensions=['fenced_code', 'codehitile'])


def markdown_to_text(md):
    return md
