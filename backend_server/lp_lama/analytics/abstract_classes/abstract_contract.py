import logging

from web3 import Web3

logger = logging.getLogger(__name__)


class AbstractContract:
    ADDRESS: str

    def __init__(self, w3: Web3, abi: list[dict]):
        self.w3 = w3
        self.abi = abi
        self.contract = w3.eth.contract(Web3.toChecksumAddress(self.ADDRESS), abi=abi)
