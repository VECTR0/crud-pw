#!/bin/sh
cd backend
pip3 install -U Flask 
pip install python-dotenv
pip3 install -U pytest
pip3 install pytest-xdist
pip3 install -r requirements.txt
cd ../frontend
npm install dotenv --save
npm install react-router-dom@6
npm install axios
if [ -d node_modules ]; then rm -Rf node_modules; fi
npm install
cd ..