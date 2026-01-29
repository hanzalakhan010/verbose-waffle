import os
from fastapi import FastAPI

import psycopg2
app = FastAPI()




DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/db-test")
def test_db():
    conn = psycopg2.connect(DATABASE_URL)
    return {"status": "connected to postgres!"}
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/health')
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)