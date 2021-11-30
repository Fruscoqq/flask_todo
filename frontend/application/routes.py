from application import app
from flask import render_template, redirect, url_for, flash, jsonify, request
import requests

@app.route('/')
def index():
    tasks_list = requests.get("http://trackhub-backend:5000/").json()
    app.logger.info(f"Tasks: {tasks_list}")
    return render_template('index.html', tasks_list=tasks_list["tasks"])

#Add route
@app.route('/add', methods=["POST"])
def add():
    # add new task
    description = request.form.get("description")
    laptime = request.form.get("laptime")
    if description == "":
        flash("Something went wrong", "newWarning")
        return redirect(url_for("index"))
    else:
        response = requests.post("http://trackhub-backend:5000/add", json = {"description": description,
        "laptime": laptime})
        flash("Your item has been added successfully", "newSuccess")
        return redirect(url_for("index"))

# Update Route
@app.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update(task_id):
    task = requests.get(f"http://trackhub-backend:5000/read/{task_id}").json()
    if request.method == 'POST':
        response = requests.put(f"http://trackhub-backend:5000/update/{task_id}", json = {"description": request.form['description'],
        "laptime": request.form['laptime']})
        return redirect(url_for('index'))
    else:
        flash("Your item was updated successfully", "newSuccess")
        return render_template('update.html', task=task)

# Delete route
@app.route('/delete/<int:task_id>')
def delete(task_id):
    # delete task
    response = requests.delete(f"http://trackhub-backend:5000/delete/{task_id}")
    flash("Your item has been deleted", "newDanger")
    return redirect(url_for("index"))

