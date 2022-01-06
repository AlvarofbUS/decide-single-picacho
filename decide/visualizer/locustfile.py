import json

from random import choice

from locust import (
    HttpUser,
    TaskSet,
    task,
    between)

HOST = "http://127.0.0.1:8000"
VOTING = 1

class DefVisualizer(TaskSet):

    @task
    def index(self):
        self.client.get("/visualizer/{0}/".format(VOTING))

class Visualizer(HttpUser):
    host = HOST
    tasks = [DefVisualizer]
    wait_time = between(3,5)
