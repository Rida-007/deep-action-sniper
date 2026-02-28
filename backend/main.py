from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ For production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint for Railway
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Deep Action Sniper Backend is running"}

# -----------------------------
# DATABASE CONNECTION
# Read from environment variables (Railway provides these)
# -----------------------------
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "*123#yolo"),
    database=os.getenv("DB_NAME", "deep_action_sniper")
)

cursor = db.cursor()

# -----------------------------
# DATA MODEL
# -----------------------------
class Snipe(BaseModel):
    url: str
    target_price: float

# -----------------------------
# ADD NEW SNIPE
# -----------------------------
@app.post("/add_snipe")
def add_snipe(snipe: Snipe):

    query = """
    INSERT INTO snipes (url, target_price, current_price, status)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        snipe.url,
        snipe.target_price,
        100,  # Starting price (initial)
        "Active"
    )

    cursor.execute(query, values)
    db.commit()

    return {
        "message": "Snipe added successfully",
        "id": cursor.lastrowid
    }

# -----------------------------
# GET ALL SNIPES
# -----------------------------
@app.get("/get_snipes")
async def get_snipes():
    cursor.execute("""
        SELECT id, url, target_price, current_price, status, created_at
        FROM snipes
        ORDER BY id DESC
    """)
    result = cursor.fetchall()

    snipes_list = []

    for row in result:
        target_price = float(row[2] or 0)
        current_price = float(row[3] or 0)

        profit = current_price - target_price

        snipes_list.append({
            "id": row[0],
            "url": row[1],
            "target_price": target_price,
            "current_price": current_price,
            "profit": profit,
            "status": row[4] or "Unknown",
            "created_at": str(row[5]) if row[5] else ""
        })

    return {"snipes": snipes_list}

# -----------------------------
# SIMULATE MARKET (Updated)
# -----------------------------
@app.post("/simulate_market")
def simulate_market():

    cursor.execute("SELECT id, target_price, current_price FROM snipes")
    snipes = cursor.fetchall()

    if not snipes:
        return {"message": "No snipes available"}

    for s in snipes:
        snipe_id = s[0]
        target_price = float(s[1] or 0)
        current_price = float(s[2] or 0)

        # If current price is zero (first simulation), we start near the target
        if current_price == 0:
            current_price = target_price + random.randint(-30, 30)

        # Gradual market movement (simulating price changes)
        movement = random.randint(-10, 10)
        new_price = current_price + movement

        # Ensure price doesn't go below 1
        if new_price < 1:
            new_price = 1

        # Check if the target price has been hit
        if new_price <= target_price:
            status = "Target Hit"
        else:
            status = "Watching"

        # Update the snipes table with the new price and status
        update_query = """
        UPDATE snipes
        SET current_price = %s,
            status = %s
        WHERE id = %s
        """

        cursor.execute(update_query, (new_price, status, snipe_id))

    db.commit()

    return {"message": "Market simulated successfully"}