import os
from dotenv import load_dotenv
from loguru import logger


from web3 import Web3
from eth_account import Account

load_dotenv()
Account.enable_unaudited_hdwallet_features()

SOLC_VERSION = os.getenv('SOLC_VERSION') or "0.8.0"
GOERLY_PROVIDER_URL = os.getenv('GOERLY_PROVIDER_URL')

def test_solc_version():
    logger.info(f"start to check solc version that must be {SOLC_VERSION}")
    assert SOLC_VERSION == "0.8.0"


def test_web3():
    logger.info(f"start to connect to web3")
    web3 = Web3(Web3.HTTPProvider(GOERLY_PROVIDER_URL))
    is_connected = web3.is_connected()

    chain_id = web3.eth.chain_id

    logger.info(f"chain id: {chain_id}")

    assert is_connected == True


def test_create_account():
    text = "John milk cat dog window"

    logger.info(f"start to create an account")
    # 0x0b87EB4eEC7634aB135DdA829d2f961279ebEAb1
    # 0xdabe48001b852fe364491b0f6a5a86473cb1edb843868b4924f569366b388053
    # acct = Account.create(text)
    # address = acct.address
    # address_checksum = Web3.to_checksum_address(address)
    web3 = Web3(Web3.HTTPProvider(GOERLY_PROVIDER_URL))
    # key = web3.to_hex(acct._private_key)
    add = "0xFAbA6eB0Ec80b4447bAcA6B90AF13188Dae150a6"

    account_balance = web3.eth.get_balance(add) 

    # logger.info(f"Address: {address}")
    # logger.info(f"key: {key}")
    logger.info(f"balace: {account_balance}")

