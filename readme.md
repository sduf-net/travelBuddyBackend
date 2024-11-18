source .venv/bin/activate
uvicorn main:app --reload
deactivate

### RUN TEST
ENV=test pytest