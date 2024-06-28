Экзамеционный проект академии TOP.

Сайт по предоставлению геодезических и кадастровых работ.

Клонируйте репозиторий:
git clone https://github.com/yourusername/yourproject.git cd yourproject

Создайте и активируйте виртуальное окружение:
python -m venv venv source venv/bin/activate # для Windows: venv\Scripts\activate

Установите зависимости:
pip install -r requirements.txt

Скопируйте файл .env.example и переименуйте его в .env:
cp .env.example .env

Откройте файл .env и заполните следующие переменные окружения:
SECRET_KEY= Введите секретный ключ Джанго

DATABASE_URL=Введите путь к базе данных

DEBUG=Режим Debug

TELEGRAM_BOT_TOKEN=<ваш_токен_бота>

YOUR_PERSONAL_CHAT_ID=<ваш_чат_айди>

Примените миграции:
python manage.py migrate

Создайте суперпользователя для доступа к админ-панели Django:
python manage.py createsuperuser

Запустите сервер разработки:
python manage.py runserver
