from fastapi import FastAPI
import uvicorn

from controllers import routes
from config.server import port

app = FastAPI(
    title="API to play poker game",
    description="FastAPI",
)

for route in routes:
    app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=port, reload=True)