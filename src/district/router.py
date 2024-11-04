from fastapi import APIRouter
from district.services import search_path
from district.schemas import DistrictSearchIn


dist_router = APIRouter(tags=["district"])


@dist_router.post("/path_possibility")
async def get_path_possibility(search_params: DistrictSearchIn):
    """
        Вернуть ДА, если есть возможность найти путь
        между районами города, связанных между собой.
    """
    search_result = await search_path(search_params=search_params)
    return {"result": search_result}
