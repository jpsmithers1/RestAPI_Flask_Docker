from flask import Flask, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def add_task():
  task = request.get_json()
  tasks.append(task)
  return '', 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = tasks[task_id]
  return task

if __name__ == '__main__':
# If running in Azure as a WebApp use app.run() - and make sure pythjong file is named application.py
  app.run()
# if running in the docker container locally use app.run(host = "0.0.0.0")
# This tells the server to listen on all networks, not just to localhost connections, otherwise the server is only accessible from within the container and not on the host when the container is run

# to test the api locally
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://localhost:5000/tasks
# to retrieve list - curl http://localhost:5000/tasks/0

# to test the api via the container - use docker run -p 0.0.0.0:8000:5000 <image name>
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://0.0.0.0:8000/tasks
# to retrieve list - curl http://0.0.0.0:8000/tasks/0

# to test the api when deployed to Azure WebApp
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://<Azure WebApp Name>/tasks
# to retrieve list - curl http://<Azure WebApp Name>/tasks/0
