import pytest
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def test_sanity():
    logger.info(f"\nHello...")
    assert 1==1
    print(f"\nhello====")
