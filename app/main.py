import os
import traceback
from fastapi import FastAPI, HTTPException

import psycopg2
app = FastAPI()




DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/db-test")
def test_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return {"status": "connected to postgres!"}
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/health')
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)