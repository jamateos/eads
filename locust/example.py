import random
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")
    @task(4)
    def vote(self):
        choices = ["a", "b"]
        secure_random=random.SystemRandom()
        self.client.post("/", {"vote": secure_random.choice(choices)})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
