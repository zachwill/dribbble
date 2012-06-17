dribbble
========

A simple Python wrapper for the [Dribbble API](http://dribbble.com/api).


Installation
------------

The easiest way to get the API is by using `pip`:

```
pip install dribbble
```


Usage
-----

The `dribbble` wrapper intends to make the API as easy to use as
possible.

```python

>>> import dribbble as d

# Get info on a player
>>> d.info('simplebits')

# Alternative, cooler name for getting info
>>> d.scout('simplebits')

# See the current community shots
>>> d.shots('popular')
>>> d.shots('everyone')
>>> d.shots('debut')

# Get shots for a player
>>> d.shots('simplebits')
>>> d.player('simplebits')

# Get information on a particular shot
>>> d.shot(1234)

# See a particular shot's rebounds
>>> d.rebounds(1234)

# Get comments on a shot
>>> d.comments(1234)

# See the likes for a player
>>> d.likes('simplebits')

# Get the followers of a player
>>> d.followers('simplebits')

# See who a player is following
>>> d.following('simplebits')
>>> d.teammates('simplebits')

# Get recent shots from the players a player is following
>>> d.scoreboard('simplebits')

# See who a given player has drafted
>>> d.draftees('simplebits')

# Get the Twitter username of a player
>>> d.twitter('simplebits')

# Check to see if a shot has attachments
>>> d.attachments(1234)

# See if a shot has PSD attachments
>>> d.psd(1234)
```
