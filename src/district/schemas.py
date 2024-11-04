from pydantic import BaseModel
from typing import List, Tuple, Literal


class DistrictSearchIn(BaseModel):
    total_districts: int # общее кол-во районов
    tunnels: List[Tuple[int, int]] # тоннели через которые производится поиск
    district_a: int # район А
    district_b: int # район Б

class DisctrictSearchResponse(BaseModel):
    result: Literal["YES", "NO"] # ответ на поиск пути
