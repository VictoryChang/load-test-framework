import logging

from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 5)
    @task
    def get_fast(self):
        logging.info("hello from fast!")
        self.client.get("/fast")


    @task
    def get_slow(self):
        logging.info("hello from slow!")
        self.client.get("/slow")