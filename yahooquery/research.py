# stdlib
import json
from datetime import datetime, timedelta

# third party
import pandas as pd

from yahooquery.base import _YahooFinance
from yahooquery.utils import convert_to_list


class Research(_YahooFinance):
    """Enable user interaction with research report and trade idea APIs

    Keyword Arguments:
        username (str): Yahoo username / email
        password (str): Yahoo password

    Note:
        The methods available through this class are only available for
        subscribers to Yahoo Finance Premium
    """

    _OPERATORS = ["lt", "lte", "gt", "gte", "btwn", "eq", "and", "or"]

    _DATA = {
        "report": {
            "sortType": "DESC",
            "sortField": "report_date",
            "offset": 0,
            "size": 100,
            "entityIdType": "argus_reports",
            "includeFields": [
                "report_date",
                "report_type",
                "report_title",
                "head_html",
                "ticker",
                "pdf_url",
                "snapshot_url",
                "sector",
                "id",
                "change_in_investment_rating",
                "investment_rating",
                "change_in_target_price",
                "change_in_earnings_per_share_estimate",
            ],
        },
        "trade": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "offset": 0,
            "size": 100,
            "entityIdType": "trade_idea",
            "includeFields": [
                "startdatetime",
                "term",
                "ticker",
                "rating",
                "price_target",
                "ror",
                "id",
                "image_url",
                "company_name",
                "price_timestamp",
                "current_price",
                "trade_idea_title",
                "highlights",
                "description",
            ],
        },
        "earnings": {
            "sortType": "ASC",
            "sortField": "companyshortname",
            "offset": 0,
            "size": 100,
            "entityIdType": "earnings",
            "includeFields": [
                "ticker",
                "companyshortname",
                "startdatetime",
                "startdatetimetype",
                "epsestimate",
                "epsactual",
                "epssurprisepct",
            ],
        },
        "splits": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "entityIdType": "splits",
            "includeFields": [
                "ticker",
                "companyshortname",
                "startdatetime",
                "optionable",
                "old_share_worth",
                "share_worth",
            ],
        },
        "ipo": {
            "sortType": "DESC",
            "sortField": "startdatetime",
            "entityIdType": "ipo_info",
            "includeFields": [
                "ticker",
                "companyshortname",
                "exchange_short_name",
                "filingdate",
                "startdatetime",
                "amendeddate",
                "pricefrom",
                "priceto",
                "offerprice",
                "currencyname",
                "shares",
                "dealtype",
            ],
        },
    }

    TRENDS = {"options": ["Bearish", "Bullish"], "multiple": True}

    SECTORS = {
        "options": [
            "Basic Materials",
            "Communication Services",
            "Consumer Cyclical",
            "Consumer Defensive",
            "Energy",
            "Financial Services",
            "Healthcare",
            "Industrial",
            "Real Estate",
            "Technology",
            "Utilities",
        ],
        "multiple": True,
    }

    REPORT_TYPES = {
        "options": [
            "Analyst Report",
            "Insider Activity",
            "Market Outlook",
            "Market Summary",
            "Market Update",
            "Portfolio Ideas",
            "Quantitative Report",
            "Sector Watch",
            "Stock Picks",
            "Technical Analysis",
            "Thematic Portfolio",
            "Top/Bottom Insider Activity",
        ],
        "multiple": True,
    }

    DATES = {
        "options": {"Last Week": 7, "Last Month": 30, "Last Year": 365},
        "multiple": False,
    }

    TERMS = {
        "field": "term",
        "options": ["Short term", "Mid term", "Long term"],
        "multiple": True,
    }

    _QUERY_OPTIONS = {
        "report": {
            "investment_rating": TRENDS,
            "sector": SECTORS,
            "report_type": REPORT_TYPES,
            "report_date": DATES,
        },
        "trade": {
            "trend": TRENDS,
            "sector": SECTORS,
            "term": TERMS,
            "startdatetime": DATES,
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _construct_date(self, n=0):
        pass

    def _construct_query(self, research_type, **kwargs):
        pass

    def _construct_operand(self, k, v, research_type):
        pass

    def _construct_urls(self, config, params, **kwargs):
        pass

    def _get_symbol(self, response, params):
        pass

    def _get_research(self, research_type, size, **kwargs):
        pass

    def reports(self, size=100, **kwargs):
        """Retrieve research reports from Yahoo Finance

        Args:
            size (int, optional): Number of reports to return. Defaults to 100
            investment_rating (str or list, optional): Type of investment
                rating.  See :py:attr:`~TRENDS` for available options
            sector (str or list, optional): Sector
                See :py:attr:`~SECTORS` for available options
            report_type (str or list, optional): Report types
                See :py:attr:`~REPORT_TYPES` for available options
            report_date (str, optional): Date range
                See :py:attr:`~DATES' for available options

        Returns:
            pandas.DataFrame: DataFrame consisting of research reports

        Raises:
            ValueError: If invalid keyword argument is passed, if invalid
                option is passed for keyword argument, or if multiple values
                are passed and only a single value is accepted
        """
        pass

    def trades(self, size=100, **kwargs):
        """Retrieve trade ideas from Yahoo Finance

        Args:
            size (int, optional): Number of trades to return. Defaults to 100
            trend (str or list, optional): Type of investment
                rating.  See :py:attr:`~TRENDS` for available options
            sector (str or list, optional): Sector
                See :py:attr:`~SECTORS` for available options
            term (str or list, optional): Term length (short, mid, long)
                See :py:attr:`~TERMS` for available options
            startdatetime (str, optional): Date range
                See :py:attr:`~DATES' for available options

        Returns:
            pandas.DataFrame: DataFrame consisting of trade ideas

        Raises:
            ValueError: If invalid keyword argument is passed, if invalid
                option is passed for keyword argument, or if multiple values
                are passed and only a single value is accepted
        """
        pass
