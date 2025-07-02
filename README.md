# Load Test Framework

## Motivation
Create a Load API Test Framework, built with the python open source library locust, that is simple to read, run, and extend.


## Environment Setup
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt


## Running Basic Load Tests, that do not require authentication
1. Run a local server built using FastAPI
    1. python main.py
2. Run the locust load test application
    1. locust --users 1 --spawn-rate 1 -H http://0.0.0.0:8000/


## Analyzing the Results
To be added