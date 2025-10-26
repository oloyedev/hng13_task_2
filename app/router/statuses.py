from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema import StatusResponse
from ..services.status import get_status_overview
import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags=["System Status"])

@router.get("/status", response_model=StatusResponse)
def get_status(db: Session = Depends(get_db)):
    try:
        return get_status_overview(db)
    except Exception as e:
        logger.error(f"Error while fetching system status: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
