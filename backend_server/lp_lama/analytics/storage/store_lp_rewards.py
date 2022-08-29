from pathlib import Path

from tqdm import tqdm

from lp_lama.analytics.abstract_classes.abstract_exchange import RuntimeExchange
from lp_lama.analytics.common.rpc_networks import get_rpc_network
from lp_lama.analytics.exchanges import SushiSwap, Pancakeswap
from lp_lama.models import Lp, Block
import pandas as pd


class LpRewardStore:
    def __init__(self, lp_id):
        self.lp = Lp.objects.get(id=lp_id)
        self.lp_exchange = self.lp.exchange
        self.data_file = Path(f"data_folder/lp_rewards/{lp_id}.pickle")
        self.data_file.parent.mkdir(exist_ok=True, parents=True)

    def get_df(self):
        if self.data_file.exists():
            df = pd.read_pickle(self.data_file)
        else:
            df = None
        return df

    def store_rewards(self):
        w3 = get_rpc_network(self.lp_exchange.chain_id)
        if self.lp.exchange.name == "sushiswap":
            exchange = SushiSwap(w3)
        elif self.lp.exchange.name == "pancakeswap":
            exchange = Pancakeswap(w3)
        date_gt = "2022-07-26"
        prev_df = self.get_df()
        if prev_df is not None:
            date_gt = prev_df.iloc[-1].name
        blocks = Block.objects.filter(chain_id=self.lp_exchange.chain_id, date__gt=date_gt).order_by("block_no")
        df_dict = {}
        for block in tqdm(blocks):
            reward, reward_price, lp_supply, lp_price, reserve0, reserve1, lp_token0_price, lp_token1_price = exchange.get_lp_reward_details_on_block(self.lp.pool_id, block.block_no)
            df_dict[block.date] = {
                "reward": reward,
                "reward_price": reward_price,
                "lp_supply": lp_supply,
                "lp_price": lp_price,
                "reserve0": reserve0,
                "reserve1": reserve1,
                "lp_token0_price": lp_token0_price,
                "lp_token1_price": lp_token1_price
            }
            df = pd.DataFrame.from_dict(df_dict, orient="index")
            if prev_df is not None:
                comb_df = pd.concat([prev_df, df])
                comb_df.to_pickle(self.data_file)
            else:
                df.to_pickle(self.data_file)
