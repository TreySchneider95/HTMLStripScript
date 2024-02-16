from bs4 import BeautifulSoup
import sys

BLACK_LIST = ('mso-border-alt:', 'word-break:keep-all')

# Open the file provided and cast it to beautiful soup using the html parser
with open(sys.argv[1], 'r+') as content:
    soup = BeautifulSoup(content, features="html.parser")


def get_html():
    """
    This function finds all the anchors then reduces it down to only anchors with internal spans. Then
    we loop through the reduced anchors to strip all the style and text from the spans and add them to
    the anchor. Last we use bs4's decompose to remove the nested spans. Nothing is returned because all
    of this is being done on the global soup variable.
    """
    anchors = soup.find_all('a')
    span_anchors = [anchor for anchor in anchors if anchor.find_all('span')]
    for anchor in span_anchors:
        anchors_spans = anchor.find_all('span')
        style = ''.join([span['style'] for span in anchors_spans])
        text = anchors_spans[0].get_text()
        anchor.string = text
        anchor['style'] = anchor['style'] + style
        styles = [x for x in anchor['style'].split(';') if not x.startswith(BLACK_LIST)]
        styles = ';'.join(styles)
        anchor['style'] = styles
        for span in anchors_spans:
            span.decompose()

get_html()

# Write the file back in place using bs4's prettify to add back in spacing for readability.
with open(sys.argv[1], 'w') as file:
    file.write(str(soup.prettify(formatter='html')))