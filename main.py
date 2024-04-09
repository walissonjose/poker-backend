from fastapi import FastAPI
import uvicorn

from src.controllers import routes
from src.config.database import db
from src.config.server import port

app = FastAPI(
    title="API to play poker game",
    description="FastAPI",
)

for route in routes:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(app, host=db["HOST_DB"], port=port, reload=True)
