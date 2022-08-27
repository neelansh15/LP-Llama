from web3 import Web3
from web3.middleware import geth_poa_middleware


def get_rpc_network(chain_id):
    if chain_id == 137:
        w3 = Web3(Web3.HTTPProvider("https://rpc-mainnet.matic.quiknode.pro"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    elif chain_id == 250:
        w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/fantom/"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    elif chain_id == 56:
        w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    else:
        raise ValueError("Unrecognised chain_id")
    return w3
