from routes.routes import router as items_router
from fastapi import FastAPI

app = FastAPI()

# Include the router from controllers.py
app.include_router(items_router)