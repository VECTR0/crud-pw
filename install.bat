@echo off
cd backend
pip install -U pytest
pip install pytest-xdist
pip install -r requirements.txt
pip install flask
cd ..
cd frontend
call npm install dotenv --save
call npm install react-router-dom@6
call npm install axios
RMDIR /S /Q node_modules
call npm install
cd ..
pause