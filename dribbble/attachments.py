"""
Check for attachments.
"""

import requests as req
from lxml.cssselect import CSSSelector
from lxml.html import fromstring as parse


css = CSSSelector('.attachments a')


def attachments(shot):
    """Check if there are attachments for a given shot."""
    endpoint = "http://dribbble.com/shots/" + str(shot)
    content = req.get(endpoint).content
    html = parse(content)
    links = css(html)
    return links


def psds(shot):
    """Return PSD attachment links for a given shot."""
    files = []
    links = attachments(shot)
    for link in links:
        name = link.text.lower()
        if name.endswith('psd'):
            href = link.get('href')
            full_url = "http://dribble.com" + href
            files.append(full_url)
    return files
