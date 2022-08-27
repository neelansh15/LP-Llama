import logging

from web3 import Web3

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

    def lp(self, pool_id):
        if pool_id in self.id_to_lp:
            return self.id_to_lp[pool_id]
        pool_address = self.contract.functions.lpToken(pool_id)
        lp_position = LpPosition(self.w3, pool_address)
        self.id_to_lp[pool_id] = lp_position
        return lp_position

    def get_pool_info(self, pool_id, block_identifier='latest'):
        reward_earned, last_updated_block, _ = self.contract.functions.poolInfo(int(pool_id)).call(block_identifier=block_identifier)
        return reward_earned

    def get_reward_earned_between_blocks(self, pool_id, start_block, end_block):
        start_reward = self.get_pool_info(pool_id, start_block)
        end_reward = self.get_pool_info(pool_id, end_block)
        reward_earned = end_reward - start_reward
        breakpoint()
        self.web3.eth.getBlock(blockNumber).timestamp
        reward_price = self.covalent.get_token_price(self.REWARD_ADDRESS, )
