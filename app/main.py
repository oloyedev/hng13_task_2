from fastapi import FastAPI
from .router import countries, statuses, images
from .database import Base, engine
import os
# ✅ Create database tables automatically (only if they don’t exist)
Base.metadata.create_all(bind=engine)


print("🚀 DATABASE_URL from Railway:", os.getenv("DATABASE_URL"))


# ✅ Initialize FastAPI app
app = FastAPI(
    title="Country Currency & Exchange API",
    description=(
        "A RESTful API that fetches country data and exchange rates, "
        "computes estimated GDPs, and caches results in a database. "
        "Includes endpoints for refreshing data, querying countries, "
        "and serving a summary image."
    ),
    version="1.0.0"
)


app.include_router(countries.router)
app.include_router(statuses.router)
app.include_router(images.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Country Currency & Exchange API 🚀",
        "endpoints": {
            "refresh": "/countries/refresh",
            "get_all": "/countries",
            "get_one": "/countries/{name}",
            "delete": "/countries/{name}",
            "status": "/status",
            "image": "/countries/image"
        }
    }
