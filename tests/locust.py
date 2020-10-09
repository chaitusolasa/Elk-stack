from locust import HttpLocust, TaskSet, task
class UserBehavior(TaskSet):
  def on_start(self):
      self.client.get("/")
 
  @task(1)
  def posts(self):
      self.client.get("/_cat/indices?v")
 
  
 
class WebsiteUser(HttpLocust):
  task_set = UserBehavior
  min_wait = 1000
  max_wait = 2000
