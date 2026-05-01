import pytest

def test_basic():
    assert True

@pytest.mark.asyncio
async def test_async_basic():
    assert True
