import json
import logging
from datetime import datetime

from lp_lama.analytics.abstract_classes.abstract_contract import AbstractContract
from lp_lama.analytics.covalent import Covalent
from lp_lama.analytics.lp_position import LpPosition

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
        _reward_earned, last_updated_block, _ = self.contract.functions.poolInfo(int(pool_id)).call(block_identifier=block_identifier)
        reward_earned = _reward_earned / 1e12
        return reward_earned

    def get_tvl(self, pool_id: int, block_identifier='latest'):
        end_datetime = datetime.fromtimestamp(self.w3.eth.getBlock(block_identifier).timestamp)
        block_date = end_datetime.strftime("%Y-%m-%d")
        lp_token0_price, token0_decimal = self.covalent.get_token_price_and_decimal_at_date(
            self.lp_address(pool_id).token0_addr, block_date)
        lp_token1_price, token1_decimal = self.covalent.get_token_price_and_decimal_at_date(
            self.lp_address(pool_id).token1_addr, block_date)
        _reserve0, _reserve1, _ = self.lp_address(pool_id).contract.functions.getReserves().call(
            block_identifier=block_identifier)
        reserve0 = _reserve0 / (10 ** token0_decimal)
        reserve1 = _reserve1 / (10 ** token1_decimal)

        lp_price = (lp_token0_price * reserve0) + (lp_token1_price * reserve1)
        return lp_price, reserve0, reserve1

    def get_lp_reward_details_on_block(self, pool_id, block_no):
        _reward = self.get_pool_info(pool_id, block_no)
        block_time = datetime.fromtimestamp(self.w3.eth.getBlock(block_no).timestamp)
        reward_price_date = block_time.strftime("%Y-%m-%d")
        reward_price, reward_decimal = self.covalent.get_token_price_and_decimal_at_date(self.REWARD_ADDRESS,
                                                                                         reward_price_date)
        reward = _reward / 10 ** reward_decimal

        lp_supply = self.lp_address(pool_id).contract.functions.balanceOf(self.ADDRESS).call(
            block_identifier=block_no)
        lp_price, reserve0, reserve1 = self.get_tvl(pool_id, block_no)
        return reward, reward_price, lp_supply, lp_price, reserve0, reserve1

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
        lp_price, reserve0, reserve1 = self.get_tvl(pool_id, end_block)

        reward_apr = total_reward * lp_supply * 100 / lp_price
        print(reward_apr)
        breakpoint()


class RuntimeExchange(AbstractExchange):
    def __init__(self, w3, address, reward_address):
        self.ADDRESS = address
        self.REWARD_ADDRESS = reward_address
        abi = json.loads("""[{"inputs":[{"internalType":"contract IERC20","name":"_sushi","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Harvest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"allocPoint","type":"uint256"},{"indexed":true,"internalType":"contract IERC20","name":"lpToken","type":"address"},{"indexed":true,"internalType":"contract IRewarder","name":"rewarder","type":"address"}],"name":"LogPoolAddition","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"allocPoint","type":"uint256"},{"indexed":true,"internalType":"contract IRewarder","name":"rewarder","type":"address"},{"indexed":false,"internalType":"bool","name":"overwrite","type":"bool"}],"name":"LogSetPool","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"sushiPerSecond","type":"uint256"}],"name":"LogSushiPerSecond","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"indexed":false,"internalType":"uint256","name":"lpSupply","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accSushiPerShare","type":"uint256"}],"name":"LogUpdatePool","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"SUSHI","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"contract IERC20","name":"_lpToken","type":"address"},{"internalType":"contract IRewarder","name":"_rewarder","type":"address"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"calls","type":"bytes[]"},{"internalType":"bool","name":"revertOnFail","type":"bool"}],"name":"batch","outputs":[{"internalType":"bool[]","name":"successes","type":"bool[]"},{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"claimOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"harvest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"lpToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"pids","type":"uint256[]"}],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"contract IMigratorChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingSushi","outputs":[{"internalType":"uint256","name":"pending","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract IERC20","name":"token","type":"address"},{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permitToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"uint128","name":"accSushiPerShare","type":"uint128"},{"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"internalType":"uint64","name":"allocPoint","type":"uint64"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"pools","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rewarder","outputs":[{"internalType":"contract IRewarder","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IRewarder","name":"_rewarder","type":"address"},{"internalType":"bool","name":"overwrite","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigratorChef","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_sushiPerSecond","type":"uint256"}],"name":"setSushiPerSecond","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"sushiPerSecond","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"},{"internalType":"bool","name":"direct","type":"bool"},{"internalType":"bool","name":"renounce","type":"bool"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"}],"name":"updatePool","outputs":[{"components":[{"internalType":"uint128","name":"accSushiPerShare","type":"uint128"},{"internalType":"uint64","name":"lastRewardTime","type":"uint64"},{"internalType":"uint64","name":"allocPoint","type":"uint64"}],"internalType":"struct MiniChefV2.PoolInfo","name":"pool","type":"tuple"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"int256","name":"rewardDebt","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"pid","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"withdrawAndHarvest","outputs":[],"stateMutability":"nonpayable","type":"function"}]""")
        super().__init__(w3, abi)
