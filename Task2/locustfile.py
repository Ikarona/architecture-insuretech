from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:8081"   # будет проксироваться портом

    @task
    def index(self):
        self.client.get("/")