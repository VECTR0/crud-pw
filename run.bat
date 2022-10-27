@echo off
cd backend
start flask --app app run
cd ..
cd frontend
start call npm start
cd ..