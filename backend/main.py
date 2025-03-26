from fastapi import FastAPI
from backend.model import generate_3d_model  # Импорт функции генерации модели
import sys
import os

# Добавляем путь к проекту в sys.path, чтобы Python мог находить модули
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the lamp generator API!"}
@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available."}
@app.post("/generate/")
async def generate(height: float, diameter: float, texture: str):
    model_path = generate_3d_model(height, diameter, texture)
    return {"model_path": model_path}
