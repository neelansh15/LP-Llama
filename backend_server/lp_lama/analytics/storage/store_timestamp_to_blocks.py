import logging
from datetime import datetime

from lp_lama.analytics.common.rpc_networks import get_rpc_network
from lp_lama.models import Block


logger = logging.getLogger(__name__)


class BlockTimestamp:
    def __init__(self, chain_id):
        self.chain_id = chain_id
        self._w3 = None

    @property
    def w3(self):
        if self._w3 is None:
            self._w3 = get_rpc_network(self.chain_id)
        return self._w3

    def store_date_to_block(self, _start_block_no=16651442):
        start_block_no = Block.objects.filter(chain_id=self.chain_id).order_by('block_no').last()
        if start_block_no is None:
            start_block_no = _start_block_no
        block_no = start_block_no + 1
        visited_block_date = set()
        block_date = datetime.fromtimestamp(self.w3.eth.getBlock(block_no).timestamp).date()
        if Block.objects.filter(chain_id=self.chain_id, block_date=block_date).exists():
            visited_block_date.add(block_date.strftime("%Y-%m-%d"))
        self._store_block_no_till_curr_date(block_date, block_no, visited_block_date)

    def _store_block_no_till_curr_date(self, block_date, block_no, visited_block_date):
        curr_date = datetime.now()
        while block_date <= curr_date:
            block_date_str = block_date.strftime("%Y-%m-%d")
            if block_date_str not in visited_block_date:
                Block.objects.create(date=block_date, chain_id=self.chain_id, block_no=block_no)
                visited_block_date.add(block_date_str)
                logger.info(f"Added {block_date_str=} for {block_no=}")
            block_no += 1
            block_date = datetime.fromtimestamp(self.w3.eth.getBlock(block_no).timestamp)
