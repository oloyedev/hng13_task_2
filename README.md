# 🌍 Country & Exchange API (v2)

A FastAPI backend that aggregates global country data and live exchange rates, computes estimated GDP values, and exposes REST endpoints for analysis — deployed on **Railway** with **MySQL**.

---

## 🚀 Features
- Fetch and cache countries from REST Countries API v2  
- Sync latest FX rates from Open Exchange Rates  
- Compute random GDP estimates for demonstration  
- Filter & sort countries by region, currency, or GDP  
- Delete or refresh country data  
- System-status & summary-image endpoints  
- Fully deployed using **Railway CI/CD**

---

## 🧩 Tech Stack
| Layer | Technology |
|-------|-------------|
| Language | Python 3.11 + |
| Framework | FastAPI |
| ORM | SQLAlchemy + Pydantic v2 |
| Database | MySQL (Railway Cloud) |
| Image Gen | Pillow (PIL) |
| Deployment | Railway |
| Testing | Postman / curl |

---

## ⚙️ Environment Variables

| Variable | Example Value | Description |
|-----------|----------------|-------------|
| `DATABASE_URL` | `mysql+pymysql://root:password@containers-us-west-xxx.railway.app:3306/railway` | MySQL connection string |
| `COUNTRY_API_URL` | `https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies` | External country source |
| `EXCHANGE_RATE_API_URL` | `https://open.er-api.com/v6/latest/USD` | Exchange-rate API source |

> **Tip:**  
> If both the API and database run inside the same Railway project, simply set  
> `DATABASE_URL = ${{ MySQL.MYSQL_URL }}`.

---

## 🧱 Project Structure

app/
├── main.py
├── config.py
├── database.py
├── models.py
├── schema.py
├── router/
│ ├── countries.py
│ ├── statuses.py
│ └── images.py
├── services/
│ ├── country.py
│ ├── status.py
│ └── utils.py
├── external/
│ ├── fetch_countries.py
│ └── fetch_rates.py
└── cache/
└── summary.png



---

## 🧪 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `/countries/refresh` | Refresh and cache all countries |
| `GET` | `/countries` | List all countries (optional filters) |
| `GET` | `/countries/{name}` | Retrieve single country |
| `DELETE` | `/countries/{name}` | Delete a country |
| `GET` | `/status` | System status overview |
| `GET` | `/countries/image` | Returns generated summary image |

---

## ▶️ Running Locally

```bash
# 1️⃣ Create & activate venv
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Create .env
cp .env.example .env   # then edit values

# 4️⃣ Run the app
uvicorn app.main:app --reload
```

Then open:
👉 http://127.0.0.1:8000/docs

## ☁️ Deployment on Railway

1.Push your code to GitHub.
2. Create a new Railway project → “Deploy from GitHub repo”.
3. Add a MySQL database service.
4. In your FastAPI service → Variables:

```ini
DATABASE_URL = ${{ MySQL.MYSQL_URL }}
COUNTRY_API_URL = https://restcountries.com/v2/all?fields=name,capital,region,population,flag,currencies
EXCHANGE_RATE_API_URL = https://open.er-api.com/v6/latest/USD
```

5. Enable Private Networking or use Public host if needed.
6. Deploy — your API goes live automatically.
