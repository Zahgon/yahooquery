# stdlib

# third party
import pandas as pd

from yahooquery.constants import COUNTRIES
from yahooquery.session_management import initialize_session

BASE_URL = "https://query2.finance.yahoo.com"


def _make_request(
    url, response_field=None, country=None, method="get", params={}, data=None, **kwargs
):
    pass


def search(
    query,
    country="United States",
    quotes_count=10,
    news_count=10,
    first_quote=False,
):
    """Search Yahoo Finance for anything

    Parameters
    ----------
    query: str
        What to search for
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    quotes_count: int, default 10, optional
        Maximum amount of quotes to return
    news_count: int, default 0, optional
        Maximum amount of news items to return
    """
    pass


def get_currencies():
    """Get a list of currencies"""
    pass


def get_exchanges():
    """Get a list of available exchanges and their suffixes"""
    pass


def get_market_summary(country="United States"):
    """Get a market summary

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.

    Returns
    -------

    """
    pass


def get_trending(country="United States"):
    """Get trending stocks for a specific region

    Parameters
    ----------
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    """
    pass
