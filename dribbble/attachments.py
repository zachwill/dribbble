"""
Check for attachments.
"""

import requests as req
from lxml.cssselect import CSSSelector as css
from lxml.etree import fromstring


selector = css('.attachments a')


def attachments(shot):
    """Check if there are PSD attachments for a given shot."""
    endpoint = "http://dribbble.com/shots/%s" % str(shot)
    content = req.get(endpoint).content
    html = fromstring(content)
    links = psds(selector(html))
    return links


def psds(attachments):
    """Return PSD links."""
    return attachments
