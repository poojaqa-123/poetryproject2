import pytest
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def test_one():
    logger.info(f"\Test 1...")
    assert 1 == 1
    print(f"\Test 1 ====")


def test_two():
    logger.info(f"\Test 2...")
    assert 1 == 1
    print(f"\Test 2 ====")


def test_three():
    logger.info(f"\Test 3...")
    assert 1 == 1
    print(f"\Test 3 ====")


# def test_four():
#     logger.info(f"\Test 4...")
#     assert 4==1
#     print(f"\Test 4 ====")

# def test_five():
#     logger.info(f"\Test 5...")
#     assert 5==1
#     print(f"\Test 5 ====")
