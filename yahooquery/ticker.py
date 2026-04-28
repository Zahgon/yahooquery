# stdlib
import re
from datetime import datetime, timedelta

# third party
import pandas as pd

# first party
from yahooquery.base import _YahooFinance
from yahooquery.constants import (
    CONFIG,
    CORPORATE_EVENTS,
    FUND_DETAILS,
    FUNDAMENTALS_OPTIONS,
    FUNDAMENTALS_TIME_ARGS,
    MODULES_DICT,
)
from yahooquery.utils import convert_to_timestamp, flatten_list, history_dataframe


class Ticker(_YahooFinance):
    """
    Base class for interacting with Yahoo Finance API

    Arguments
    ----------
    symbols: str or list
        Symbol or list collection of symbols

    Keyword Arguments
    -----------------
    asynchronous: bool, default False, optional
        Defines whether the requests are made synchronously or asynchronously.
    country: str, default 'united states', optional
        This allows you to alter the following query parameters that are
        sent with each request:  lang, region, and corsDomain.
    formatted: bool, default False, optional
        Quantitative values are given as dictionaries with at least two
        keys:  'raw' and 'fmt'.  The 'raw' key expresses value numerically
        and the 'fmt' key expresses the value as a string.  See Notes for more
        detail
    max_workers: int, default 8, optional
        Defines the number of workers used to make asynchronous requests.
        This only matters when asynchronous=True
    proxies: dict, default None, optional
        Allows for the session to use a proxy when making requests
    timeout: int, default 5, optional
        Stop waiting for a response after a given number of seconds
    user_agent: str, default random.choice, optional
        A browser's user-agent string that is sent with the headers on each
        request
    validate: bool, default False, optional
        Validate existence of symbols during instantiation
    verify: bool or str, default True, optional
        Used to verify SSL certificates for HTTPS requests.  Can either be
        a boolean, in which case it controsl whether we verify the server's
        TLS certificate, or a string in which case it must be a path to a CA
        bundle to use.

    Notes
    -----
    When formatted is set to True, all quote_summary modules will return as
    dictionaries.  There are two reasons for this:

    1. Quantitative values are expressed as dictionaries.  For example:

       "totalPay": {
           "raw": 115554666,
           "fmt": "11.56M",
           "longFmt": "11,555,466"
       }

       When formatted is set to False, the _format_data method will return
       the value in the "raw" key.

    2. Dates are either expressed as timestamps:

       "governanceEpochDate": 1570147200

       Or as dictionaries:

        "exDividendDate": {
            "raw": 1573084800,
            "fmt": "2019-11-07"
        }

        When formatted is set to False, the _format_data method will return the
        date expressed in the format YYYY-MM-DD by either converting from the
        timestamp or retrieving the "fmt" key.
    """

    def __init__(self, symbols, **kwargs):
        validate = kwargs.pop("validate", False)
        super().__init__(**kwargs)
        self.symbols = symbols
        self.invalid_symbols = None
        if validate:
            self.symbols, self.invalid_symbols = self.validate_symbols()

    def _quote_summary(self, modules):
        pass

    def _quote_summary_dataframe(self, module, **kwargs):
        pass

    def _to_dataframe(self, data, **kwargs):
        pass

    @property
    def all_modules(self):
        """
        Returns all quoteSummary modules, indexed by module title
        for each symbol

        Notes
        -----
        Only returns JSON
        """
        pass

    def get_modules(self, modules):
        """
        Obtain specific quoteSummary modules for given symbol(s)

        Parameters
        ----------
        modules: list or str
            Desired modules for retrieval

        Notes
        -----
        Only returns JSON

        Raises
        ------
        ValueError
            If invalid module is specified
        """
        pass

    @property
    def asset_profile(self):
        """Asset Profile

        Geographical and business summary data for given symbol(s).

        Returns
        -------
        dict
            assetProfile module data
        """
        pass

    @property
    def calendar_events(self):
        """Calendar Events

        Earnings and Revenue expectations for upcoming earnings date for given
        symbol(s)

        Returns
        -------
        dict
            calendarEvents module data
        """
        pass

    @property
    def earnings(self):
        """Earnings

        Historical earnings data for given symbol(s)

        Returns
        -------
        dict
            earnings module data
        """
        pass

    @property
    def earnings_trend(self):
        """Earnings Trend

        Historical trend data for earnings and revenue estimations for given
        symbol(s)

        Returns
        -------
        dict
            earningsTrend module data
        """
        pass

    @property
    def esg_scores(self):
        """ESG Scores

        Data related to a given symbol(s) environmental, social, and
        governance metrics

        Returns
        -------
        dict
            esgScores module data
        """
        pass

    @property
    def financial_data(self):
        """Financial Data

        Financial KPIs for given symbol(s)

        Returns
        -------
        dict
            financialData module data
        """
        pass

    def news(self, count=25, start=None):
        """News articles related to given symbol(s)

        Obtain news articles related to a given symbol(s).  Data includes
        the title of the article, summary, url, author_name, publisher

        Parameters
        ----------
        count: int
            Desired number of news items to return
        start: str or datetime
            Date to begin retrieving news items.  If date is a str, utilize
            the following format: YYYY-MM-DD.

        Notes
        -----
        It's recommended to use only one symbol for this property as the data
        returned does not distinguish between what symbol the news stories
        belong to

        Returns
        -------
        dict
        """
        pass

    @property
    def index_trend(self):
        """Index Trend

        Trend data related given symbol(s) index, specificially PE and PEG
        ratios

        Returns
        -------
        dict
            indexTrend module data
        """
        pass

    @property
    def industry_trend(self):
        """Industry Trend

        Seems to be deprecated

        Returns
        -------
        dict
            industryTrend module data
        """
        pass

    @property
    def key_stats(self):
        """Key Statistics

        KPIs for given symbol(s) (PE, enterprise value, EPS, EBITA, and more)

        Returns
        -------
        dict
            defaultKeyStatistics module data
        """
        pass

    @property
    def major_holders(self):
        """Major Holders

        Data showing breakdown of owners of given symbol(s), insiders,
        institutions, etc.

        Returns
        -------
        dict
            majorHoldersBreakdown module data
        """
        pass

    @property
    def page_views(self):
        """Page Views

        Short, Mid, and Long-term trend data regarding a symbol(s) page views

        Returns
        -------
        dict
            pageViews module data
        """
        pass

    @property
    def price(self):
        """Price

        Detailed pricing data for given symbol(s), exchange, quote type,
        currency, market cap, pre / post market data, etc.

        Returns
        -------
        dict
            price module data
        """
        pass

    @property
    def quote_type(self):
        """Quote Type

        Stock exchange specific data for given symbol(s)

        Returns
        -------
        dict
            quoteType module data
        """
        pass

    @property
    def quotes(self):
        """Quotes

        Retrieve quotes for multiple symbols with one call

        Notes
        -----
        There will be more than one request if passing in more than 1,500
        symbols.  A 414 error code (URI Too long) will occur otherwise.

        Returns
        -------
        dict
        """
        pass

    @property
    def recommendations(self):
        """Recommendations

        Retrieve the top 5 symbols that are similar to a given symbol

        Returns
        -------
        dict
        """
        pass

    @property
    def share_purchase_activity(self):
        """Share Purchase Activity

        High-level buy / sell data for given symbol(s) insiders

        Returns
        -------
        dict
            netSharePurchaseActivity module data
        """
        pass

    @property
    def summary_detail(self):
        """Summary Detail

        Contains similar data to price endpoint

        Returns
        -------
        dict
            summaryDetail module data
        """
        pass

    @property
    def summary_profile(self):
        """Summary Profile

        Data related to given symbol(s) location and business summary

        Returns
        -------
        dict
            summaryProfile module data
        """
        pass

    @property
    def technical_insights(self):
        """Technical Insights

        Technical trading information as well as company metrics related
        to innovativeness, sustainability, and hiring.  Metrics can also
        be compared against the company's sector

        Returns
        -------
        dict
        """
        pass

    def _financials(
        self, financials_type, frequency=None, premium=False, types=None, trailing=True
    ):
        pass

    def _financials_dataframes(self, data, period_type):
        pass

    def all_financial_data(self, frequency="a"):
        """
        Retrieve all financial data, including income statement,
        balance sheet, cash flow, and valuation measures.

        Notes
        -----
        The trailing twelve month (TTM) data is not available through this
        method

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        """
        pass

    def get_financial_data(self, types, frequency="a", trailing=True):
        """
        Obtain specific data from either cash flow, income statement,
        balance sheet, or valuation measures.

        Notes
        -----
        See available options to pass to method through FUNDAMENTALS_OPTIONS

        Parameters
        ----------
        types: list or str
            Desired types of data for retrieval
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Raises
        ------
        ValueError
            If invalid type is specified
        """
        pass

    @property
    def corporate_events(self):
        pass

    @property
    def corporate_guidance(self):
        """"""
        pass

    @property
    def valuation_measures(self):
        """Valuation Measures
        Retrieves valuation measures for most recent four quarters as well
        as the most recent date

        Notes
        -----
        Only quarterly data is available for non-premium subscribers
        """
        pass

    def balance_sheet(self, frequency="a"):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.

        Returns
        -------
        pandas.DataFrame
        """
        pass

    def cash_flow(self, frequency="a", trailing=True):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Returns
        -------
        pandas.DataFrame
        """
        pass

    @property
    def company_officers(self):
        """Company Officers

        Retrieves top executives for given symbol(s) and their total pay
        package.  Uses the assetProfile module to retrieve data

        Returns
        -------
        pandas.DataFrame
            assetProfile module data
        """
        pass

    @property
    def earning_history(self):
        """Earning History

        Data related to historical earnings (actual vs. estimate) for given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            earningsHistory module data
        """
        pass

    @property
    def fund_ownership(self):
        """Fund Ownership

        Data related to top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            fundOwnership module data
        """
        pass

    @property
    def grading_history(self):
        """Grading History

        Data related to upgrades / downgrades by companies for a given
        symbol(s)

        Returns
        -------
        pandas.DataFrame
            upgradeDowngradeHistory module data
        """
        pass

    def income_statement(self, frequency="a", trailing=True):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Returns
        -------
        pandas.DataFrame
        """
        pass

    @property
    def insider_holders(self):
        """Insider Holders

        Data related to stock holdings of a given symbol(s) insiders

        Returns
        -------
        pandas.DataFrame
            insiderHolders module data
        """
        pass

    @property
    def insider_transactions(self):
        """Insider Transactions

        Data related to transactions by insiders for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            insiderTransactions module data
        """
        pass

    @property
    def institution_ownership(self):
        """Institution Ownership

        Top 10 owners of a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            institutionOwnership module data
        """
        pass

    @property
    def recommendation_trend(self):
        """Recommendation Trend

        Data related to historical recommendations (buy, hold, sell) for a
        given symbol(s)

        Returns
        -------
        pandas.DataFrame
            recommendationTrend module data
        """
        pass

    @property
    def sec_filings(self):
        """SEC Filings

        Historical SEC filings for a given symbol(s)

        Returns
        -------
        pandas.DataFrame
            secFilings endpoint data
        """
        pass

    # FUND SPECIFIC

    def _fund_holdings(self, holding_type):
        pass

    @property
    def fund_bond_holdings(self):
        """Fund Bond Holdings

        Retrieves aggregated maturity and duration information for a given
        symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings module data subset
        """
        pass

    @property
    def fund_category_holdings(self):
        """Fund Category Holdings

        High-level holding breakdown (cash, bonds, equity, etc.) for a given
        symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        pass

    @property
    def fund_equity_holdings(self):
        """Fund Equity Holdings

        Retrieves aggregated priceTo____ data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings module data subset
        """
        pass

    @property
    def fund_performance(self):
        """Fund Performance

        Historical return data for a given symbol(s) and symbol(s) specific
        category

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            fundPerformance module data
        """
        pass

    @property
    def fund_profile(self):
        """Fund Profile

        Summary level information for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            fundProfile endpoint data
        """
        pass

    @property
    def fund_holding_info(self):
        """Fund Holding Information

        Contains information for a funds top holdings, bond ratings, bond
        holdings, equity holdings, sector weightings, and category breakdown

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        dict
            topHoldings module data
        """
        pass

    @property
    def fund_top_holdings(self):
        """Fund Top Holdings

        Retrieves Top 10 holdings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        pass

    @property
    def fund_bond_ratings(self):
        """Fund Bond Ratings

        Retrieves aggregated bond rating data for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        pass

    @property
    def fund_sector_weightings(self):
        """Fund Sector Weightings

        Retrieves aggregated sector weightings for a given symbol(s)

        .. warning:: This endpoint will only return data for specific
                     securities (funds and etfs)

        Returns
        -------
        pandas.DataFrame
            topHoldings module data subset
        """
        pass

    @property
    def p_fair_value(self):
        pass

    # PREMIUM
    def p_all_financial_data(self, frequency="a"):
        """
        Retrieve all financial data, including income statement,
        balance sheet, cash flow, and valuation measures.

        Notes
        -----
        The trailing twelve month (TTM) data is not available through this
        method

        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly.  Value should be 'a' or 'q'.
        """
        pass

    def p_get_financial_data(self, types, frequency="a", trailing=True):
        """
        Obtain specific data from either cash flow, income statement,
        balance sheet, or valuation measures.

        Notes
        -----
        See available options to pass to method through FUNDAMENTALS_OPTIONS

        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Parameters
        ----------
        types: list or str
            Desired types of data for retrieval
        frequency: str, default 'a', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned
        """
        pass

    def p_balance_sheet(self, frequency="a"):
        """Balance Sheet

        Retrieves balance sheet data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly balance sheet.  Value should
            be 'a' or 'q'.

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        pass

    def p_cash_flow(self, frequency="a", trailing=True):
        """Cash Flow

        Retrieves cash flow data for most recent four quarters or most
        recent four years as well as the trailing 12 months

        Parameters
        ----------
        frequency: str, default 'a', optional
            Specify either annual or quarterly cash flow statement.  Value
            should be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        pass

    @property
    def p_corporate_events(self):
        pass

    def p_income_statement(self, frequency="a", trailing=True):
        """Income Statement

        Retrieves income statement data for most recent four quarters or most
        recent four years as well as trailing 12 months.

        Parameters
        ----------
        frequency: str, default 'A', optional
            Specify either annual or quarterly income statement.  Value should
            be 'a' or 'q'.
        trailing: bool, default True, optional
            Specify whether or not you'd like trailing twelve month (TTM)
            data returned

        Notes
        -----
        You must be subscribed to Yahoo Finance Premium and be logged in
        for this method to return any data

        Returns
        -------
        pandas.DataFrame
        """
        pass

    @property
    def p_company_360(self):
        pass

    @property
    def p_technical_insights(self):
        pass

    @property
    def p_portal(self):
        pass

    def p_reports(self, report_id):
        pass

    def p_ideas(self, idea_id):
        pass

    @property
    def p_technical_events(self):
        pass

    def p_valuation_measures(self, frequency="q"):
        """Valuation Measures
        Retrieves valuation measures for all available dates for given
        symbol(s)
        """
        pass

    @property
    def p_value_analyzer(self):
        pass

    @property
    def p_value_analyzer_drilldown(self):
        pass

    # HISTORICAL PRICE DATA
    def dividend_history(self, start, end=None):
        """
        Historical dividend data

        Pulls historical dividend data for a given symbol(s)

        Parameters
        ----------
        start: str or datetime.datetime
            Specify a starting point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object
        end: str of datetime.datetime, default None, optional
            Specify a ending point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object.

        Returns
        -------
        pandas.DataFrame
            historical pricing data
        """
        pass

    def history(
        self,
        period="ytd",
        interval="1d",
        start=None,
        end=None,
        adj_timezone=True,
        adj_ohlc=False,
    ):
        """
        Historical pricing data

        Pulls historical pricing data for a given symbol(s)

        Parameters
        ----------
        period: str, default ytd, optional
            Length of time
        interval: str, default 1d, optional
            Time between data points
        start: str or datetime.datetime, default None, optional
            Specify a starting point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object
        end: str of datetime.datetime, default None, optional
            Specify a ending point to pull data from.  Can be expressed as a
            string with the format YYYY-MM-DD or as a datetime object.
        adj_timezone: bool, default True, optional
            Specify whether or not to apply the GMT offset to the timestamp
            received from the API.  If True, the datetimeindex will be adjusted
            to the specified ticker's timezone.
        adj_ohlc: bool, default False, optional
            Calculates an adjusted open, high, low and close prices according
            to split and dividend information

        Returns
        -------
        pandas.DataFrame
            Historical pricing data. Indexed with a pd.MultiIndex with two
            levels 'symbol' and 'dates'.

            If `interval` is intraday then 'dates' level will be
            represented with a `pd.DatetimeIndex`.

            If `interval` is '1d' or higher then 'dates' level will be
            represented with a `pd.Index` with dtype 'object'. Rows
            relating to closed sessions are indexed with `datatime.date`.
            If the 'close' of the last row represents the latest price of
            an open session then this last row will be indexed with a
            `datatime.datetime` object giving the time of the last trade
            that the 'close' price relates to.
        """
        pass

    def _history_1m(self, adj_timezone=True, adj_ohlc=False):
        pass

    def _historical_data_to_dataframe(self, data, params, adj_timezone):
        pass

    def _adjust_ohlc(self, df):
        pass

    @property
    def option_chain(self):
        pass

    def _option_dataframe(self, data, symbol):
        pass
