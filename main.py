import re
import sys

REG_STRING = r"\<span[^\>]+\><span[^/>]+\>(.[^</span>]*)\<\/span>\<\/span>"

def strip_html(path_to_document):
    """
    Opens file provided to the function. Then using re.sub finds all occurences of the pattern and replaces it with only the group one text.
    Finally it finds it way back to the beginning of the file and writes all the new text without the reg pattern and finally trucates just 
    to remove any trailing or leading whitespace.
    """
    with open(path_to_document, "r+") as file:
        text = file.read()
        text = re.sub(REG_STRING, r'\1', text)
        file.seek(0,0)
        file.write(text)
        file.truncate()

strip_html(sys.argv[1])
