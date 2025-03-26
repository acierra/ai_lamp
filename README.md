AI Lamp Shade Generator
Description:
AI Lamp Shade Generator is a web-based application that utilizes artificial intelligence to design and generate 3D-printable lampshades. The tool allows users to create custom lampshades while ensuring compatibility with a standard lamp base. The generated 3D models are available for further customization and can be exported in a format suitable for 3D printing.

Features:

AI-powered lampshade design – Generates unique 3D lampshade models using neural networks.

Customizable dimensions – Users can adjust size and shape parameters.

3D model preview – View the design before exporting.

Export for 3D printing – Supports STL and OBJ file formats.

User-friendly web interface – Easy-to-use platform for designers and makers.

Technology Stack:

Frontend: Vue.js (or React)

Backend: FastAPI (Python)

AI Model: PyTorch-based neural network

3D Processing: Trimesh, OpenSCAD

Database: PostgreSQL / SQLite

Deployment: Docker, AWS/GCP

How It Works:

The AI model generates a lampshade design based on user input.

The design is visualized in a 3D preview.

Users can adjust dimensions and other parameters.

The final model is exported as an STL/OBJ file for 3D printing.

This project aims to simplify the process of creating custom lampshades while leveraging AI for unique and efficient designs.



Как восстановить виртуальное окружение на другом компьютере
Если клонируешь репозиторий на другой компьютер, выполни:

cd ai_lamp
python -m venv venv  # Создаём виртуальное окружение
source venv/bin/activate  # Активируем (Mac/Linux)
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt  # Устанавливаем зависимости
