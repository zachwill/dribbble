"""
Dribbble tests.
"""

from unittest import TestCase, main
from mock import Mock, MagicMock
import dribbble as d


class Dribbble(TestCase):

    def setUp(self):
        d.api.req = Mock()
        self.get = d.api.req.get

    def test_comments(self):
        d.comments(123)
        expected = "http://api.dribbble.com/shots/123/comments"
        self.get.assert_called_with(expected, params={})

    def test_draftees(self):
        d.draftees('vi')
        expected = "http://api.dribbble.com/players/vi/draftees"
        self.get.assert_called_with(expected, params={})

    def test_followers(self):
        d.followers('simplebits')
        expected = "http://api.dribbble.com/players/simplebits/followers"
        self.get.assert_called_with(expected, params={})

    def test_following(self):
        d.following('simplebits')
        expected = "http://api.dribbble.com/players/simplebits/following"
        self.get.assert_called_with(expected, params={})

    def test_info(self):
        d.info('dash')
        expected = "http://api.dribbble.com/players/dash"
        self.get.assert_called_with(expected, params={})

    def test_likes(self):
        d.likes('dash')
        expected = "http://api.dribbble.com/players/dash/likes"
        self.get.assert_called_with(expected, params={})

    def test_player(self):
        d.player('simplebits')
        expected = "http://api.dribbble.com/players/simplebits/shots"
        self.get.assert_called_with(expected, params={})

    def test_rebounds(self):
        d.rebounds('dash')
        expected = "http://api.dribbble.com/shots/dash/rebounds"
        self.get.assert_called_with(expected, params={})

    def test_scoreboard(self):
        d.scoreboard('dash')
        expected = "http://api.dribbble.com/players/dash/shots/following"
        self.get.assert_called_with(expected, params={})

    def test_scout(self):
        d.scout('vi')
        expected = "http://api.dribbble.com/players/vi"
        self.get.assert_called_with(expected, params={})

    def test_shot(self):
        d.shot(123)
        expected = "http://api.dribbble.com/shots/123"
        self.get.assert_called_with(expected, params={})

    def test_shots_for_popular(self):
        d.shots('popular')
        expected = "http://api.dribbble.com/shots/popular"
        self.get.assert_called_with(expected, params={})

    def test_shots_for_an_individual(self):
        d.shots('simplebits')
        expected = "http://api.dribbble.com/players/simplebits"
        self.get.assert_called_with(expected, params={})

    def test_teammates(self):
        d.teammates('vi')
        expected = "http://api.dribbble.com/players/vi/following"
        self.get.assert_called_with(expected, params={})


class Twitter(TestCase):

    def setUp(self):
        d.api.req = MagicMock()
        self.get = d.api.req.get

    def test_twitter(self):
        d.twitter('vi')
        expected = "http://api.dribbble.com/players/vi"
        self.get.assert_called_with(expected, params={})


if __name__ == '__main__':
    main()
