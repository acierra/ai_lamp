Как восстановить виртуальное окружение на другом компьютере
Если клонируешь репозиторий на другой компьютер, выполни:

cd ai_lamp
python -m venv venv  # Создаём виртуальное окружение
source venv/bin/activate  # Активируем (Mac/Linux)
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt  # Устанавливаем зависимости
