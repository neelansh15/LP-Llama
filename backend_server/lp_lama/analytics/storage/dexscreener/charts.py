import logging
from datetime import datetime

import pandas as pd
import requests
from retry import retry

from storage_constants.timeframe import TimeFrame, TIMEFRAME_TO_DEXSCREENER

from lp_lama.analytics.storage.dexscreener.chart_addresses import CHART_ADDRESS

logger = logging.getLogger(__name__)


class DexScreenerCharts:
    def __init__(self, chart_address):
        self.session = requests.Session()
        # self.dex_io = 5
        self.url = f"https://io.dexscreener.com/u/chart/bars/{chart_address}"

    def get_latest_bars_df(self, timeframe: TimeFrame, num_of_bars: int) -> pd.DataFrame:
        """Add 500 to curr_timestamp as DexScreener API is non-inclusive of end_time,
        hence increase it by marginal amount to make curr_time inclusive."""
        curr_timestamp = int(datetime.now().timestamp() + 500)
        bars_df = self.get_bars_df_from(timeframe, curr_timestamp, num_of_bars)
        return bars_df

    def get_bars_df_from(self, timeframe: TimeFrame, end_timestamp: int,
                         num_of_bars: int) -> pd.DataFrame:
        chart_url = self._get_bars_chart_url_till_time(end_timestamp, timeframe, num_of_bars)
        logger.info(f"{chart_url=}")
        dexscreen_data = self._get_data_from_chart_url(chart_url)
        bars_df = self._convert_dexscreen_data_to_df(dexscreen_data)
        return bars_df

    def _get_bars_chart_url_till_time(self, end_timestamp: int, timeframe: TimeFrame,
                                      num_of_bars: int):
        """We can only use end_time with DexScreener API (bug). Hence, by specifying num_of_bars,
        and then looping backwards, we can get historical data."""
        dex_timestamp = int(end_timestamp) * 1_000
        dex_timeframe = TIMEFRAME_TO_DEXSCREENER[timeframe]
        # url = f"{self.url.format(self.dex_io)}?from={dex_timestamp}&to={dex_timestamp}&res={dex_timeframe}&cb={num_of_bars}"
        url = f"{self.url}?from={dex_timestamp}&to={dex_timestamp}&res={dex_timeframe}&cb={num_of_bars}"
        return url

    @retry(tries=5, delay=10)
    def _get_data_from_chart_url(self, chart_url: str):
        logger.info("Fetching data from dexscreener")
        headers = {
            # "Host": "io.dexscreener.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            # "Accept-Language": "en-US,en;q=0.5",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Alt-Used": "io.dexscreener.com",
            "Connection": "keep-alive",
            # "Upgrade-Insecure-Requests": "1",
            # "Sec-Fetch-Dest": "document",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-Site": "none",
            # "Sec-Fetch-User": "?1",
            # "TE": "trailers"
        }
        response = self.session.get(chart_url, headers=headers)
        logger.info("Fetched data from dexscreener")
        # self.dex_io = max((self.dex_io + 1) % 10, 3)
        try:
            json_resp = response.json()
        except Exception as error:
            logger.error(f"{response.text=}")
            breakpoint()
            raise error
        return json_resp

    @staticmethod
    def _convert_dexscreen_data_to_df(dexscreen_data: dict):
        bars = dexscreen_data["bars"]
        bars_df = pd.DataFrame(bars)
        bars_df["datetime"] = pd.to_datetime(bars_df["timestamp"], unit='ms')
        bars_df.set_index("datetime", inplace=True)
        columns = ["open", "high", "low", "close", "volumeUsd", "timestamp"]
        bars_df = bars_df[columns].copy()
        for column in columns:
            bars_df[column] = bars_df[column].astype(float)
        bars_df["timestamp"] = (bars_df["timestamp"] / 1000).astype(int)
        return bars_df


def main():
    logger.info("Starting")
    # dexscreen_charts = DexScreenerCharts(CHART_ADDRESS[CurrPair.twoShare_wftm])
    # dexscreen_charts = DexScreenerCharts(CHART_ADDRESS[CurrPair.wbtc_usdc])
    dexscreen_charts = DexScreenerCharts(CHART_ADDRESS[CurrPair.weth_usdc])
    bars_df = dexscreen_charts.get_latest_bars_df(TimeFrame.MIN_1, 10)
    breakpoint()


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    main()
