# stdlib
import logging
import random

# third party
from bs4 import BeautifulSoup
from curl_cffi import requests
from requests.exceptions import ConnectionError, RetryError, SSLError
from requests_futures.sessions import FuturesSession

# first party
from yahooquery.constants import BROWSERS

logger = logging.getLogger(__name__)


DEFAULT_TIMEOUT = 5
DEFAULT_SESSION_URL = "https://finance.yahoo.com"
CRUMB_FAILURE = (
    "Failed to obtain crumb.  Ability to retrieve data will be significantly limited."
)
DEFAULT_SETUP_RETRIES = 5


def get_crumb(session):
    pass


def setup_session(session: requests.Session, url: str = None):
    pass


def initialize_session(session=None, **kwargs):
    pass
