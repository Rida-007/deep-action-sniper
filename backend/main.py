from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import random
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId

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
async def health_check():
    return {"status": "healthy"}

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Deep Action Sniper Backend is running"}

# MongoDB configuration from env
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "deep_action_sniper")

mongo_client: AsyncIOMotorClient | None = None
db = None
snipes_coll = None

@app.on_event("startup")
async def startup_db_client():
    global mongo_client, db, snipes_coll
    mongo_client = AsyncIOMotorClient(MONGO_URI)
    db = mongo_client[MONGO_DB]
    snipes_coll = db.get_collection("snipes")
    # Ensure indexes if needed
    await snipes_coll.create_index("created_at")

@app.on_event("shutdown")
async def shutdown_db_client():
    global mongo_client
    if mongo_client:
        mongo_client.close()

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
async def add_snipe(snipe: Snipe):
    try:
        doc = {
            "url": snipe.url,
            "target_price": float(snipe.target_price),
            "current_price": 100.0,
            "status": "Active",
        }
        result = await snipes_coll.insert_one(doc)
        return {"message": "Snipe added successfully", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# GET ALL SNIPES
# -----------------------------
@app.get("/get_snipes")
async def get_snipes():
    try:
        cursor = snipes_coll.find().sort("_id", -1)
        snipes_list = []
        async for doc in cursor:
            snipes_list.append({
                "id": str(doc.get("_id")),
                "url": doc.get("url"),
                "target_price": float(doc.get("target_price", 0.0)),
                "current_price": float(doc.get("current_price", 0.0)),
                "profit": float(doc.get("current_price", 0.0)) - float(doc.get("target_price", 0.0)),
                "status": doc.get("status", "Unknown"),
                "created_at": doc.get("created_at").isoformat() if doc.get("created_at") else "",
            })
        return {"snipes": snipes_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------
# SIMULATE MARKET
# -----------------------------
@app.post("/simulate_market")
async def simulate_market():
    try:
        cursor = snipes_coll.find()
        updates = []
        async for doc in cursor:
            snipe_id = doc.get("_id")
            target_price = float(doc.get("target_price", 0.0))
            current_price = float(doc.get("current_price", 0.0))

            if current_price == 0:
                current_price = target_price + random.randint(-30, 30)

            movement = random.randint(-10, 10)
            new_price = current_price + movement
            if new_price < 1:
                new_price = 1

            status = "Target Hit" if new_price <= target_price else "Watching"

            await snipes_coll.update_one({"_id": snipe_id}, {"$set": {"current_price": new_price, "status": status}})

        return {"message": "Market simulated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
