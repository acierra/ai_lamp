from fastapi import FastAPI
from fastapi.responses import FileResponse
from backend.model import generate_3d_model

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the lamp generator API!"}

@app.get("/generate_shade/")
def generate_shade(height: int = 100, radius: int = 50, pattern_type: str = "smooth"):
    filename = generate_3d_model(height, radius, pattern_type)
    return FileResponse(filename, media_type="application/stl", filename=filename)
