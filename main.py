from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from controllers import routes
from config.server import port
from config.database import db
from config.middlewares.cors import cors

app = FastAPI(
    title="API for play Five Cards Draw Poker",
    version='0.0.1'
)

app.add_middleware(CORSMiddleware, **cors)

for router in routes:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app='main:app', host=db['host'], port=port, reload=True)
