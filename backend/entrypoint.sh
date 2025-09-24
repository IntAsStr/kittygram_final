#!/bin/bash

# Применяем миграции
python manage.py migrate --noinput

# Собираем статические файлы
python manage.py collectstatic --noinput

# Копируем собранные статические файлы в нужную директорию
cp -r /app/collected_static/. /backend_static/static/

# Запускаем основной процесс (команда из CMD)
exec "$@"