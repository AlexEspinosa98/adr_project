from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from modules.auth.infraestructure_auth.api.routes import auth_routes
from modules.surveys.infrastructure_surveys.api.routes import surveys_routes
from modules.admin.infrastructure_admin.api.routes import admin_routes
import uvicorn

app = FastAPI(title="ADR Project API")

# Mount static files directory
app.mount("/upload", StaticFiles(directory="uploads"), name="static")

# Add middleware
# app.add_middleware(RequestLoggingMiddleware)

# Include routers
app.include_router(auth_routes.router, prefix="/api/v1")
app.include_router(surveys_routes.router, prefix="/api/v1")
app.include_router(admin_routes.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to the ADR Project API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
