# stdlib
import logging
import os
from concurrent.futures import as_completed
from datetime import datetime
from typing import ClassVar
from urllib import parse

# third party
from requests_futures.sessions import FuturesSession
from tqdm import tqdm

# first party
from yahooquery.constants import (
    CONFIG,
    COUNTRIES,
)
from yahooquery.headless import YahooFinanceHeadless, has_selenium
from yahooquery.session_management import get_crumb, initialize_session
from yahooquery.utils import convert_to_list

logger = logging.getLogger(__name__)


class _YahooFinance:
    CHUNK: ClassVar[int] = 1500

    def __init__(self, **kwargs):
        self.country = kwargs.pop("country", "united states").lower()
        self.formatted = kwargs.pop("formatted", False)
        self.progress = kwargs.pop("progress", False)
        self.username = kwargs.pop("username", os.getenv("YF_USERNAME", None))
        self.password = kwargs.pop("password", os.getenv("YF_PASSWORD", None))
        self._setup_url = kwargs.pop("setup_url", os.getenv("YF_SETUP_URL", None))
        self.session = initialize_session(kwargs.pop("session", None), **kwargs)
        if self.username and self.password:
            self.login()
        self.crumb = get_crumb(self.session)

    @property
    def symbols(self):
        """
        List of symbol(s) used to retrieve information
        """
        pass

    @symbols.setter
    def symbols(self, symbols):
        pass

    @property
    def country(self):
        pass

    @country.setter
    def country(self, country):
        pass

    @property
    def default_query_params(self):
        """
        Dictionary containing default query parameters that are sent with
        each request.  The dictionary contains four keys:  lang, region,
        corsDomain, and crumb

        Notes
        -----
        The query parameters will default to
        {'lang': 'en-US', 'region': 'US', 'corsDomain': 'finance.yahoo.com'}

        To change the default query parameters, set the country property equal
        to a valid country.
        """
        pass

    def login(self) -> None:
        pass

    def _chunk_symbols(self, key, params=None, chunk=None, **kwargs):
        pass

    def validate_symbols(self) -> tuple[list[str], list[str]]:
        """Symbol Validation

        Validate existence of given symbol(s) and modify the symbols property
        to include only the valid symbols.  If invalid symbols were passed,
        they will be stored in the `invalid_symbols` property.
        """
        pass

    def _format_data(self, obj, dates):
        pass

    def _get_data(self, key, params=None, **kwargs):
        pass

    def _construct_params(self, config, params=None):
        pass

    def _construct_urls(self, config, params, **kwargs):
        """Construct URL requests"""
        pass

    def _async_requests(self, response_field, urls, params, **kwargs):
        pass

    def _sync_requests(self, response_field, urls, params, **kwargs):
        pass

    def _validate_response(self, response, response_field):
        pass

    def _get_symbol(self, response, params):
        pass

    def _construct_data(self, json, response_field, **kwargs):
        pass
