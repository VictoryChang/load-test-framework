# Load Test Framework

## Motivation
Create a Load API Test Framework, built with the python open source library locust, that is simple to read, run, and extend.

## Design Pattern
Locust uses the concept of "Users" as a method of structuring performance tests with code. Configurable properties include: how long a user waits between calls, the total number of users to test with, and how quickly they are added to the test.

```python
from random import randint
import logging

from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)
    @task
    def get_fast(self):
        self.client.get("/fast")
```


## Environment Setup
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt


## Running Basic Load Tests, that do not require authentication
1. Run a local server built using FastAPI
    1. python main.py

2. Run the locust load test application
    1. UI: locust --users 1 --spawn-rate 1 -H http://0.0.0.0:8000
    2. Headless Mode: locust --users 1 --spawn-rate 1 -H http://0.0.0.0:8000 --headless

## Types of Tests

|Test|Description|Total Users|Ramp Up Speed (per second)|Duration|
|---|---|---|---|---|
|Load|Real-life Application Load|10|1|Standard|
|Stress|Finding the first bottleneck|1000|1|Standard|
|Spike|Sudden High Ramp Up|1000|1000|Short|
|Endurance|Slow Ramp Up, Long Period of Time|10|1|Long|


## Analyzing the Results
To be added