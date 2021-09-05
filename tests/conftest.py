#!/usr/bin/python3

import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def minter(accounts):
    return accounts[1]


@pytest.fixture(scope="module")
def token(Token, owner, minter):
    return Token.deploy("Test Token", "TST", 18, 1e21, owner, minter, {'from': owner})
