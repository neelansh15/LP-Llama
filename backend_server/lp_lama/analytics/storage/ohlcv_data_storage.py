import logging
from datetime import datetime, timedelta

import pandas as pd
from dateutil.parser import parse

from common.constants import DATA_FOLDER, CAN_BREAKPOINT
from storage.dexscreener.chart_addresses import CHART_ADDRESS
from storage.dexscreener.charts import DexScreenerCharts
from storage_constants.curr_pairs import CurrPair
from storage_constants.timeframe import TimeFrame, TIMEFRAME_TO_DEXSCREENER

logger = logging.getLogger(__name__)


class OhlcvDataStorage:
    def __init__(self, curr_pair: CurrPair, timeframe: TimeFrame):
        self.data_folder = DATA_FOLDER / f"ohlcv/{curr_pair.value}/{timeframe.value}"
        self.all_df_folder = self.data_folder / "all_df_folder"
        self.data_file = self.data_folder / "data.pickle"
        self.timeframe = timeframe
        self.curr_pair = curr_pair
        self._dex_screener = None
        self.max_num_of_bars = 1000

    @property
    def dex_screener(self) -> DexScreenerCharts:
        if self._dex_screener is None:
            self._dex_screener = DexScreenerCharts(CHART_ADDRESS[self.curr_pair])
        return self._dex_screener

    def get_data(self) -> pd.DataFrame:
        """Get stored data. To update use store_and_get_latest_bars function"""
        logger.info(f"Fetching stored data for {self.curr_pair}: {self.timeframe}")
        df = pd.read_pickle(self.data_file)
        return df

    def store_and_get_latest_bars(self):
        bars_df, stored_data_start_timestamp, stored_data_end_timestamp = \
            self.get_data_and_start_end_timestamp()
        """Not adding 500 to curr_timestamp even though DexScreener API is non-inclusive of 
        end_time, because even if we call this function at 4:00:01, then also we will 
        include the data, so no need to add. 
        As adding adds complication like when timing is 3:59:58, we do not have new 
        data but we still make an API call."""
        curr_timestamp = int(datetime.now().timestamp())
        self._store_data_between(bars_df, stored_data_end_timestamp, curr_timestamp)

    def store_data_from(self, start_date_str: str):
        """Store data from start_date_str till current time"""
        bars_df, stored_data_start_timestamp, stored_data_end_timestamp = \
            self.get_data_and_start_end_timestamp()
        start_timestamp = int(parse(start_date_str).timestamp())
        if start_timestamp < stored_data_start_timestamp:
            self._store_data_between(bars_df, start_timestamp, stored_data_start_timestamp)
        # self.store_and_get_latest_bars()

    def get_data_and_start_end_timestamp(self):
        try:
            bars_df = self.get_data()
            stored_data_start_timestamp = bars_df.iloc[0].timestamp
            stored_data_end_timestamp = bars_df.iloc[-1].timestamp
            return bars_df, stored_data_start_timestamp, stored_data_end_timestamp
        except FileNotFoundError:
            logger.info(f"{self.data_file=} not found, hence saving it")
            bars_df = self.dex_screener.get_latest_bars_df(self.timeframe, self.max_num_of_bars)
            self._save_data_to_file(bars_df)
            return self.get_data_and_start_end_timestamp()

    def _store_data_between(self, _bars_df, start_timestamp, end_timestamp):
        current_end_timestamp = end_timestamp
        bars_df_list = [_bars_df, ]
        bars_df = _bars_df
        dex_screener_minutes = TIMEFRAME_TO_DEXSCREENER[self.timeframe]
        start_time = datetime.fromtimestamp(start_timestamp)
        while current_end_timestamp > start_timestamp:
            logger.info(f"Getting dexscreener data till {bars_df.iloc[0].name=}")
            current_end_timestamp = self._fetch_and_update_bars_df_list(
                bars_df_list, current_end_timestamp, start_time,
                dex_screener_minutes, start_timestamp)
            if len(bars_df_list) > 1:
                bars_df_list.reverse()
                bars_df = pd.concat(bars_df_list)
                bars_df = self._save_data_to_file(bars_df)
                bars_df_list = [bars_df, ]
                # breakpoint()
        return bars_df

    def _fetch_and_update_bars_df_list(self, bars_df_list, current_end_timestamp,
                                       start_time, dex_screener_minutes, start_timestamp):
        # breakpoint()
        end_time = datetime.fromtimestamp(current_end_timestamp)
        bars_needed = int((end_time - start_time).total_seconds() / (60 * dex_screener_minutes))
        if bars_needed == 0:
            logger.info(f"{bars_needed=}, {start_timestamp=}, "
                        f"{current_end_timestamp=}, {self.timeframe=}")
            return 0
        num_of_bars = min(self.max_num_of_bars, bars_needed)
        # breakpoint()
        bars_df = self.dex_screener.get_bars_df_from(
            self.timeframe, current_end_timestamp, num_of_bars)
        if len(bars_df) > 0:
            bars_df_list.append(bars_df)
            end_timestamp = bars_df.iloc[0].timestamp
        else:
            breakpoint()
            logger.warning(f"For {current_end_timestamp=}, {len(bars_df)=}")
            bars_seconds = num_of_bars * 60 * dex_screener_minutes
            should_be_start_time = end_time - timedelta(seconds=bars_seconds)
            logger.warning(f"Returning {should_be_start_time.timestamp()=}")
            return should_be_start_time.timestamp()
        return end_timestamp

    def _save_data_to_file(self, df: pd.DataFrame):
        df = df.sort_index()
        # if len(df[df.index.duplicated()]) > 0:
        #     logger.error("Duplicate index found")
        #     if CAN_BREAKPOINT:
        #         breakpoint()
        # time_gap = df.index[1:] - df.index[:-1]
        # if all([time_gap[0] == element for element in time_gap]) is False:
        #     logger.error("time_gap is different")
        #     if CAN_BREAKPOINT:
        #         breakpoint()
        self.data_file.parent.mkdir(exist_ok=True, parents=True)
        df.to_pickle(self.data_file)
        return df

    # def _correct_df_file(self):
    #     df = self.get_data()


def main():
    logger.info("Starting")
    data_storage = OhlcvDataStorage(CurrPair.weth_usdc, TimeFrame.MIN_1)
    # data_storage.store_data_from("2021-07-29")
    df = data_storage.get_data()
    breakpoint()


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stdout, format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)
    main()
