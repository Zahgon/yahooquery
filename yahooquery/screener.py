# stdlib
import re
from urllib import parse

from yahooquery.base import _YahooFinance
from yahooquery.constants import SCREENERS


class Screener(_YahooFinance):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _construct_params(self, config, params):
        pass

    def _construct_urls(self, config, params):
        pass

    def _get_symbol(self, response, params, **kwargs):
        pass

    def _check_screen_ids(self, screen_ids):
        pass

    @property
    def available_screeners(self):
        """Return list of keys available to pass to
        :func:`Screener.get_screeners`
        """
        pass

    def get_screeners(self, screen_ids, count=25):
        """Return list of predefined screeners from Yahoo Finance

        Parameters:
        screen_ids (str or list): Keys corresponding to list
            screen_ids = 'most_actives day_gainers'
            screen_ids = ['most_actives', 'day_gainers']
        count (int): Number of items to return, default=25
        """
        pass
