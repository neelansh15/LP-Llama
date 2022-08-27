import logging
from datetime import datetime

from abstract_classes.abstract_contract import AbstractContract
# from common.utils import get_deadline
from covalent import Covalent
from lp_position import LpPosition

logger = logging.getLogger(__name__)


class AbstractExchange(AbstractContract):
    ADDRESS: str
    REWARD_ADDRESS: str

    def __init__(self, w3, abi):
        super().__init__(w3, abi)
        self.id_to_lp = {}
        self._covalent = None

    @property
    def covalent(self):
        if self._covalent is None:
            self._covalent = Covalent(self.w3.eth.chain_id)
        return self._covalent

    def lp_address(self, pool_id) -> LpPosition:
        if pool_id not in self.id_to_lp:
            pool_address = self.contract.functions.lpToken(pool_id).call()
            lp_position = LpPosition(self.w3, pool_address)
            self.id_to_lp[pool_id] = lp_position
        return self.id_to_lp[pool_id]

    def get_pool_info(self, pool_id, block_identifier='latest'):
        reward_earned, last_updated_block, _ = self.contract.functions.poolInfo(int(pool_id)).call(block_identifier=block_identifier)
        return reward_earned

    def get_tvl(self, pool_id: int, block_identifier='latest'):
        end_datetime = datetime.fromtimestamp(self.w3.eth.getBlock(block_identifier).timestamp)
        block_date = end_datetime.strftime("%Y-%m-%d")
        lp_token0_price, token0_decimal = self.covalent.get_token_price_and_decimal_at_date(
            self.lp_address(pool_id).token0_addr, block_date)
        lp_token1_price, token1_decimal = self.covalent.get_token_price_and_decimal_at_date(
            self.lp_address(pool_id).token1_addr, block_date)
        reserve0, reserve1, _ = self.lp_address(pool_id).contract.functions.getReserves().call(
            block_identifier=block_identifier)

        lp_price = (lp_token0_price * reserve0 / 10 ** token0_decimal) + (
                    lp_token1_price * reserve1 / 10 ** token1_decimal)
        return lp_price

    def get_reward_earned_between_blocks(self, pool_id, start_block, end_block):
        start_reward = self.get_pool_info(pool_id, start_block)
        end_reward = self.get_pool_info(pool_id, end_block)
        reward_earned = end_reward - start_reward
        end_datetime = datetime.fromtimestamp(self.w3.eth.getBlock(end_block).timestamp)
        reward_price_date = end_datetime.strftime("%Y-%m-%d")
        reward_price, reward_decimal = self.covalent.get_token_price_and_decimal_at_date(self.REWARD_ADDRESS, reward_price_date)
        total_reward = reward_earned * reward_price / 10**reward_decimal

        lp_supply = self.lp_address(pool_id).contract.functions.balanceOf(self.ADDRESS).call(
            block_identifier=end_block)
        lp_price = self.get_tvl(pool_id, end_block)

        reward_apr = total_reward * lp_supply * 100 * 365 / (lp_price * 1e12)
        print(reward_apr)
        breakpoint()
