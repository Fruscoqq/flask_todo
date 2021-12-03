from application import app, db
from application.models import Tasks
from flask import render_template, redirect, url_for, request, flash, jsonify


@app.route('/', methods=['GET'])
def index():
    tasks_list = Tasks.query.all()
    tasks_dict = {"tasks":[]}
    for task in tasks_list:
        tasks_dict["tasks"].append(
            {
                "id": task.id,
                "description": task.description,
                "laptime": task.laptime
            }
        )
    return jsonify(tasks_dict)

# Add route
@app.route('/add', methods=["POST"])
def add():
    # add new task
        new_task = Tasks(description=request.json["description"], laptime=request.json["laptime"])
        db.session.add(new_task)
        db.session.commit()
        return f"Added description {new_task.description}, laptime {new_task.laptime}"

# Get single task
@app.route('/read/<int:task_id>', methods=['GET'])
def read(task_id):
        task = Tasks.query.get(task_id)
        tasks_dict = {
            "id": task.id,
            "description": task.description,
            "laptime": task.laptime
        }
        return jsonify(tasks_dict)

# Update Route
@app.route('/update/<int:task_id>', methods=['PUT'])
def update(task_id):
        task = Tasks.query.get(task_id)
        task.description = request.json["description"]
        task.laptime = request.json["laptime"]
        db.session.commit()
        return f"Updated task ID {task_id} description {task.description}, laptime {task.laptime}"

# Delete route
@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    # delete task
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Deleted task ID: {task_id} with description: {task.description} and a laptime of {task.laptime}"
