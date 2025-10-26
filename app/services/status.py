from sqlalchemy.orm import Session
from ..models import Country
from datetime import timezone

def get_status_overview(db: Session):
    """
    Returns system status — total number of countries
    and the timestamp of the most recent refresh.
    """

 
    total_countries = db.query(Country).count()

    latest_entry = (
        db.query(Country.last_refreshed_at)
        .order_by(Country.last_refreshed_at.desc())
        .first()
    )

    last_refreshed = latest_entry[0] if latest_entry else None

    return {
        "total_countries": total_countries,
        "last_refreshed_at": (
            last_refreshed.replace(tzinfo=timezone.utc).isoformat()
            if last_refreshed else None
        ),
    }
