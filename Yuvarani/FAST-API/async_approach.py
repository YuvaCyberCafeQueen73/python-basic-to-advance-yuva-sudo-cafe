from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/dashboard")
async def showDashboard():
    customer, booking, payment = await asyncio.gather(get_customer(), get_booking(), get_payment_status())
    return {
        "customer": customer,
        "booking": booking,
        "payment": payment
    }

async def get_customer():
    await asyncio.sleep(2)
    return {"username": "Yuvarani"}

async def get_booking():
    await asyncio.sleep(2)
    return {"booking-date": "2026-11-02"}

async def get_payment_status():
    await asyncio.sleep(2)
    return {"status": "confirmed"}