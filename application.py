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
#setting the host to 0.0.0.0 tells the server to listen on all networks, not just to localhost connections, otherwise the server is only accessible from within the container and not on the host when the container is run
  app.run()
  
# to test the api locally
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://localhost:5000/tasks
# to retrieve list - curl http://localhost:5000/tasks/0


# to test the api via the container - use docker run -p 0.0.0.0:8000:5000 <image name>
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://0.0.0.0:8000/tasks
# to retrieve list - curl http://0.0.0.0:8000/tasks/0