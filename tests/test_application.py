import pytest
import json
from application.flaskapplication import app

def test_add_tasks():
    """Test the adding of a task"""
    response = app.test_client().post("/tasks", json={"task": "Buy milk"})
    assert response.status_code == 201
   
def test_list_tasks():
    """Test the endpoint to list out tasks"""
    response = app.test_client().get('/tasks/0')
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert data["task"] == "Buy milk"

def test_index_wrong_route():
    """Test for wrong route"""
    response = app.test_client().get("/wrong_route")
    assert response.status_code == 404
    
    
    
    
    