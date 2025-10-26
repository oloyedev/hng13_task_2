from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from ..schema import CountryResponse, PostResponse
from ..services.country import (
    refresh_countries,
    get_all_countries,
    get_country_by_name,
    delete_country
)
from ..database import get_db

router = APIRouter()


@router.post("/countries/refresh", response_model=PostResponse)
def refresh_countries_route(db: Session = Depends(get_db)):
    try:
        result = refresh_countries(db)
        return result
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



@router.get("/countries", response_model=List[CountryResponse])
def get_countries(
    region: Optional[str] = Query(None),
    currency: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    try:
        countries = get_all_countries(db, region, currency, sort)
        return countries
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")



@router.get("/countries/{name}", response_model=CountryResponse)
def get_country(name: str, db: Session = Depends(get_db)):
    country = get_country_by_name(db, name)
    if not country:
        raise HTTPException(status_code=404, detail="Country not found")
    return country



@router.delete("/countries/{name}")
def delete_countries(name: str, db: Session = Depends(get_db)):
    deleted = delete_country(db, name)
    if not deleted:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"message": "Country deleted successfully", "name": name}
