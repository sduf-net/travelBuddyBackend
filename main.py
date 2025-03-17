import os
from fastapi import FastAPI
from database import Base, engine
from create_db import create_database
from controllers.auth_controller import auth_controller
from controllers.feed_controller import feed_controller

app = FastAPI()


if not os.getenv("ENV"):
    os.environ["ENV"] = "dev"

# create db
create_database()
# create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
app.include_router(feed_controller.router, prefix="/feed", tags=["feed"])