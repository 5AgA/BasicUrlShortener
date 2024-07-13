#!/bin/bash

# SQLite 데이터베이스 파일 삭제
rm db.sqlite3

# 마이그레이션 파일 삭제
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# 마이그레이션 생성 및 적용
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver
