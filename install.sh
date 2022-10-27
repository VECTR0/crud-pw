#!/bin/sh
cd backend
pip3 install -U pytest
pip3 install pytest-xdist
pip3 install -r requirements.txt
pip3 install flask
cd ..
cd frontend
npm install dotenv --save
npm install react-router-dom@6
npm install axios
rm -r node_modules
npm install
cd ..