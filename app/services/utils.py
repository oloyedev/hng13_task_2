import random
from typing import Dict

def generate_random_multiplier() -> int:
    return random.randint(1000, 2000)

def compute_estimated_gdp(population: int, exchange_rate: float) -> float:
    if not exchange_rate or exchange_rate == 0:
        return 0
    return round(population * generate_random_multiplier() / exchange_rate, 2)

def format_error(error: str, details: str) -> Dict[str, str]:
    return {"error": error, "details": details}
