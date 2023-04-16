from behave import *
import json
from application.flaskapplication import app

@given('a buy milk task is added to the task list')
def step_impl(context):
    response = app.test_client().post("/tasks", json={"task": "Buy milk"})
    assert response.status_code == 201

@then('buy milk task should be returned in task list')
def step_impl(context):
    response = app.test_client().get('/tasks/0')
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert data["task"] == "Buy milk"
