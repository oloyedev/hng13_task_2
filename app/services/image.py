import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from sqlalchemy.orm import Session
from ..models import Country

CACHE_PATH = "app/cache/summary.png"

def generate_summary_image(db: Session):
    countries = db.query(Country).order_by(Country.estimated_gdp.desc()).limit(5).all()
    total = db.query(Country).count()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    img = Image.new("RGB", (800, 400), color=(25, 25, 25))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font = ImageFont.load_default()  # Use default font if Arial is not available

    draw.text((20, 20), f"🌍 Country Summary Report", fill=(255, 255, 255), font=font)
    draw.text((20, 60), f"Total Countries: {total}", fill=(180, 255, 180), font=font)
    draw.text((20, 100), "Top 5 by Estimated GDP:", fill=(255, 255, 255), font=font)

    y_offset = 130
    for c in countries:
        draw.text((40, y_offset), f"{c.name}: {round(c.estimated_gdp, 2)}", fill=(255, 255, 0), font=font)
        y_offset += 30

    draw.text((20, y_offset + 20), f"Last Refreshed: {timestamp}", fill=(180, 180, 255), font=font)

    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    img.save(CACHE_PATH)
    return CACHE_PATH
