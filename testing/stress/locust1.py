from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):

  @task(1)
  def login(self):
    self.client.post("/",{
            "UserName": "root",
            "Password": "SOEN341echelon!"
        })

  @task(2)
  def my_task(self):
    self.client.get("/schedule_make/")

  @task(3)
  def my_task2(self):
    self.client.get("/schedule_view/")

  @task(4)
  def my_task3(self):
    self.client.get("/browse_all_courses/")

class MyLocust(HttpLocust):
  task_set = MyTaskSet
  host = "http://localhost:8000"
  min_wait = 5000
  max_wait = 5000
