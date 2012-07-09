"""
Dribbble API docs:  http://dribbble.com/api

Core functions for interacting with the Dribbble API.
"""

import requests as req


ENDPOINT = "http://api.dribbble.com"


def get(url, **params):
    """Perform a GET request and parse the returned JSON."""
    if 'count' in params:
        count = params.pop('count')
        params['per_page'] = count
    response = req.get(url, params=params)
    return response.json


def comments(number, **params):
    """Return the comments for a given shot."""
    if isinstance(number, int):
        number = str(number)
    url = "/".join((ENDPOINT, "shots", number, "comments"))
    return get(url, **params)


def draftees(name, **params):
    """Return the draftees of a given player."""
    url = "/".join((ENDPOINT, "players", name, "draftees"))
    return get(url, **params)


def followers(name, **params):
    """Return the followers of a player."""
    url = "/".join((ENDPOINT, "players", name, "followers"))
    return get(url, **params)


def following(name, **params):
    """Return the players a given player is following."""
    url = "/".join((ENDPOINT, "players", name, "following"))
    return get(url, **params)


def info(name, **params):
    """Same as scouting a player."""
    return scout(name, **params)


def likes(name, **params):
    """Return a player's likes."""
    url = "/".join((ENDPOINT, "players", name, "likes"))
    return get(url, **params)


def player(name, **params):
    """Return data on a player."""
    url = "/".join((ENDPOINT, "players", name, "shots"))
    return get(url, **params)


def rebounds(number, **params):
    """Return the rebounds of a given shot."""
    url = "/".join((ENDPOINT, "shots", number, "rebounds"))
    return get(url, **params)


def scoreboard(name, **params):
    """Get the recent shots of the players a given player is following."""
    url = "/".join((ENDPOINT, "players", name, "shots", "following"))
    return get(url, **params)


def scout(name, **params):
    """Get the profile information of a given player."""
    url = "/".join((ENDPOINT, "players", name))
    return get(url, **params)


def shot(number, **params):
    """Return the shot for a specific id."""
    url = "/".join((ENDPOINT, "shots", str(number)))
    return get(url, **params)


def shots(kind=None, **params):
    """List of shots for either 'debuts', 'everyone', or 'popular'."""
    possible = ('debuts', 'everyone', 'popular')
    if not kind:
        kind = "popular"
    elif kind not in possible:
        # Misused. Looking for player shots.
        return scout(kind)
    url = "/".join((ENDPOINT, "shots", kind))
    return get(url, **params)


def teammates(name, **params):
    """Same as following."""
    return following(name, **params)


def twitter(name):
    """Return the Twitter username of a player."""
    info = scout(name)
    return info['twitter_screen_name']
