import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.image import generate_summary_image  # adjust if name differs

router = APIRouter(tags=["Image Summary"])

@router.get("/countriess/image")
def get_summary_image(db: Session = Depends(get_db)):
   
    image_path = "app/cache/summary.png"

    try:
       
        if not os.path.exists(image_path):
            generate_summary_image(db)

        if not os.path.exists(image_path):
            raise HTTPException(status_code=404, detail="Summary image not found")

        return FileResponse(image_path, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary image: {str(e)}")
