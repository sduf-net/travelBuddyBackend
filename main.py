from fastapi import FastAPI
from database import Base, engine
from controllers.auth_controller import auth_controller

app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
