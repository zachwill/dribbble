"""
Check for attachments.
"""

import requests as req
from lxml.cssselect import CSSSelector
from lxml.html import fromstring as parse


css = CSSSelector('.attachments a')


def attachments(shot):
    """Check if there are PSD attachments for a given shot."""
    endpoint = "http://dribbble.com/shots/%s" % str(shot)
    content = req.get(endpoint).content
    html = parse(content)
    return psds(html)


def psds(html):
    """Return PSD links."""
    files = []
    links = css(html)
    for link in links:
        name = link.text.lower()
        if name.endswith('psd'):
            href = link.get('href')
            full_url = "http://dribble.com" + href
            files.append(full_url)
    return files
