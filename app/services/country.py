from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from ..external.fetch_countries import fetch_countries
from ..external.fetch_rates import fetch_exchange_rates
from ..models import Country
from .utils import compute_estimated_gdp, format_error


def refresh_countries(db: Session):
    try:
        countries_data = fetch_countries()
        exchange_rates = fetch_exchange_rates()
    except ConnectionError as e:
        return format_error("External data source unavailable", str(e))

    for item in countries_data:
        name = item.get("name")
        capital = item.get("capital")
        region = item.get("region")
        population = item.get("population", 0)
        flag_url = item.get("flag_url")  # ✅ this now matches the fetch function
        currency_code = item.get("currency_code")  # ✅ same

        # ✅ compute exchange rate and GDP
        exchange_rate = exchange_rates.get(currency_code) if currency_code else None
        estimated_gdp = compute_estimated_gdp(population, exchange_rate) if exchange_rate else 0

        existing = db.query(Country).filter(Country.name.ilike(name)).first()

        if existing:
            existing.capital = capital
            existing.region = region
            existing.population = population
            existing.currency_code = currency_code
            existing.exchange_rate = exchange_rate
            existing.estimated_gdp = estimated_gdp
            existing.flag_url = flag_url
            existing.last_refreshed_at = datetime.utcnow()
        else:
            new_country = Country(
                name=name,
                capital=capital,
                region=region,
                population=population,
                currency_code=currency_code,
                exchange_rate=exchange_rate,
                estimated_gdp=estimated_gdp,
                flag_url=flag_url,
                last_refreshed_at=datetime.utcnow()
            )
            db.add(new_country)

    try:
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        return format_error("Database error", str(e))

    total = db.query(Country).count()
    return {
        "message": "Countries refreshed successfully",
        "total": total,
        "last_refreshed_at": datetime.utcnow().isoformat()
    }



def get_all_countries(db: Session, region: str = None, currency: str = None, sort: str = None):
    """
    Retrieve all countries, optionally filtered and sorted.
    """
    query = db.query(Country)

    if region:
        query = query.filter(Country.region.ilike(region))
    if currency:
        query = query.filter(Country.currency_code.ilike(currency))

   
    if sort == "gdp_desc":
        query = query.order_by(Country.estimated_gdp.desc())
    elif sort == "gdp_asc":
        query = query.order_by(Country.estimated_gdp.asc())

    return query.all()



def get_country_by_name(db: Session, name: str):
   
    country = db.query(Country).filter(Country.name.ilike(name)).first()
    return country



def delete_country(db: Session, name: str):
    """
    Delete a country record by name.
    """
    country = db.query(Country).filter(Country.name.ilike(name)).first()
    if not country:
        return {"error": "Country not found"}

    db.delete(country)
    db.commit()
    return {"message": f"{name} deleted successfully"}
