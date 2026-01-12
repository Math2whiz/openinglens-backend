from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "backend alive"}

@app.get("/setup")
def setup():
    return {"setup": "complete"}
