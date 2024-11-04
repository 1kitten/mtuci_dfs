import pytest

from district.schemas import DistrictSearchIn
from district.services import can_reach


@pytest.mark.asyncio
async def test_can_reach_positive():
    search_params = DistrictSearchIn(
        total_districts=5,
        tunnels=[(1, 2), (2, 3), (3, 4)],
        district_a=1,
        district_b=4
    )
    result = can_reach(
        total_districts=search_params.total_districts,
        tunnels=search_params.tunnels,
        district_a=search_params.district_a,
        district_b=search_params.district_b
    )

    assert result == "YES", "Ожидалось YES"


@pytest.mark.asyncio
async def test_can_reach_negative():
    search_params = DistrictSearchIn(
        total_districts=5,
        tunnels=[(1, 2), (2, 3), (4, 5)],
        district_a=1,
        district_b=5
    )
    result = can_reach(
        total_districts=search_params.total_districts,
        tunnels=search_params.tunnels,
        district_a=search_params.district_a,
        district_b=search_params.district_b
    )

    assert result == "NO", "Ожидалось NO"
