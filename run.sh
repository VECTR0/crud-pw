#!/bin/sh
cd backend
flask --app app run &
cd ../frontend
call npm start
cd ..