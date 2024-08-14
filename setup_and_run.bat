@echo off
python inicio.py
psql -U postgres -f setup_database.sql
python comandos.py
pause