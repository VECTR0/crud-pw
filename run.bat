@echo off
cd backend
start flask --app app run
cd ../frontend
start call npm start
cd ..