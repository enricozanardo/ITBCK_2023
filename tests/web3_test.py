import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

SOLC_VERSION = os.getenv('SOLC_VERSION') 

def test_solc_version():
    logger.info(f"start to check solc version..")

    assert SOLC_VERSION == "0.4.0"

