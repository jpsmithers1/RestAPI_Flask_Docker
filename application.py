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
  app.run(host='0.0.0.0')
  
# to test the api 
# add item to list - curl -X POST -H "Content-Type: application/json" -d '{"task": "Buy milk"}' http://localhost:5000/tasks
# to retrieve list - curl http://localhost:5000/tasks/0