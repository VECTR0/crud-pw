#!/bin/sh
cd backend
flask --app app run &
cd ..
cd frontend
call npm start
cd ..