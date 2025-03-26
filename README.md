Как восстановить виртуальное окружение на другом компьютере
Если клонируешь репозиторий на другой компьютер, выполни:

bash
Копировать
Редактировать
git clone https://github.com/ТВОЙ_ЛОГИН/ai_lamp.git
cd ai_lamp
python -m venv venv  # Создаём виртуальное окружение
source venv/bin/activate  # Активируем (Mac/Linux)
venv\Scripts\activate  # Для Windows
pip install -r requirements.txt  # Устанавливаем зависимости
