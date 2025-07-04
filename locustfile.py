from random import randint
import logging

from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)
    @task
    def get_fast(self):
        self.client.get("/fast")

    @task
    def get_slow(self):
        logging.info('send log to locust ui')
        self.client.get("/slow")

    @task
    def get_user(self):
        user_id = randint(1,4)
        self.client.get(f"/users/{user_id}")

    @task
    def get_user_group_by_name(self):
        user_id = randint(1,4)
        self.client.get(f"/users/{user_id}", name="/users/userId")
