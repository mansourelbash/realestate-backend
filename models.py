# models.py
from pydantic import BaseModel
from typing import Optional, List

class Geometry(BaseModel):
    rings: List[List[List[float]]]

class Attributes(BaseModel):
    OBJECTID: int
    VILL_CODE: str
    HOD_CODE: str
    SECTOR_CODE: str
    SHEET_NO: str
    PARCEL_ID: str
    DLS_KEY: str
    PARCEL_TYPE: int
    PARCEL_INFO_SOURCE: str
    PARCEL_PART_NO: int
    TEMP_P_ID: Optional[int]
    PARCEL_ID_D: int
    TRANSACTION_DATE: Optional[str]
    ORGANIZATION: str
    NOTES: Optional[str]
    SHEETID: Optional[str]
    GLOBALID: str
    SHAPE_AREA: float
    SHAPE_LEN: float

class Item(BaseModel):
    attributes: Attributes
    geometry: Geometry
