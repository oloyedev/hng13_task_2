from pydantic import BaseModel, HttpUrl, RootModel
from datetime import datetime
from typing import Optional, Dict, List


class PostResponse(BaseModel):
    message: str
    total: int
    last_refreshed_at: datetime



class StatusResponse(BaseModel):
    total_countries: int
    last_refreshed_at: Optional[str] = None

    class Config:
        orm_mode = True



class CountryResponse(BaseModel):
    id: int
    name: str
    capital: Optional[str]
    region: Optional[str]
    population: int
    currency_code: Optional[str]
    exchange_rate: Optional[float]
    estimated_gdp: Optional[float]
    flag_url: Optional[HttpUrl]
    last_refreshed_at: datetime

    class Config:
        from_attributes = True


#
class CountryListResponse(RootModel[List[CountryResponse]]):

    pass



class ValidationErrorResponse(BaseModel):
    error: str = "Validation failed"
    details: Dict[str, str]



class NotFoundResponse(BaseModel):
    error: str = "Country not found"



class ExternalAPIErrorResponse(BaseModel):
    error: str = "External data source unavailable"
    details: str



class SummaryImageErrorResponse(BaseModel):
    error: str = "Summary image not found"
