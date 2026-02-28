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
# DATABASE CONNECTION (LAZY LOADING)
# Only connect when actually needed, not at startup
# This allows the app to start even if database isn't configured yet
# -----------------------------
db = None
cursor = None

def get_db_connection():
    """Get or create database connection (lazy loading)"""
    global db, cursor
    
    try:
        if db is None or not db.is_connected():
            db = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "*123#yolo"),
                database=os.getenv("DB_NAME", "deep_action_sniper"),
                autocommit=True
            )
            cursor = db.cursor()
        return db, cursor
    except mysql.connector.Error as err:
        print(f"❌ Database connection failed: {err}")
        raise Exception(f"Could not connect to database: {err}")

# Test database connection on startup (optional, logs but doesn't block)
try:
    get_db_connection()
    print("✅ Database connected successfully on startup")
except Exception as e:
    print(f"⚠️ Database will connect on first request: {e}")

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
    try:
        db, cursor = get_db_connection()
        
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
    except Exception as e:
        return {"error": f"Failed to add snipe: {str(e)}"}, 500

# -----------------------------
# GET ALL SNIPES
# -----------------------------
@app.get("/get_snipes")
async def get_snipes():
    try:
        db, cursor = get_db_connection()
        
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
    except Exception as e:
        return {"error": f"Failed to fetch snipes: {str(e)}"}, 500

# -----------------------------
# SIMULATE MARKET (Updated)
# -----------------------------
@app.post("/simulate_market")
def simulate_market():
    try:
        db, cursor = get_db_connection()
        
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
    except Exception as e:
        return {"error": f"Failed to simulate market: {str(e)}"}, 500