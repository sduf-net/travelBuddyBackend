from fastapi import FastAPI
from database import Base, engine
from controllers.auth_controller import auth_controller
from controllers.profile_controller import profile_controller
from controllers.explore_controller import explore_controller
from controllers.chat_controller import chat_controller

app = FastAPI()

# Initialize the database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
app.include_router(profile_controller.router, prefix="/profile", tags=["profile"])
app.include_router(chat_controller.router, prefix="/chat", tags=["chat"])
app.include_router(explore_controller.router, prefix="/explore", tags=["explore"])