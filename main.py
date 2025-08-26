from fastapi import FastAPI
from config.db import db_config
from routes import user_routers

app = FastAPI(title="Youtube Manager", version="1.0.0")
app.include_router(user_routers.router)

@app.on_event("startup")
async def startup_db():
    await db_config.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await db_config.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
