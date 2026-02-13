from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from src.project_routes import app as routes_app

def get_application() -> FastAPI:
    """Get the FastAPI app instance."""
    _app = FastAPI(
        description="Tras - Language Translation API",)     

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"], 
        allow_headers=["*"], 
    )

    _app.include_router(routes_app)

    return _app

app = get_application()